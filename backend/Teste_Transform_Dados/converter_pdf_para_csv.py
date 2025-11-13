import os
import pandas as pd
import tabula

pdf_path = os.path.join("data","pdfs", "Anexo_I_Rol_2021RN_465.2021_RN647.2025.pdf")
csv_filename = os.path.join("data", "csv", "tabela_anexo1.csv")

print("extraindo tabelas do pdf!")
tabelas = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

df_final = pd.concat(tabelas, ignore_index=True)
df_final = df_final.fillna("")
df_final.to_csv(csv_filename, index=False, sep=";", encoding="utf-8-sig")

print("arquivo csv criado com sucesso")
