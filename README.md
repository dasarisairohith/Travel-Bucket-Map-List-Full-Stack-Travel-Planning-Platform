# 🌍 Travel Bucket Map List

A full-stack travel planning platform that helps users **discover, organize, visualize, and track travel destinations** using interactive maps, categorized bucket lists, and trip management.

Built with **React.js, Flask, MySQL, Leaflet, and Google Maps API**.

---

## 🚀 Features

### 🔐 Authentication

* User registration and login
* JWT-based authentication
* Secure password hashing
* Protected API endpoints
* User-specific travel data

### 📍 Destination Management

* Add travel destinations
* Edit destination information
* Delete destinations
* Store city and country
* Store latitude and longitude
* Add personal notes
* Set destination priority
* Mark destinations as visited

### 🗺️ Interactive Maps

* Interactive world map using Leaflet
* Destination markers
* Map-based destination visualization
* Marker popups with destination information
* Zoom and pan support

### 🏷️ Categories

Destinations can be organized into categories:

* Beach
* Mountains
* City
* Historical
* Adventure
* Food
* Other

### ⭐ Priority Tracking

Each destination can have:

* Low priority
* Medium priority
* High priority

### ✈️ Trip Management

* Create trips
* Add descriptions
* Set start and end dates
* Set trip status
* Associate destinations with trips
* Delete trips

### 📊 Dashboard

The dashboard provides travel statistics including:

* Total destinations
* Visited destinations
* Wishlist destinations
* Number of trips
* Number of countries

### 🔎 Google Places Integration

The backend supports Google Places API integration for destination and location search.

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Vite
* JavaScript
* React Router
* Axios
* Leaflet
* React Leaflet
* CSS

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Flask-CORS
* Requests
* Werkzeug

## Database

* MySQL
* SQLAlchemy ORM

## APIs & Services

* REST API
* Leaflet
* OpenStreetMap
* Google Places API

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      React.js        │
                    │      Frontend        │
                    └──────────┬───────────┘
                               │
                               │ Axios / REST API
                               │ JWT
                               ▼
                    ┌──────────────────────┐
                    │        Flask         │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          ┌──────────┐   ┌───────────┐  ┌────────────┐
          │  MySQL   │   │  Google   │  │  Leaflet   │
          │ Database │   │  Places   │  │    Maps    │
          └──────────┘   └───────────┘  └────────────┘
```

---

# 📁 Project Structure

```text
travel-bucket-map/
│
├── backend/
│   │
│   ├── app/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── destinations.py
│   │   │   ├── trips.py
│   │   │   ├── dashboard.py
│   │   │   └── places.py
│   │   │
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   ├── .env.example
│   ├── config.py
│   ├── requirements.txt
│   └── run.py
│
├── database/
│   └── schema.sql
│
├── frontend/
│   │
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   ├── main.jsx
│   │   └── styles.css
│   │
│   ├── .env.example
│   ├── index.html
│   └── package.json
│
├── .gitignore
└── README.md
```

---

# 🗄️ Database Schema

The application uses MySQL to persist user and travel information.

## Users

```text
users
├── id
├── name
├── email
├── password_hash
└── created_at
```

## Destinations

```text
destinations
├── id
├── user_id
├── name
├── country
├── city
├── latitude
├── longitude
├── category
├── priority
├── visited
├── notes
└── created_at
```

## Trips

```text
trips
├── id
├── user_id
├── name
├── description
├── start_date
├── end_date
└── status
```

## Trip-Destination Relationship

```text
trip_destinations
├── trip_id
└── destination_id
```

This creates a many-to-many relationship between trips and destinations.

---

# ⚙️ Installation

## Prerequisites

Install the following:

* Python 3.10+
* Node.js 18+
* npm
* MySQL 8+

Verify:

```bash
python --version
node --version
npm --version
mysql --version
```

---

# 🗄️ 1. Create MySQL Database

Open MySQL:

```bash
mysql -u root -p
```

Create the database:

```sql
CREATE DATABASE travel_bucket;
```

Verify:

```sql
SHOW DATABASES;
```

---

# 🐍 2. Setup Backend

Navigate to the backend:

```bash
cd backend
```

Create a Python virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 4. Configure Backend Environment

Create a `.env` file inside `backend/`.

Example:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/travel_bucket

JWT_SECRET_KEY=your-secret-key

GOOGLE_MAPS_API_KEY=your-google-api-key

FRONTEND_URL=http://localhost:5173
```

Replace the MySQL username and password with your own credentials.

---

# ▶️ 5. Run Backend

Inside the `backend` directory:

```bash
python run.py
```

The Flask API will run at:

```text
http://localhost:5000
```

Test:

```text
http://localhost:5000/api/health
```

Expected:

```json
{
  "status": "ok"
}
```

---

# ⚛️ 6. Setup Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

---

# 🔑 7. Configure Frontend

Create:

```text
frontend/.env
```

Add:

```env
VITE_API_URL=http://localhost:5000/api
```

---

# ▶️ 8. Run Frontend

```bash
npm run dev
```

Open the URL displayed by Vite, usually:

```text
http://localhost:5173
```

---

# 🔐 Authentication Flow

```text
User
  │
  ▼
Login / Register
  │
  ▼
React Frontend
  │
  │ POST /api/auth/login
  ▼
Flask Backend
  │
  ▼
MySQL
  │
  ▼
JWT Token
  │
  ▼
React
  │
  ▼
Protected API Requests
```

The JWT token is sent with protected requests:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

# 🔌 API Endpoints

## Authentication

| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| POST   | `/api/auth/register` | Register user    |
| POST   | `/api/auth/login`    | Login            |
| GET    | `/api/auth/me`       | Get current user |

## Destinations

| Method | Endpoint                 | Description        |
| ------ | ------------------------ | ------------------ |
| GET    | `/api/destinations`      | Get destinations   |
| POST   | `/api/destinations`      | Add destination    |
| GET    | `/api/destinations/<id>` | Get destination    |
| PUT    | `/api/destinations/<id>` | Update destination |
| DELETE | `/api/destinations/<id>` | Delete destination |

## Trips

| Method | Endpoint                                             | Description        |
| ------ | ---------------------------------------------------- | ------------------ |
| GET    | `/api/trips`                                         | Get trips          |
| POST   | `/api/trips`                                         | Create trip        |
| PUT    | `/api/trips/<id>`                                    | Update trip        |
| DELETE | `/api/trips/<id>`                                    | Delete trip        |
| POST   | `/api/trips/<trip_id>/destinations/<destination_id>` | Add destination    |
| DELETE | `/api/trips/<trip_id>/destinations/<destination_id>` | Remove destination |

## Dashboard

| Method | Endpoint               | Description           |
| ------ | ---------------------- | --------------------- |
| GET    | `/api/dashboard/stats` | Get travel statistics |

## Places

| Method | Endpoint                       | Description   |
| ------ | ------------------------------ | ------------- |
| GET    | `/api/places/search?q=<query>` | Search places |

---

# 📍 Example Destination Request

```http
POST /api/destinations
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
```

```json
{
  "name": "Eiffel Tower",
  "city": "Paris",
  "country": "France",
  "latitude": 48.8584,
  "longitude": 2.2945,
  "category": "City",
  "priority": "High",
  "visited": false,
  "notes": "Visit during sunset."
}
```

---

# ✈️ Example Trip Request

```http
POST /api/trips
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
```

```json
{
  "name": "European Summer Trip",
  "description": "Two-week European vacation",
  "start_date": "2027-06-10",
  "end_date": "2027-06-25",
  "status": "Planned"
}
```

---

# 🗺️ Map Implementation

The application uses **React Leaflet** to display destinations.

Destination coordinates are stored in MySQL:

```text
latitude
longitude
```

The frontend converts these coordinates into map markers.

```text
MySQL
  │
  ▼
Flask API
  │
  ▼
React
  │
  ▼
React Leaflet
  │
  ▼
Interactive Map
```

---

# 🌐 Google Places API

Google Places API can be used to search for destinations.

Configure the backend:

```env
GOOGLE_MAPS_API_KEY=YOUR_API_KEY
```

Then call:

```text
GET /api/places/search?q=Tokyo
```

The API key should be kept in environment variables and should not be committed to GitHub.

---

# 🔒 Security

The project implements:

* Password hashing
* JWT authentication
* Protected endpoints
* User-level data isolation
* Environment-based secrets
* CORS configuration

Sensitive values should never be hardcoded.

Do not commit:

```text
.env
```

to GitHub.

---

# 🧪 Testing

The REST API can be tested using:

* Postman
* Insomnia
* Thunder Client
* cURL

Example:

```bash
curl http://localhost:5000/api/health
```

---

# 🔄 Application Workflow

```text
Register
   │
   ▼
Login
   │
   ▼
Dashboard
   │
   ├───────────────┐
   ▼               ▼
Destinations      Trips
   │               │
   ▼               ▼
Add Location      Create Trip
   │               │
   ▼               ▼
Leaflet Map       Add Destinations
   │               │
   └───────┬───────┘
           ▼
      Travel Planning
```

---

# 📊 Dashboard Statistics

The dashboard calculates:

```text
Total Destinations
        │
        ├── Visited
        │
        └── Wishlist

Total Trips

Unique Countries
```

Example:

```text
Destinations: 20
Visited: 8
Wishlist: 12
Trips: 4
Countries: 7
```

---

# 🚀 Future Enhancements

Possible improvements include:

### 🧭 Advanced Travel Planning

* Route optimization
* Distance calculation
* Travel time estimation
* Multi-city itinerary planning
* Daily itinerary management

### 🌦️ External APIs

* Weather API
* Flight API
* Hotel API
* Currency conversion
* Local attractions API

### 💰 Budget Management

* Trip budget
* Accommodation expenses
* Food expenses
* Transportation expenses
* Total spending analytics

### 👥 Social Features

* Public profiles
* Shared bucket lists
* Public trips
* Follow travelers
* Destination reviews

### 🔔 Notifications

* Upcoming trip reminders
* Destination reminders
* Travel checklist notifications

---

# 💼 Resume Project Description

**Travel Bucket Map List**
*React.js, Flask, MySQL, Leaflet, Google Maps API*

> Built a full-stack travel planning platform for visualizing, organizing, and tracking destinations through interactive maps and categorized travel lists. Implemented Flask REST APIs with MySQL persistence and JWT authentication, integrating Leaflet/Google Maps for location visualization and responsive dashboards for managing trips, destinations, priorities, and notes.

---

# 🧠 Skills Demonstrated

```text
React.js
JavaScript
Python
Flask
REST API Development
MySQL
SQLAlchemy
JWT Authentication
Axios
Leaflet
Google Maps API
CRUD Operations
Database Design
API Integration
Authentication
Authorization
Responsive Web Development
Full-Stack Development
```

---

# 👨‍💻 Author

**Dasari Sai Rohith**

---

# 📜 License

This project is intended for educational, portfolio, and demonstration purposes.
