# src/downloader.py

import os
import requests

def create_output_folder(folder_name="output"):
    """Cria a pasta de saída (output) se não existir."""
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def download_pdfs(pdf_links, output_folder="output"):
    """Faz o download dos PDFs e retorna seus caminhos."""
    pdf_paths = []
    for link in pdf_links:
        # Garantir que o link está completo
        pdf_url = link if link.startswith('http') else f"https://www.gov.br{link}"
        pdf_name = pdf_url.split("/")[-1]
        pdf_path = os.path.join(output_folder, pdf_name)
        pdf_paths.append(pdf_path)

        print(f"📥 Baixando: {pdf_url}")

        try:
            pdf_response = requests.get(pdf_url)
            pdf_response.raise_for_status()
            with open(pdf_path, 'wb') as f:
                f.write(pdf_response.content)
        except requests.RequestException as e:
            print(f"❌ Erro ao baixar {pdf_url}: {e}")
    return pdf_paths
