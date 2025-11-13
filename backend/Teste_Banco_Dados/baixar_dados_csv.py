import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zipfile import ZipFile
from io import BytesIO


base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"

base_dir = os.path.dirname(os.path.dirname(__file__))

data_folder = os.path.join(base_dir, "data", "dados_cadastrais_csv")
os.makedirs(data_folder, exist_ok=True)



def get_zip_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar {url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
       
        if href.endswith("/"):
            new_url = url + href
            links += get_zip_links(new_url)
       
        elif href.endswith(".csv"):
            full_url = href if href.startswith("http") else url + href
            links.append(full_url)
    return links


zip_links = get_zip_links(base_url)

for zip_url in zip_links:
    file_name = zip_url.split("/")[-1]
    file_path = os.path.join(data_folder, file_name)

    response = requests.get(zip_url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"csv salvo: {file_name}")

    else:
        print(f"Erro ao baixar: {file_name}")
