# Web Scraping - Extração de PDFs

Este projeto realiza o web scraping de uma página da ANS (Agência Nacional de Saúde Suplementar) para acessar e baixar arquivos PDF relacionados à atualização do rol de procedimentos.

## Funcionalidades

- Acessa a página da ANS para encontrar links para os arquivos PDF.
- Baixa os arquivos PDF para uma pasta local.
- Compacta os arquivos PDF em um arquivo ZIP.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Requests** (para requisições HTTP)
- **BeautifulSoup4** (para parsing do HTML)
- **Zipfile** (para compactação de arquivos)
- **Pytest** (para testes automatizados)

## Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Futila/intuitive-care-placement-test.git
   cd intuitive-care-placement-test.git
   cd scraping
   ```
2. Criar um Ambiente Virtual (Opcional, mas Recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instalar as Dependências
   ```bash
   pip install -r requirements.txt
   ```
4. Executar o Scraper
   ```bash
   python main.py
   ```

## Testes

Para rodar os testes automatizados, use o comando:

```bash
pytest tests/
```

Isso executará todos os testes dentro da pasta tests e verificará se as funções do scraping estão funcionando corretamente.
