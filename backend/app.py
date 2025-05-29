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
                venue = event['_embedded']['venues'][0].get('name', 'N/A')
                city = event['_embedded']['venues'][0]['city'].get('name', 'N/A')
                url = event.get('url', '#')

                result.append({
                    'name': name,
                    'date': date,
                    'venue': venue,
                    'city': city,
                    'url': url
                })
            except Exception as e:
                continue  # Skip malformed event

        return jsonify({'events': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

