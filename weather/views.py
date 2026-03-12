from django.shortcuts import render ,redirect
from .models import Subscriber
from django.core.mail import send_mail
import requests

API_KEY = "9d32635a6432bc834001c7f7df3e0702"

def home(request):

    weather_data = None
    forecast_list = None

    if request.method == "POST":

        city = request.POST['city']

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        # AQI API
        aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        aqi_response = requests.get(aqi_url)
        aqi_data = aqi_response.json()

        aqi = aqi_data["list"][0]["main"]["aqi"]

        aqi_text = {
            1: "Good 🟢",
            2: "Fair 🟡",
            3: "Moderate 🟠",
            4: "Poor 🔴",
            5: "Very Poor 🟣"
        }

        aqi_status = aqi_text.get(aqi, "Unknown")

        # Forecast API
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        forecast_list = forecast_data["list"][:5]

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "aqi": aqi,
            "aqi_status": aqi_status
        }

    return render(request, 'index.html', {
        "weather": weather_data,
        "forecast": forecast_list
    })


# 🌍 GPS Location Weather


def location_weather(request):

    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    # AQI API
    aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    aqi_response = requests.get(aqi_url)
    aqi_data = aqi_response.json()

    aqi = aqi_data["list"][0]["main"]["aqi"]

    aqi_text = {
        1: "Good 🟢",
        2: "Fair 🟡",
        3: "Moderate 🟠",
        4: "Poor 🔴",
        5: "Very Poor 🟣"
    }

    aqi_status = aqi_text.get(aqi, "Unknown")

    # Forecast API
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    #forecast_list = forecast_data["list"][:5]
    forecast_list = forecast_data["list"][::8][:5]

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "aqi": aqi,
        "aqi_status": aqi_status
    }

    return render(request, "index.html", {
        "weather": weather_data,
        "forecast": forecast_list
    })
def subscriber(request):
    if request.method == "POST":
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST['city']
        Subscriber.objects.create(
            email=email,
            phone=phone,
            city=city
        )
    return redirect("/")   

def send_weather_alert(email, city):
    subject = "Weather Alert"
    message = f"Weather change detected in {city}. Please check forecast."
    send_mail(
        subject,
        message,
        "yourgmail@gmail.com",
        [email],
        fail_silently=False
    )
