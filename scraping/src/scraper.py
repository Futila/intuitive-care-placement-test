# src/scraper.py

import requests
from bs4 import BeautifulSoup

def extract_pdf_links(url):
    """Acessa a URL e extrai os links dos anexos."""
    response = requests.get(url)
    response.raise_for_status()  # Lança um erro se a requisição falhar

    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [a['href'] for a in soup.find_all('a', href=True) if 'Anexo' in a.text]

    if not pdf_links:
        print("❌ Nenhum link de PDF encontrado.")

    return pdf_links
