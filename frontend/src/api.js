import axios from 'axios';

const baseURL = 'https://teste-nivelamento-7tiv.onrender.com';

export async function buscarOperadoraAPI(nome) {
  const response = await axios.get(`${baseURL}/buscar`, { params: { nome } });
  return response.data;
}
