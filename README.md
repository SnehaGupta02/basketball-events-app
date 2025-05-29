# 🏀 Basketball Matches App

This is a simple full-stack web application that displays a list of upcoming basketball matches using the [Ticketmaster Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/).

## 📌 Features

- Fetches live basketball event data from Ticketmaster
- Displays name, date, venue, city, and link to each match
- Built with:
  - **Frontend:** React
  - **Backend:** Flask (Python)
  - **API Source:** Ticketmaster

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/basketball-matches.git
cd basketball-matches
###Backend Setup
cd backend
pip install -r requirements.txt
Create a .env file or add your Ticketmaster API key in app.py:
TICKETMASTER_API_KEY = 'your_ticketmaster_api_key'
Start the Flask server:
python app.py
### Frontend Setup (React)
bash
Copy
Edit
cd basketball-matches
npm install
npm start
🙌 Acknowledgements
Ticketmaster API

Create React App

Flask
