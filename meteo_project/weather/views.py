import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

# Fonction pour récupérer les coordonnées de la ville
def get_coordinates(city):
    api_key = '372c13e831b69621bce9dfb244df8858'  # Clé API OpenWeather
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            latitude = data['coord']['lat']
            longitude = data['coord']['lon']
            return latitude, longitude
        else:
            raise ValidationError(f"Erreur lors de la récupération des coordonnées pour {city}.")
    except requests.exceptions.RequestException as e:
        raise ValidationError(f"Erreur de connexion à l'API de géocodage : {str(e)}")

# Fonction pour récupérer les prévisions météo sur 5 jours
def get_weather_data(lat, lon):
    api_key = '372c13e831b69621bce9dfb244df8858'  # Clé API OpenWeather
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Filtrage des 5 premiers jours (on garde 5 valeurs horaires)
            return {
                "current": {
                    "temperature": data["list"][0]["main"]["temp"],
                    "description": data["list"][0]["weather"][0]["description"],
                    "humidity": data["list"][0]["main"]["humidity"],
                    "wind_speed": data["list"][0]["wind"]["speed"],
                    "icon": data["list"][0]["weather"][0]["icon"],
                },
                "hourly": data["list"][:5],  # Prochaines 5 heures
                "daily": data["list"][::8][:5],  # Prenons les prévisions journalières (1 tous les 8 éléments)
            }
        else:
            raise ValidationError(f"Erreur lors de la récupération des données météo pour ({lat}, {lon}).")
    except requests.exceptions.RequestException as e:
        raise ValidationError(f"Erreur de connexion à l'API météo : {str(e)}")

# Fonction pour récupérer l'image de fond de la ville
def get_background_image(city):
    pexels_api_key = 'WEM3MGK7BEKIq0BWZvuJQyVlYm2VCndVYAkDnCBA6NBpI2bmfoPz0KS4'  # Clé API Pexels
    url = f'https://api.pexels.com/v1/search?query={city}&per_page=1'

    headers = {
        'Authorization': f'Bearer {pexels_api_key}',
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if len(data['photos']) > 0:
                return data['photos'][0]['src']['original']
            else:
                # Si aucune image n'est trouvée, retourner une image par défaut
                return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.alamy.com%2Fstock-photo%2Fplace-du-capitole-toulouse.html&psig=AOvVaw2W-juxLxP2N9RfHr6BQteJ&ust=1744544527561000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMiOnvq00owDFQAAAAAdAAAAABAE"  # Remplace par une URL d'image par défaut
        else:
            # En cas d'erreur avec l'API Pexels, retourner une image par défaut
            return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.alamy.com%2Fstock-photo%2Fplace-du-capitole-toulouse.html&psig=AOvVaw2W-juxLxP2N9RfHr6BQteJ&ust=1744544527561000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMiOnvq00owDFQAAAAAdAAAAABAE"  # Remplace par une URL d'image par défaut
    except requests.exceptions.RequestException as e:
        # Si l'API échoue, retourne une image par défaut
        return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.alamy.com%2Fstock-photo%2Fplace-du-capitole-toulouse.html&psig=AOvVaw2W-juxLxP2N9RfHr6BQteJ&ust=1744544527561000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMiOnvq00owDFQAAAAAdAAAAABAE"  # Remplace par une URL d'image par défaut


class WeatherAPIView(APIView):
    def get(self, request, *args, **kwargs):
        city = request.query_params.get('city')
        if not city:
            raise ValidationError("Le paramètre 'city' est requis.")

        try:
            lat, lon = get_coordinates(city)
            weather_data = get_weather_data(lat, lon)
            background_image = get_background_image(city)

            return Response({
                'current': weather_data['current'],
                'hourly': weather_data['hourly'],
                'daily': weather_data['daily'],
                'backgroundImage': background_image
            }, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
