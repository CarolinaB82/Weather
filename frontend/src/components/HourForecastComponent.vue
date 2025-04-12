<template>
    <div class="forecast-left">
      <h3>Prochaines heures</h3>
      <ul>
        <li v-for="(hour, index) in hours" :key="index">
          {{ new Date(hour.dt * 1000).toLocaleTimeString() }} - {{ hour.main.temp }}°C - {{ hour.weather[0].description }}
          <img :src="'https://openweathermap.org/img/wn/' + hour.weather[0].icon + '@2x.png'" />
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      hours: Array
    }
  };
  </script>
  