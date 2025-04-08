<template>
  <div id="app">
    <h1 v-if="weather.city">Weather in {{ weather.city }}</h1>
    <p v-if="weather.temperature">Temperature: {{ weather.temperature }} °C</p>
    <p v-if="weather.description">Description: {{ weather.description }}</p>
    <p v-if="weather.humidity">Humidity: {{ weather.humidity }}%</p>
    <p v-if="weather.wind_speed">Wind Speed: {{ weather.wind_speed }} m/s</p>

    <!-- Message de chargement -->
    <p v-if="isLoading">Loading weather data...</p>

    <!-- Message d'erreur -->
    <p v-if="error" style="color: red;">Error: {{ error }}</p>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      weather: {
        city: '',
        temperature: '',
        description: '',
        humidity: '',
        wind_speed: ''
      },
      isLoading: true,  // Indique si les données sont en train de charger
      error: null       // Stocke un message d'erreur si quelque chose échoue
    };
  },
  created() {
    this.fetchWeather();
  },
  methods: {
    fetchWeather() {
      this.isLoading = true;  // Démarre le chargement
      this.error = null;      // Réinitialise l'erreur

      fetch('http://localhost:8000/api/weather/')
        .then(response => response.json())
        .then(data => {
          this.weather = data;  // Assigne les données météo reçues
          this.isLoading = false;  // Arrête le chargement
        })
        .catch(error => {
          console.error('Error fetching weather data:', error);
          this.error = 'Impossible de récupérer les données météo.';  // Affiche l'erreur
          this.isLoading = false;  // Arrête le chargement
        });
    }
  }
};
</script>

<style>
/* Ajoute ton style ici */
#app {
  text-align: center;
  padding: 20px;
}
h1 {
  color: #333;
}
p {
  font-size: 1.2em;
}
</style>
