# 🌤 Django Weather Dashboard

A modern **Weather Web Application** built using **Python Django**.
This project allows users to check **live weather, AQI, 5-day forecast, and air quality maps**.
Users can also **subscribe with email and phone** to receive weather alerts.

---

## 🚀 Features

* 🌍 Live Weather by City
* 📍 Weather using GPS location
* 🌫 Air Quality Index (AQI)
* 📊 5-Day Weather Forecast
* 🗺 Air Quality Heat Map
* 🔔 Weather Alert Subscription
* 📧 Email Alert System
* 🧑‍💼 Django Admin Panel for Subscribers

---

## 🛠 Tech Stack

* Python
* Django
* Bootstrap 5
* OpenWeatherMap API
* Leaflet.js (Map)
* SQLite Database

---

## 📷 Screenshots

Weather Dashboard UI with Forecast and AQI Map.

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/django-weather-app.git
cd django-weather-app
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🔑 Environment Setup

Create API key from **OpenWeatherMap** and add it to `views.py`.

Example:

```
API_KEY = "your_api_key_here"
```

---

## 📁 Project Structure

```
weather_pro/
│
├── config/
├── weather/
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## 📬 Future Improvements

* Hourly weather forecast
* Weather charts & graphs
* Push notifications
* Live rain radar
* Deployment on cloud

---

## 👨‍💻 Author

Developed by - Deepak Kumar

---

⭐ If you like this project, please give it a star on GitHub.
