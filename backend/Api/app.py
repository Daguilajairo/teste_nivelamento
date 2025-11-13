import os
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "operadoras_plano_saude", "Relatorio_cadop.csv")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
    print("📂 Lendo CSV:", csv_path)
    df = pd.read_csv(csv_path, encoding="utf-8", sep=";")
    print("✅ CSV carregado com sucesso! Linhas:", len(df))
except Exception as e:
    print(" Erro ao carregar CSV:", e)
    df = None


@app.get("/")
def root():
    return {"message": "API funcionando com sucesso"}

@app.get("/buscar")
def buscar_operadora(nome: str = Query(...)):
    nome = nome.strip()  
    ...

    

    """
    Busca operadoras de plano de saúde pelo nome no CSV.
    Exemplo: /buscar?nome=unimed
    """
    try:
        print(f" Buscando operadora com nome: {nome}")

        nome_lower = nome.lower()


        resultados = df[
        df["Razao_Social"].astype(str).str.lower().str.startswith(nome_lower, na=False)
]



        print(f" Linhas encontradas: {len(resultados)}")

        if resultados.empty:
            return {"mensagem": f"Nenhum resultado encontrado para '{nome}'."}

        
        colunas_principais = [
            "REGISTRO_OPERADORA", "CNPJ", "Razao_Social",
            "Modalidade", "Cidade", "UF",
            "Representante", "Cargo_Representante"
        ]
        resultados = resultados[colunas_principais]

        return resultados.head(10).to_dict(orient="records")

    except Exception as e:
        import traceback
        print(" ERRO AO BUSCAR:", traceback.format_exc())
        return {"erro": str(e)}
