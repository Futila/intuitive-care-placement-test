import os
import pandas as pd
import zipfile
import pdfplumber

def extrair_dados_pdf(pdf_path):
    '''
    Função para extrair as tabelas do PDF
    '''
    try:
        tabelas = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tb = page.extract_tables()
                if tb:
                    tabelas.extend(tb)
        
        if not tabelas:
            raise ValueError("Nenhuma tabela encontrada")
            
        # Combine todas as tabelas
        df = pd.concat([pd.DataFrame(tabela[1:], columns=tabela[0]) 
                      for tabela in tabelas if tabela])
        
        # Renomear colunas
        df.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatoria"}, inplace=True)
        
        return df
    except Exception as e:
        print(f"Erro pdfplumber: {str(e)}")
        return None


def main():
    pdf_path = "Anexo I.pdf"
    if not pdf_path:
        print("Nenhum arquivo selecionado!")
        return
    
    print(f"Processando... {pdf_path}")
    df = extrair_dados_pdf(pdf_path)
    
    if df is not None:
        nome = "Fernando_Futila"
        arquivo_csv = "procedimentos_saude.csv"
        arquivo_zip = f"Teste_{nome}.zip"  # Substitua com seu nome
        
        try:
            df.to_csv(arquivo_csv, index=False, encoding='utf-8-sig')
            print(f"CSV salvo: {arquivo_csv}")
            
            with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
                zipf.write(arquivo_csv)
            print(f"Arquivo ZIP criado: {arquivo_zip}")
            
            os.remove(arquivo_csv)
            print("Processo concluído com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar resultados: {str(e)}")
    else:
        print("Falha na extração dos dados.")

if __name__ == "__main__":
    main()