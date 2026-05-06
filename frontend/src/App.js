import React, { useEffect, useState } from "react";
import "./App.css";

function App() {

  const [incidents, setIncidents] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/incidents")
      .then((response) => response.json())
      .then((data) => {
        setIncidents(data);
      });

  }, []);

  return (
    <div className="container">

      <h1>Incident Management Dashboard</h1>

      <div className="incident-list">

        {incidents.map((incident) => (

          <div className="incident-card" key={incident.id}>

            <h3>{incident.component_id}</h3>

            <p>
              <strong>Severity:</strong> {incident.severity}
            </p>

            <p>
              <strong>Status:</strong> {incident.status}
            </p>

            <p>
              <strong>Message:</strong> {incident.message}
            </p>

            <p>
              <strong>MTTR:</strong> {
                incident.mttr_minutes !== null
                  ? `${incident.mttr_minutes} mins`
                  : "N/A"
              }
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}

export default App;