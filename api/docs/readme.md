# 📌 Projeto: Buscador de Operadoras de Saúde

Este projeto consiste em uma API desenvolvida com **FastAPI** (Python) para buscar operadoras de saúde a partir de um arquivo CSV e um frontend em **Vue.js** para exibir os resultados da busca de maneira interativa.

---

## 🖥️ Backend (FastAPI)

### 📌 Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- Pandas

### 🔧 Instalação e Execução

1. **Clonar o repositório:**

   ```bash
    git clone https://github.com/Futila/intuitive-care-placement-test.git
    cd intuitive-care-placement-test.git
    cd api/backend
    cd app
   ```

2. **Criar e ativar um ambiente virtual (opcional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   venv\Scripts\activate  # No Windows
   ```

3. **Instalar dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Executar a API:**

   ```bash
   python main.py
   ```

5. **Acessar a API:**
   - Documentação interativa: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

### 🚀 Endpoints da API

| Método | Rota               | Descrição                                 |
| ------ | ------------------ | ----------------------------------------- |
| GET    | `/search/?q=texto` | Busca operadoras pelo nome (razão social) |

#### Exemplo de Requisição

```bash
curl -X 'GET' 'http://127.0.0.1:8000/search/?q=unimed' -H 'accept: application/json'
```

#### Exemplo de Resposta

```json
[
  {
    "Registro_ANS": 386596,
    "CNPJ": 366982000130,
    "Razao_Social": "CENTRAL REGIONAL DAS COOPERATIVAS MÉDICAS - UNIMED CERRADO",
    "Nome_Fantasia": "UNIMED CERRADO",
    "Modalidade": "Cooperativa Médica",
    "Cidade": "Goiânia",
    "UF": "GO",
    "Telefone": 92883684
  }
]
```

### 📜 Testes no Postman

Uma coleção de testes foi criada para facilitar a demonstração dos resultados da API. Acesse a pasta backend/postman e importe a coleção no Postman para testar as requisições de forma prática.

## 🎨 Frontend (Vue.js)

### 📌 Requisitos

- Node.js 16+
- Vue.js 3
- Axios

### 🔧 Instalação e Execução

1. **Acessar a pasta do frontend:**
   ```bash
   cd ../frontend
   ```
2. **Instalar dependências:**
   ```bash
   npm install
   ```
3. **Executar o frontend:**

   ```bash
   npm run dev
   ```

4. **Acessar no navegador:**
   - [http://localhost:5173](http://localhost:5173)

### 🎭 Funcionalidade

- O usuário digita um termo de busca e recebe uma lista de operadoras filtradas pela razão social.
- Exibe os resultados em uma **tabela estilizada**.

## 🚀 Tecnologias Utilizadas

- **Backend:** Python, FastAPI, Pandas
- **Frontend:** Vue.js, Axios
- **Banco de Dados:** Arquivo CSV
- **Servidor de Desenvolvimento:** Uvicorn
