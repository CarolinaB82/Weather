<template>
    <div class="current-weather">
      <h2>Météo actuelle pour {{ city }}</h2>
      <p><strong>Température :</strong> {{ weatherData.temperature }} °C</p>
      <p><strong>Description :</strong> {{ weatherData.description }}</p>
      <p><strong>Humidité :</strong> {{ weatherData.humidity }} %</p>
      <p><strong>Vent :</strong> {{ weatherData.wind_speed }} m/s</p>
      <img :src="'https://openweathermap.org/img/wn/' + weatherData.icon + '@2x.png'" alt="icone météo" />
    </div>
  </template>
  
  <script>
  export default {
    props: {
      weatherData: Object,
      city: String,
      searchCity: Function
    },
  };
  </script>
  