import os
import zipfile

csv_filename = os.path.join("data", "csv", "tabela_anexo1.csv")
zip_folder = "zips"
os.makedirs(zip_folder, exist_ok=True)
zip_filename = os.path.join(zip_folder, "Teste_jairo.zip")

with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(csv_filename, arcname=os.path.basename(csv_filename))

print("arquivo zip criado com sucesso")
