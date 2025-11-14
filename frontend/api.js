
import axios from "axios";

const API_URL = "https://teste-nivelamento-7tiv.onrender.com"; 

export async function buscarOperadoraAPI(nome) {
  if (!nome) return [];
  const response = await axios.get(`${API_URL}/buscar`, { params: { nome } });
  return response.data;
}
