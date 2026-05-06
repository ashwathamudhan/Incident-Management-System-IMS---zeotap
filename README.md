# 🚨 Incident Management System

A lightweight Incident Management System built for the Zeotap Infrastructure / SRE Internship Assignment.

The project simulates basic SRE incident workflows including ingestion, tracking, RCA validation, MTTR calculation, and containerized deployment.

---

# ✨ Features

- Incident ingestion API
- Incident lifecycle tracking
- Severity-based workflows
- RCA validation for P1/P2 incidents
- MTTR (Mean Time To Resolution) calculation
- React dashboard for incident visualization
- Dockerized using Docker Compose

---

# 🛠 Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Backend          | FastAPI                 |
| Frontend         | ReactJS                 |
| Database         | SQLite                  |
| ORM              | SQLAlchemy              |
| Validation       | Pydantic                |
| Containerization | Docker & Docker Compose |

---

# 🏗 Architecture

![Architecture](screenshots/architecture.png)

---

# 🚀 Run Locally

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm start
```

---

# 🐳 Run with Docker

```bash
docker compose up --build
```

Frontend:

```bash
http://localhost:3000
```

Backend:

```bash
http://localhost:8000/docs
```

---

# 📡 API Endpoints

| Method | Endpoint                 | Purpose                |
| ------ | ------------------------ | ---------------------- |
| GET    | `/health`                | Health check           |
| POST   | `/ingest`                | Create incident        |
| GET    | `/incidents`             | List incidents         |
| PUT    | `/incidents/{id}/status` | Update incident status |

---

# 📸 Screenshots

## Swagger API

![Swagger](screenshots/swagger.png)

---

## Incident Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Docker Containers

![Docker](screenshots/docker.png)

---

# 🔍 Key Functionalities

### Incident Workflow

- OPEN
- ACKNOWLEDGED
- CLOSED

### RCA Enforcement

P1/P2 incidents require RCA before closure.

### MTTR Calculation

Automatically calculates incident resolution time.

---

# 🔮 Future Improvements

- Authentication & RBAC
- Kubernetes deployment
- Redis caching
- Monitoring integration

---

# 👨‍💻 Author

**Ashwath Amudhan C A**
