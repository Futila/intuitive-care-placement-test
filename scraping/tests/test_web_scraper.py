import pytest
import os
from src.web_scrapper import extract_pdf_links, create_output_folder, download_pdfs, zip_pdfs

# Testando a extração dos links
def test_extract_pdf_links():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    links = extract_pdf_links(url)

    print("Links encontrados:", links)

    assert len(links) > 0  # Deve haver ao menos um link encontrado
    assert all(link.endswith(('.pdf', '.xlsx')) for link in links)  # Todos os links devem ser PDFs

# Testando a criação do diretório
def test_create_output_folder():
    folder = create_output_folder()
    assert os.path.exists(folder)  # A pasta deve existir
    assert folder == "output"

# Testando o download dos PDFs (com link simulado)
@pytest.mark.skip(reason="Evita downloads reais durante os testes")
def test_download_pdfs():
    links = ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"]
    output_folder = "output"
    pdf_paths = download_pdfs(links, output_folder)
    assert len(pdf_paths) == 1
    assert pdf_paths[0].endswith(".pdf")
    assert os.path.isfile(pdf_paths[0])

# Testando a compactação dos PDFs
def test_zip_pdfs():
    os.makedirs("output", exist_ok=True)
    pdf_path = "output/test.pdf"
    with open(pdf_path, "wb") as f:
        f.write(b"Teste PDF")
    
    zip_path = zip_pdfs([pdf_path])
    assert os.path.isfile(zip_path)
    assert zip_path.endswith(".zip")
