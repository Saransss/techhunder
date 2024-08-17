import requests
from django.conf import settings
from django.shortcuts import render
def home(request):
    weather_data = None
    error = None

    if request.method == "POST":
        location = request.POST.get('location')
        api_key = '47e7a962e49319b088a423de9c62b238'  # Your API Key
        
        # OpenWeatherMap API URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"

        # API Call
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'location': data['name'],
                'temp': data['main']['temp'],
                'icon': data['weather'][0]['icon'],
                'description': data['weather'][0]['description']
            }
        else:
            error = "Location not found or API Error."

    return render(request, 'home.html', {'weather_data': weather_data, 'error': error})
