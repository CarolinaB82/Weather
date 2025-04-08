import axios from 'axios';

const API_URL = 'http://localhost:8000/api/weather/';  // L'URL de ton API Backend Django

// Crée une fonction pour récupérer les données météo
export const getWeather = async (city) => {
  try {
    const response = await axios.get(`${API_URL}?city=${city}`);  // Requête GET à l'API
    console.log(response.data);  // Affiche les données météo dans la console
    return response.data;  // Retourne les données météo
  } catch (error) {
    console.error('Erreur lors de la récupération des données météo:', error);
    throw error;  // Lève une erreur si la requête échoue
  }
};