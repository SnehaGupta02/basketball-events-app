import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:5000/api/basketball-events')
      .then((response) => response.json())
      .then((data) => {
        setEvents(data.events || []);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching events:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>Upcoming Basketball Matches</h1>
      {loading ? (
        <p>Loading matches...</p>
      ) : events.length === 0 ? (
        <p>No events found.</p>
      ) : (
        <div className="event-list">
          {events.map((event, index) => (
            <div key={index} className="event-card">
              <h2>{event.team1} vs {event.team2}</h2>
              <p><strong>Date:</strong> {event.date} {event.time && `at ${event.time}`}</p>
              <p><strong>Venue:</strong> {event.venue}, {event.city}</p>
              <a href={event.url} target="_blank" rel="noopener noreferrer">View Details</a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;

