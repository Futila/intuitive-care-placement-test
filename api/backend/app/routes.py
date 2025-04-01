from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Bem-vindo à API de Teste."}

    # Carregar CSV
df = pd.read_csv("Relatorio_cadop.csv", delimiter=";")

# print(df.to_string())

@router.get("/search/")
def buscar_operadora(q: str):
    resultados = df[df["Razao_Social"].str.contains(q, case=False, na=False)]
    return resultados.fillna("").to_dict(orient="records")  # Substitui NaN por strings vazias
