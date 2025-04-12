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
          await this.getCityImage(city);
        } else {
          this.error = 'Aucune donnée reçue de l\'API.';
        }
      } catch (error) {
        this.error = 'Erreur lors de la récupération des données météo : ' + error.message;
      } finally {
        this.loading = false;
      }
    },

    async getCityImage(city) {
      try {
        const response = await axios.get(`https://api.pexels.com/v1/search?query=${city}&per_page=1`, {
          headers: {
            Authorization: 'WEM3MGK7BEKIq0BWZvuJQyVlYm2VCndVYAkDnCBA6NBpI2bmfoPz0KS4',
          }
        });
        if (response.data && response.data.photos.length > 0) {
          this.backgroundImage = response.data.photos[0].src.original;
        } else {
          this.backgroundImage = "https://www.cerema.fr/sites/default/files/styles/uas_medium/public/media/images/2020/12/cityscape-3239939_-_copie.png?h=29a9f0d1&itok=0NtvLYbS";
          console.error('Aucune image trouvée pour cette ville.');
        }
      } catch (error) {
        console.error('Erreur lors de la récupération de l\'image Pexels :', error);
      }
    }
  },
  watch: {
    city(newCity) {
      this.debouncedSearch(newCity);
    }
  },
  mounted() {
    this.getWeather(this.city);
    this.getCityImage(this.city);
  }
};
</script>
