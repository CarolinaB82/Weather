<template>
    <div>
      <h1>Météo actuelle</h1>
      <!-- Affichage des données météo -->
      <div v-if="weather">
        <p>Température : {{ weather.temperature }}°C</p>
        <p>Description : {{ weather.description }}</p>
      </div>
    
      <!-- Affichage d'un message de chargement pendant que les données sont récupérées -->
      <p v-else>Chargement...</p>
    
      <!-- Affichage d'une erreur en cas de problème -->
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        weather: null,  // Données météo
        error: null,    // Erreur éventuelle
      };
    },
    created() {
      this.fetchWeather();  // Charge les données météo lorsqu'on accède au composant
    },
    methods: {
      fetchWeather() {
        fetch('http://127.0.0.1:8000/api/weather/')  // Appel de l'API backend
          .then(response => response.json())
          .then(data => {
            this.weather = data;  // Enregistre les données reçues dans l'état
          })
          .catch(err => {
            this.error = 'Impossible de récupérer les données météo.';  // Gère l'erreur
          });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Ajoute des styles si nécessaire */
  </style>
  