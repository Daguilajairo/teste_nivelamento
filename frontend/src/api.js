import axios from 'axios';

const baseURL = "http://127.0.0.1:8000";

export async function buscarOperadoraAPI(nome) {
  try {
    const response = await axios.get(`${baseURL}/buscar`, { params: { nome } });
    return response.data;
  } catch (error) {
    console.error("Erro na chamada da API:", error);
    return { erro: error.message };
  }
}
