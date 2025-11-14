from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
      allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "operadoras_plano_saude", "Relatorio_cadop.csv")

@app.get("/buscar")
def buscar_operadora(nome: str = Query(..., min_length=1)):
    try:
       
        df = pd.read_csv(CSV_PATH, sep=';')

        
        df.columns = df.columns.str.strip()

        
        df['Razao_Social'] = df['Razao_Social'].astype(str).str.strip().fillna('')

        
        df_filtrado = df[df['Razao_Social'].str.lower().str.startswith(nome.lower())]

        
        df_front = df_filtrado[['Razao_Social', 'CNPJ', 'Modalidade']].rename(
            columns={'Razao_Social': 'Operadora'}
        )

       
        return df_front.to_dict(orient="records")

    except FileNotFoundError:
        return {"erro": "Arquivo CSV não encontrado"}
    except KeyError as ke:
        return {"erro": f"Coluna não encontrada no CSV: {str(ke)}"}
    except Exception as e:
        return {"erro": str(e)}
