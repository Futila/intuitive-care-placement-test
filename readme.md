## Testes

### 1️⃣ Teste de Web Scraping

- Acesse o site da **ANS** e baixe os anexos I e II.
- Compacte os arquivos em um único `.zip`.

### 2️⃣ Teste de Transformação de Dados

- Extraia a tabela "Rol de Procedimentos e Eventos em Saúde" do **Anexo I**.
- Salve os dados em formato `.csv` e compacte em um arquivo `.zip`.

### 3️⃣ Teste de Banco de Dados

- Baixe os arquivos de demonstrações contábeis e dados cadastrais da ANS.
- Estruture e importe os dados para um banco **MySQL** ou **PostgreSQL**.
- Desenvolva queries analíticas para analisar despesas de operadoras.

q1.sql: Cria as tabelas necessárias para armazenar os dados.

q2.sql: Importa os dados para o banco, garantindo o encoding correto.

q3.sql: Elabora queries analíticas para identificar as operadoras com maiores despesas.

### 4️⃣ Teste de API

- Desenvolva uma **API** em **Python** para buscar operadoras no CSV cadastral.
- Crie uma interface web com **Vue.js**.
- Forneça uma **coleção do Postman** para teste da API.

## Como Executar

Cada teste possui um README próprio dentro de sua respectiva pasta, contendo instruções detalhadas sobre instalação e execução.
