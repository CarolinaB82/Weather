import requests
from django.http import JsonResponse

def weather(request):
    api_key = '372c13e831b69621bce9dfb244df8858'  # Remplace par ta clé API OpenWeatherMap
    city = 'Paris'  # Ville par défaut
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return JsonResponse({'error': 'City not found'}, status=404)

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }

    return JsonResponse(weather_data)
