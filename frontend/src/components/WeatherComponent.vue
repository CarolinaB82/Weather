<template>
  <div class="weather-container">
    <h1>Weather for {{ city }}</h1>

    <!-- Formulaire pour entrer le nom de la ville -->
    <div>
      <input v-model="city" @keyup.enter="getWeather(city)" placeholder="Enter city" />
      <button @click="getWeather(city)">Get Weather</button>
    </div>

    <!-- Affichage quand les données sont en cours de chargement -->
    <div v-if="loading" class="loading">Loading weather data...</div>

    <!-- Affichage quand une erreur survient -->
    <div v-if="error" class="error">{{ error }}</div>

    <!-- Affichage des données météorologiques quand elles sont disponibles -->
    <div v-if="weatherData" class="weather-data">
      <p><strong>Temperature:</strong> {{ weatherData.temperature }}°C</p>
      <p><strong>Description:</strong> {{ weatherData.description }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      city: 'Paris',  // Ville par défaut
      weatherData: null,  // Stocke les données météorologiques
      error: null,  // Gère les erreurs
      loading: false,  // Indicateur de chargement
    };
  },
  methods: {
    // Méthode pour récupérer les données météo
    async getWeather(city) {
      this.loading = true;  // Afficher le message de chargement
      this.error = null;  // Réinitialiser les erreurs
      try {
        // Effectuer la requête à l'API Django
        const response = await axios.get(`http://localhost:8000/api/weather/?city=${city}`);
        console.log('Données météo:', response.data);  // Affiche les données dans la console
        this.weatherData = response.data;  // Stocke les données météo
      } catch (error) {
        this.error = 'Erreur lors de la récupération des données météo.';  // Gérer l'erreur
        console.error('Erreur:', error);  // Affiche l'erreur dans la console
      } finally {
        this.loading = false;  // Fin du chargement
      }
    },
  },
  mounted() {
    // Appel initial pour charger les données météo pour la ville par défaut
    this.getWeather(this.city);
  },
};
</script>

<style scoped>
/* Styles pour ton composant */
.weather-container {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 30px auto;
  padding: 20px;
  max-width: 600px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #333;
}

.loading {
  color: #3498db;
  font-weight: bold;
}

.error {
  color: #e74c3c;
  font-weight: bold;
}

.weather-data p {
  font-size: 18px;
  color: #2c3e50;
}

.weather-data strong {
  font-weight: bold;
}

input {
  padding: 8px;
  margin-right: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  padding: 8px 12px;
  border-radius: 4px;
  background-color: #3498db;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}
</style>
