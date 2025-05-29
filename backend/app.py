from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TICKETMASTER_API_KEY = 'cTvgfXULHCKVUx361hfLaaGEfA3AbFj7'

@app.route('/api/basketball-events', methods=['GET'])
def get_basketball_events():
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        'keyword': 'basketball',
        'apikey': TICKETMASTER_API_KEY,
        'size': 10,
        'countryCode': 'US'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if '_embedded' not in data:
            return jsonify({'events': []})

        events = data['_embedded'].get('events', [])
        result = []

        for event in events:
            try:
                name = event.get('name', 'N/A')
                date = event['dates']['start'].get('localDate', 'N/A')
                time = event['dates']['start'].get('localTime', '')
                venue = event['_embedded']['venues'][0].get('name', 'N/A')
                city = event['_embedded']['venues'][0]['city'].get('name', 'N/A')
                url = event.get('url', '#')

                # Try splitting team names
                if ' vs ' in name.lower():
                    parts = name.lower().split(' vs ')
                elif ' VS ' in name:
                    parts = name.split(' VS ')
                else:
                    parts = [name, 'TBD']

                team1 = parts[0].strip().title()
                team2 = parts[1].strip().title() if len(parts) > 1 else 'TBD'

                result.append({
                    'team1': team1,
                    'team2': team2,
                    'date': date,
                    'time': time,
                    'venue': venue,
                    'city': city,
                    'url': url
                })
            except Exception as e:
                print(f"Error parsing event: {e}")
                continue

        return jsonify({'events': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

