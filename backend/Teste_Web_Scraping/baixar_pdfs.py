import os
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
pdf_folder = os.path.join ("data", "pdfs")
os.makedirs(pdf_folder, exist_ok=True)

response = requests.get(url)

if response.status_code == 200:
    print("Página acessada com sucesso!\n")

    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".pdf") and ("Anexo_I" in href or "Anexo_II" in href):
            if href.startswith("/"):
                href = "https://www.gov.br" + href
            pdf_links.append(href)

    for pdf_url in pdf_links:
        file_name = pdf_url.split("/")[-1]
        file_path = os.path.join(pdf_folder, file_name)
        pdf_response = requests.get(pdf_url)
        with open(file_path, "wb") as f:
            f.write(pdf_response.content)
        print(f" PDF salvo: {file_name}")
else:
    print(" Erro ao acessar a página.")
