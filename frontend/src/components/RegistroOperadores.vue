<template>
  <div class="card">
    <div class="container-card">
      <div class="title">
        <h1>Registro de Operadores</h1>
      </div>

      <div class="form">
        <input
          class="input"
          type="text"
          v-model="nome"
          placeholder="Buscar Operadora"
        />
        <button class="btn-search" @click="buscarOperadora">Buscar</button>
      </div>

      <div class="table-header">
        <p>Operadora</p>
        <p>CNPJ</p>
        <p>Modalidade</p>
      </div>

      <div class="table-body">
        <div v-for="item in resultados" :key="item.CNPJ" class="table-row">
          <p>{{ item.Razao_Social }}</p>
          <p>{{ item.CNPJ }}</p>
          <p>{{ item.Modalidade }}</p>
        </div>

        <p v-if="resultados.length === 0 && buscou">Nenhum resultado encontrado.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { buscarOperadoraAPI } from "../api.js";


export default {
  name: "CadastroOperadores",
  data() {
    return {
      nome: "",
      resultados: [],
      buscou: false,
      debounceTimer: null,
    };
  },
  watch: {
   
    nome(novoValor) {
      clearTimeout(this.debounceTimer);

      if (!novoValor.trim()) {
        this.resultados = [];
        this.buscou = false;
        return;
      }

      
      this.debounceTimer = setTimeout(async () => {
        try {
          const data = await buscarOperadoraAPI(novoValor);
          this.resultados = data;
          this.buscou = true;
        } catch (error) {
          console.error("Erro ao buscar operadora:", error);
          this.resultados = [];
          this.buscou = true;
        }
      }, 300); 
    },
  },
  methods: {
    async buscarOperadora() {
      if (!this.nome.trim()) return;

      try {
        const data = await buscarOperadoraAPI(this.nome);
        this.resultados = data;
        this.buscou = true;
      } catch (error) {
        console.error("Erro ao buscar operadora:", error);
        this.resultados = [];
        this.buscou = true;
      }
    },
  },
};
</script>

