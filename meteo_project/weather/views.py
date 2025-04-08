# weather/views.py

import requests  # Pour effectuer la requête à l'API externe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

def get_weather_data(city):
    # Appel à l'API externe OpenWeatherMap
    api_key = '372c13e831b69621bce9dfb244df8858'  # Remplace par ta clé API OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        # Si la réponse est un succès (code 200)
        if response.status_code == 200:
            data = response.json()  # Récupère les données au format JSON
            return {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            raise ValidationError(f"Erreur lors de la récupération des données météo pour {city}.")
    except requests.exceptions.RequestException as e:
        raise ValidationError(f"Erreur de connexion à l'API météo : {str(e)}")

class WeatherAPIView(APIView):
    def get(self, request, *args, **kwargs):
        city = request.query_params.get('city')  # Récupère le paramètre city
        if not city:
            raise ValidationError("City parameter is required.")  # Si city est absent, lève une exception

        try:
            weather_data = get_weather_data(city)  # Récupère les données météo
            return Response(weather_data, status=status.HTTP_200_OK)  # Réponse OK avec les données
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)  # Erreur si la ville n'est pas trouvée
