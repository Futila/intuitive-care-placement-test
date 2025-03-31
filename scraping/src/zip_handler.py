# src/zip_handler.py

import os
import zipfile

def zip_pdfs(pdf_paths, zip_name="anexos.zip", output_folder="output"):
    """Compacta os PDFs baixados em um arquivo .zip."""
    zip_path = os.path.join(output_folder, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for pdf in pdf_paths:
            zipf.write(pdf, os.path.basename(pdf))
            os.remove(pdf)  # Remove os PDFs após compactar
    return zip_path
