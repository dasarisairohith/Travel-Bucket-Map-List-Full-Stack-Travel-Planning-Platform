# Travel Bucket Map List

Full-stack travel planning platform built with React, Flask, MySQL, JWT, Leaflet, and Google Maps Places API.

## Features
- JWT authentication
- Personal travel bucket list
- Interactive Leaflet map
- Destination CRUD
- Categories, priority, visited status, notes
- Trip CRUD and destination assignment
- Dashboard statistics
- Google Places search endpoint
- Responsive React UI

## Requirements
- Python 3.10+
- Node.js 18+
- MySQL 8+

## 1. Database
Create a database:
```sql
CREATE DATABASE travel_bucket;
```
Then update `backend/.env`.

## 2. Backend
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python run.py
```

Backend runs at `http://localhost:5000`.

## 3. Frontend
```bash
cd frontend
npm install
npm run dev
```
Open the Vite URL shown in the terminal.

## Environment
Copy `.env.example` to `.env` in both frontend and backend.

Backend:
- `DATABASE_URL`
- `JWT_SECRET_KEY`
- `GOOGLE_MAPS_API_KEY`
- `FRONTEND_URL`

Frontend:
- `VITE_API_URL`
- `VITE_GOOGLE_MAPS_API_KEY`

Google Maps API key is optional for the core Leaflet map. Enable Places API if using the Google place search endpoint.

## API
Auth:
- POST `/api/auth/register`
- POST `/api/auth/login`
- GET `/api/auth/me`

Destinations:
- GET `/api/destinations`
- POST `/api/destinations`
- GET `/api/destinations/<id>`
- PUT `/api/destinations/<id>`
- DELETE `/api/destinations/<id>`

Trips:
- GET `/api/trips`
- POST `/api/trips`
- PUT `/api/trips/<id>`
- DELETE `/api/trips/<id>`
- POST `/api/trips/<id>/destinations/<destination_id>`
- DELETE `/api/trips/<id>/destinations/<destination_id>`

Dashboard:
- GET `/api/dashboard/stats`

Places:
- GET `/api/places/search?q=Paris`

## Notes
The application uses OpenStreetMap tiles through Leaflet for the interactive map. Respect OpenStreetMap tile usage policies in production.
