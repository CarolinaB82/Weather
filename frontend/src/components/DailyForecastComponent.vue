<template>
    <div class="forecast-right">
      <h3>Prochains jours</h3>
      <ul>
        <li v-for="(day, index) in days" :key="index">
          {{ new Date(day.dt * 1000).toLocaleDateString() }} : 
          Min {{ day.main.temp_min }}°C / Max {{ day.main.temp_max }}°C - {{ day.weather[0].description }}
          <img :src="'https://openweathermap.org/img/wn/' + day.weather[0].icon + '@2x.png'" />
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      days: Array
    }
  };
  </script>
  