# 🏀 Basketball Events Web App

This project displays a list of upcoming **Basketball matches** using the **Ticketmaster Discovery API**. It includes a simple **Flask backend** and a **React frontend** that shows the teams playing, scheduled date and time, venue, and a link to the event.

---

## 📌 Features

- 🏟️ Shows upcoming basketball matches in the US  
- 🕒 Displays scheduled date and time  
- 🧾 Lists venue and city  
- 🔗 Links to official event pages  
- 🔁 Automatically fetches fresh data on page load  
- 🌐 React-based UI + Flask backend

---

## 📡 API Used

- **API Name:** Ticketmaster Discovery API  
- **Endpoint:** [`https://app.ticketmaster.com/discovery/v2/events.json`](https://app.ticketmaster.com/discovery/v2/events.json)  
- **Query Example:**
  ```
  https://app.ticketmaster.com/discovery/v2/events.json?keyword=basketball&countryCode=US&apikey=YOUR_API_KEY
  ```

---

## 🗂️ Project Structure

```
basketball-events-app/
├── backend/
│   └── app.py            # Flask backend to fetch basketball events
├── frontend/
│   ├── public/
│   └── src/
│       └── App.js        # React component displaying event cards
├── README.md             # Project documentation
```

---

## 🚀 How to Run

### 🧠 Prerequisites

- Python 3.x  
- Node.js and npm

---

### ⚙️ Backend Setup (Flask)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install flask flask-cors requests
python app.py
```

Runs on: `http://127.0.0.1:5000/api/basketball-events`

---

### 💻 Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

Runs on: `http://localhost:3000`



---

## ✅ Example Output

```json
{
  "team1": "Los Angeles Lakers",
  "team2": "Boston Celtics",
  "date": "2025-06-12",
  "time": "19:00",
  "venue": "Crypto.com Arena",
  "city": "Los Angeles",
  "url": "https://www.ticketmaster.com/event/XYZ"
}
```

---

## 📝 Assignment Requirements

| Requirement                  | Status |
|-----------------------------|--------|
| Basketball or Soccer match  | ✅     |
| Used a free public API      | ✅     |
| Displayed teams and date    | ✅     |
| Included optional backend   | ✅     |
| Hosted on GitHub            | ✅     |

---

## 🔗 Submission

- **GitHub Repo:** [https://github.com/SnehaGupta02/basketball-events-app](https://github.com/SnehaGupta02/basketball-events-app)
- **API Used:** [Ticketmaster Discovery API](https://app.ticketmaster.com/discovery/v2/events.json)

---

## 👩‍💻 Author

**Sneha Gupta**   
Made with ❤️ for the internship assignment.
