<template>
  <div v-if="weatherData" :style="{
      backgroundImage: backgroundImage ? 'url(' + backgroundImage + ')' : 'none',
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      height: '100vh',
      backgroundAttachment: 'fixed',
      color: 'white',
      padding: '20px',
      boxSizing: 'border-box',
    }" class="weather-container">

    <div class="weather-content">
      <!-- 🌡️ Météo actuelle -->
      <CurrentWeatherComponent :weatherData="weatherData.current" :city="city" :searchCity="debouncedSearch" />

      <!-- Recherche dynamique de la ville -->
      <div class="search-bar">
        <input type="text" v-model="city" @input="debouncedSearch(city)" placeholder="Rechercher une ville" />
      </div>
<!-- Conteneur des prévisions (heures + jours) -->
<div class="forecast-container">
  <div class="forecast-left">
          <HourForecastComponent :hours="weatherData.hourly.slice(0, 5)" />
        </div>

        <!-- 📅 Prévision 3 prochains jours -->
        <div class="forecast-right">
          <DailyForecastComponent :days="weatherData.daily.slice(0, 3)" />
        </div>
  </div>
</div>
</div>
</template>

<script>
import '@/assets/weather.css';
import axios from 'axios';
import { debounce } from 'lodash';
import CurrentWeatherComponent from './CurrentWeatherComponent.vue';
import HourForecastComponent from './HourForecastComponent.vue';
import DailyForecastComponent from './DailyForecastComponent.vue';

export default {
  components: {
    CurrentWeatherComponent,
    HourForecastComponent,
    DailyForecastComponent,
  },
  data() {
    return {
      city: 'Paris', // Ville par défaut
      weatherData: null, // Données météo
      error: null, // Message d'erreur
      loading: false, // Indicateur du chargement des données
      backgroundImage: '', // URL de l'image de fond
    };
  },
  methods: {
    debouncedSearch: debounce(function(city) {
      this.getWeather(city);
    }, 500),
    
    async getWeather(city) {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get(`http://localhost:8000/api/weather/?city=${city}`);
        if (response.data) {
          this.weatherData = response.data;
          this.backgroundImage = response.data.backgroundImage;
        } else {
          this.error = 'Aucune donnée reçue de l\'API.';
        }
      } catch (error) {
        this.error = 'Erreur lors de la récupération des données météo : ' + error.message;
      } finally {
        this.loading = false;
      }
    },
  },

   
  watch: {
    city(newCity) {
      this.debouncedSearch(newCity);
    }
  },
  mounted() {
    this.getWeather(this.city);
  }
};
</script>
