import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zipfile import ZipFile
from io import BytesIO


base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

base_dir = os.path.dirname(os.path.dirname(__file__))

data_folder = os.path.join(base_dir, "data", "repositorio_ultimos_2_anos")
os.makedirs(data_folder, exist_ok=True)


ano_atual = datetime.now().year
anos_validos = [ano_atual, ano_atual - 1]


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
       
        elif href.endswith(".zip") and any(str(ano) in href for ano in anos_validos):
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
        print(f"ZIP salvo: {file_name}")

        
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(data_folder)
            print(f"ZIP extraído: {file_name}")
    else:
        print(f"Erro ao baixar: {file_name}")
