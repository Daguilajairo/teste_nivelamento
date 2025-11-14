from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# Permite requisições do front local (Vite/Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "operadoras_plano_saude", "Relatorio_cadop.csv")

@app.get("/buscar")
def buscar_operadora(nome: str = Query(..., min_length=1)):
    try:
        # Lê o CSV com separador ponto e vírgula
        df = pd.read_csv(CSV_PATH, sep=';')

        # Limpa espaços e valores nulos na coluna Razao_Social
        df['Razao_Social'] = df['Razao_Social'].astype(str).str.strip().fillna('')

        # Filtra pelo início do nome (case insensitive)
        df_filtrado = df[df['Razao_Social'].str.lower().str.startswith(nome.lower())]

        # Seleciona apenas as colunas necessárias e renomeia para o front
        df_front = df_filtrado[['Razao_Social', 'CNPJ', 'Modalidade']].rename(
            columns={'Razao_Social': 'Operadora'}
        )

        # Retorna como lista de dicionários
        return df_front.to_dict(orient="records")

    except FileNotFoundError:
        return {"erro": "Arquivo CSV não encontrado"}
    except Exception as e:
        return {"erro": str(e)}
