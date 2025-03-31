import unittest
import os
import requests
from main import extract_pdf_links, create_output_folder, download_pdfs, zip_pdfs

class TestWebScraping(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente antes dos testes."""
        self.url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
        self.output_dir = "output"
    
    def test_extract_pdf_links(self):
        """Testa a extração de links de PDF."""
        response = requests.get(self.url)
        pdf_links = extract_pdf_links(response.text)
        
        self.assertIsInstance(pdf_links, list)  # Deve retornar uma lista
        self.assertGreater(len(pdf_links), 0)   # Deve conter ao menos um link
        for link in pdf_links:
            self.assertTrue(link.startswith("http"))  # Link válido

    def test_create_output_folder(self):
        """Verifica se a pasta output é criada."""
        create_output_folder(self.output_dir)
        self.assertTrue(os.path.exists(self.output_dir))  # Pasta deve existir

    def test_download_pdfs(self):
        """Valida se o download de PDFs ocorre corretamente."""
        pdf_links = ["https://www.exemplo.com/test.pdf"]
        pdf_paths = download_pdfs(pdf_links, self.output_dir)
        
        self.assertEqual(len(pdf_paths), len(pdf_links))  # Todos os PDFs devem ser baixados
        for pdf in pdf_paths:
            self.assertTrue(os.path.exists(pdf))  # Arquivo PDF deve existir

    def test_zip_pdfs(self):
        """Garante que o arquivo zip é gerado."""
        pdf_paths = [os.path.join(self.output_dir, "test.pdf")]
        zip_path = zip_pdfs(pdf_paths, self.output_dir)
        
        self.assertTrue(os.path.exists(zip_path))  # ZIP deve ser criado

    def tearDown(self):
        """Limpa os arquivos gerados após os testes."""
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

if __name__ == '__main__':
    unittest.main()
