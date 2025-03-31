import requests
from bs4 import BeautifulSoup
import zipfile
import os

def extract_pdf_links(url):
    """Acessa a URL e extrai os links dos anexos."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [a['href'] for a in soup.find_all('a', href=True) if 'Anexo' in a.text]
    return pdf_links

def create_output_folder(folder_name="output"):
    """Cria a pasta de saída (output) se não existir."""
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def download_pdfs(pdf_links, output_folder="output"):
    """Faz o download dos PDFs e retorna seus caminhos."""
    pdf_paths = []
    for link in pdf_links:
        pdf_url = link if link.startswith('http') else f"https://www.gov.br{link}"
        pdf_name = pdf_url.split("/")[-1]
        pdf_path = os.path.join(output_folder, pdf_name)
        pdf_paths.append(pdf_path)

        pdf_response = requests.get(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(pdf_response.content)
    return pdf_paths

def zip_pdfs(pdf_paths, zip_name="anexos.zip", output_folder="output"):
    """Compacta os PDFs baixados em um arquivo .zip."""
    zip_path = os.path.join(output_folder, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for pdf in pdf_paths:
            zipf.write(pdf, os.path.basename(pdf))
            os.remove(pdf)  # Remove os PDFs após compactar
    return zip_path

if __name__ == "__main__":
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    pdf_links = extract_pdf_links(url)
    output_folder = create_output_folder()
    pdf_paths = download_pdfs(pdf_links, output_folder)
    zip_path = zip_pdfs(pdf_paths, output_folder=output_folder)

    print(f"Arquivo zip gerado em: {zip_path}")
