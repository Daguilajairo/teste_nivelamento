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
        <p v-if="loading">Carregando...</p>
        <p v-else-if="erroApi" class="error-message">{{ erroApi }}</p>

        <template v-else>
          <div
            v-for="(item, index) in resultados"
            :key="item.CNPJ || index"
            class="table-row"
          >
            <p>{{ item.Operadora }}</p>
            <p>{{ item.CNPJ }}</p>
            <p>{{ item.Modalidade }}</p>
          </div>

          <p v-if="resultados.length === 0 && buscou">Nenhum resultado encontrado.</p>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { buscarOperadoraAPI } from "../api.js";

export default {
  name: "RegistroOperadores",
  data() {
    return {
      nome: "",
      resultados: [],
      buscou: false,
      debounceTimer: null,
      loading: false,
      erroApi: null,
    };
  },
  watch: {
    nome(novoValor) {
      clearTimeout(this.debounceTimer);
      this.erroApi = null;

      if (!novoValor.trim()) {
        this.resultados = [];
        this.buscou = false;
        return;
      }

      this.loading = true;

      this.debounceTimer = setTimeout(async () => {
        await this.performSearch(novoValor);
        this.loading = false;
      }, 300);
    },
  },
  methods: {
    async performSearch(searchName) {
      this.buscou = true;
      try {
        const data = await buscarOperadoraAPI(searchName);

        if (Array.isArray(data)) {
          // Recebe diretamente do backend
          this.resultados = data;
          this.erroApi = null;
          
        } else if (data && data.mensagem) {
          this.resultados = [];
          this.erroApi = null;
        } else if (data && data.erro) {
          this.resultados = [];
          this.erroApi = `Erro da API: ${data.erro}`;
          console.error("Erro da API:", data.erro);
        } else {
          this.resultados = [];
          this.erroApi = null;
        }
      } catch (error) {
        console.error("Erro geral ao buscar operadora:", error);
        this.resultados = [];
        this.erroApi = "Falha de comunicação com o servidor. Verifique a URL.";
      }
    },
    async buscarOperadora() {
      if (!this.nome.trim()) return;
      this.loading = true;
      clearTimeout(this.debounceTimer);
      await this.performSearch(this.nome);
      this.loading = false;
    },
  },
};
</script>
