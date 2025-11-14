import os
import pandas as pd
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "backend", "data", "operadoras_plano_saude", "Relatorio_cadop.csv")
df = None

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    df = pd.read_csv(csv_path, encoding="utf-8", sep=";")
except Exception as e:
    print(f"ERRO AO CARREGAR CSV: {e}")
    df = None

@app.get("/")
def root():
    return {"message": "API funcionando com sucesso"}

@app.get("/buscar")
def buscar_operadora(nome: str = Query(...)):
    global df
    if df is None:
        raise HTTPException(
            status_code=500,
            detail="Dados da operadora não carregados. CSV pode estar faltando."
        )

    nome = nome.strip()
    if not nome:
        return {"mensagem": "Informe um nome válido para busca."}

    try:
        nome_lower = nome.lower()
        resultados = df[df["Razao_Social"].astype(str).str.lower().str.startswith(nome_lower, na=False)]

        if resultados.empty:
            return {"mensagem": f"Nenhum resultado encontrado para '{nome}'."}

        colunas_principais = [
            "REGISTRO_OPERADORA", "CNPJ", "Razao_Social",
            "Modalidade", "Cidade", "UF",
            "Representante", "Cargo_Representante"
        ]
        resultados = resultados[colunas_principais]
        return resultados.head(10).to_dict(orient="records")

    except KeyError as ke:
        raise HTTPException(status_code=500, detail=f"Erro de coluna: {str(ke)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")
