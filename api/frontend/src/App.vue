<!-- <script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style> -->


<!-- <template>
  <div>
    <input v-model="query" placeholder="Buscar Operadora" @keyup="buscar" />
    <ul>
      <li v-for="operadora in resultados" :key="operadora.id">
        {{ operadora.Razao_Social }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return { query: '', resultados: [] };
  },
  methods: {
    async buscar() {
      const res = await axios.get(`http://localhost:8000/search/?q=${this.query}`);
      this.resultados = res.data;
    },
  },
};
</script> -->


<template>
  <div class="container">
    <h1>Buscar Operadora</h1>
    <div class="search-container">
      <input
        v-model="query"
        placeholder="Digite o nome da operadora..."
        class="search-input"
      />
      <button @click="buscar" class="search-button">Buscar</button>
    </div>

    <table v-if="resultados.length" class="result-table">
      <thead>
        <tr>
          <th>Registro ANS</th>
          <th>Razão Social</th>
          <th>Nome Fantasia</th>
          <th>Cidade</th>
          <th>UF</th>
          <th>Telefone</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="operadora in resultados" :key="operadora.Registro_ANS">
          <td>{{ operadora.Registro_ANS }}</td>
          <td>{{ operadora.Razao_Social }}</td>
          <td>{{ operadora.Nome_Fantasia }}</td>
          <td>{{ operadora.Cidade }}</td>
          <td>{{ operadora.UF }}</td>
          <td>{{ operadora.Telefone }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>Nenhuma operadora encontrada.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      resultados: [],
    };
  },
  methods: {
    async buscar() {
      if (!this.query.trim()) return;
      try {
        const res = await axios.get(`http://localhost:8000/search/?q=${this.query}`);
        this.resultados = res.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Estilização geral */
.container {
  max-width: 100%;
  margin: 20px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

/* Título */
h1 {
  text-align: center;
  color: #333;
}

/* Estilização do input e botão */
.search-container {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.search-input {
  width: 60%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.search-button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}

/* Tabela de resultados */
.result-table {
  width: 100%;
  border-collapse: collapse;
  /* background: white; */
}

.result-table th,
.result-table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}

.result-table th {
  background-color: #007bff;
  color: white;
}

.result-table tbody tr:nth-child(even) {
  background-color: #000000;
}

.result-table tbody tr:nth-child(odd) {
  background-color: #000000;
}
</style>
