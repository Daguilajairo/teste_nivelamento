import axios from 'axios';

const baseURL = import.meta.env.VITE_API_URL;


export async function buscarOperadoraAPI(nome) {
  try {
    const response = await axios.get(`${baseURL}/buscar`, { params: { nome } });
    return response.data;
  } catch (error) {
    console.error("Erro na chamada da API:", error);
    return { erro: error.message };
  }
}

console.log("API URL:", import.meta.env.VITE_API_URL);
