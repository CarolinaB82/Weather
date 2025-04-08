<template>
  <div id="app">
    <!-- Inclure le composant weathercomponent.vue ici -->
    <WeatherComponent />
  </div>
</template>

<script>
// Importer le composant weathercomponent.vue
import WeatherComponent from './components/WeatherComponent.vue';

export default {
  name: 'App',
  components: {
    WeatherComponent  // Déclarer le composant pour pouvoir l'utiliser
  }
};
</script>

<style>
#app {
  text-align: center;
  padding: 20px;
}
</style>
