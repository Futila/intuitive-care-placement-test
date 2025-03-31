# main.py

import os
from src.scraper import extract_pdf_links
from src.downloader import create_output_folder, download_pdfs
from src.zip_handler import zip_pdfs

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    print("🔍 Iniciando Web Scraper...")

    # Criar pasta de saída na raiz do projeto
    output_folder = create_output_folder(os.path.join(os.path.dirname(__file__), "output"))

    # Extrair links
    pdf_links = extract_pdf_links(url)
    if not pdf_links:
        print("❌ Nenhum PDF para baixar. Encerrando...")
        return

    # Fazer download dos PDFs
    pdf_paths = download_pdfs(pdf_links, output_folder)

    # Compactar PDFs em ZIP
    zip_path = zip_pdfs(pdf_paths, output_folder=output_folder)

    print(f"✅ Arquivo ZIP gerado em: {zip_path}")

if __name__ == "__main__":
    main()























# import os
# from src.web_scraper import extract_pdf_links
# from src.downloader import download_pdf
# from src.zip_handler import zip_files

# URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao"
# OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

# def main():
#     print("Iniciando Web Scraper...")

#     # 1. Extrair links
#     pdf_links = extract_pdf_links(URL)
#     print(f"Encontrados {len(pdf_links)} links de PDF.")

#     # 2. Criar a pasta 'output' no nível correto
#     os.makedirs(OUTPUT_DIR, exist_ok=True)

#     # 3. Baixar PDFs
#     for link in pdf_links:
#         download_pdf(link, OUTPUT_DIR)

#     # 4. Compactar os PDFs em ZIP
#     zip_path = os.path.join(OUTPUT_DIR, "arquivos.zip")
#     zip_files(OUTPUT_DIR, zip_path)

#     print(f"Download e compactação concluídos: {zip_path}")

# if __name__ == "__main__":
#     main()





















# import requests
# from bs4 import BeautifulSoup
# import zipfile
# import os

# # 1. Acessar o site
# url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # 2. Encontrar os links dos anexos
# pdf_links = [a['href'] for a in soup.find_all('a', href=True) if 'Anexo' in a.text]

# # 3. Criar a pasta output (se não existir)
# output_dir = "output"
# os.makedirs(output_dir, exist_ok=True)

# # 4. Baixar os PDFs
# pdf_paths = []
# for link in pdf_links:
#     pdf_url = link if link.startswith('http') else f"https://www.gov.br{link}"
#     pdf_name = pdf_url.split("/")[-1]
#     pdf_path = os.path.join(output_dir, pdf_name)
#     pdf_paths.append(pdf_path)

#     pdf_response = requests.get(pdf_url)
#     with open(pdf_path, 'wb') as f:
#         f.write(pdf_response.content)

# # 5. Compactar os PDFs na pasta output
# zip_path = os.path.join(output_dir, 'anexos.zip')
# with zipfile.ZipFile(zip_path, 'w') as zipf:
#     for pdf in pdf_paths:
#         zipf.write(pdf, os.path.basename(pdf))
#         os.remove(pdf)  # Remove os PDFs após compactar

# print(f"Arquivo zip gerado em: {zip_path}")





































# import requests
# from bs4 import BeautifulSoup
# import zipfile
# import os

# # 1. Acessar o site
# url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # 2. Encontrar os links dos anexos
# pdf_links = [a['href'] for a in soup.find_all('a', href=True) if 'Anexo' in a.text]

# # 3. Baixar os PDFs
# pdf_paths = []
# for link in pdf_links:
#     pdf_url = link if link.startswith('http') else f"https://www.gov.br{link}"
#     pdf_name = pdf_url.split("/")[-1]
#     pdf_paths.append(pdf_name)

#     pdf_response = requests.get(pdf_url)
#     with open(pdf_name, 'wb') as f:
#         f.write(pdf_response.content)

# # 4. Compactar os PDFs
# with zipfile.ZipFile('output/anexos.zip', 'w') as zipf:
#     for pdf in pdf_paths:
#         zipf.write(pdf)
#         os.remove(pdf)  # Remove os PDFs após compactar
