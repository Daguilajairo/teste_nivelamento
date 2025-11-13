import os
import pandas as pd
import re

csv_original = os.path.join("data", "csv", "tabela_anexo1.csv")
csv_corrigido = os.path.join("data", "csv", "tabela_anexo1_corrigida.csv")


df = pd.read_csv(csv_original, sep=";")


substituicoes = {
    r"\bOD\b": "Seg.Odontológica",
    r"\bAMB\b": "Seg.Ambulatorial"
}

for padrao, novo in substituicoes.items():
    df = df.replace(to_replace=padrao, value=novo, regex=True)

df.to_csv(csv_corrigido, index=False, sep=";", encoding="utf-8-sig")
print("Novo arquivo corrigido e salvo .")
