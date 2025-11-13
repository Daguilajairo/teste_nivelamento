Teste de Nivelamento
TESTE 1 – Iniciado dia 11/11/2025 às 10h, finalizado às 17h

Criei uma pasta chamada teste de nivelamento.

Criei um arquivo chamado main.py, onde seria feito todo o código.

Criei um ambiente virtual usando o comando no terminal:

python -m venv venv


Essa pasta guarda o Python “isolado” e tudo o que for instalado com pip.

Ativei o ambiente virtual com:

venv\Scripts\activate


Criei uma pasta chamada pdfs para guardar os PDFs baixados do site indicado.

Instalei as bibliotecas necessárias:

requests → para baixar páginas e arquivos da internet.

beautifulsoup4 → para interpretar o HTML e buscar os links dos PDFs.

Desenvolvi o código para acessar a página, interpretar o HTML, filtrar apenas os PDFs Anexo I e II, e salvar os arquivos na pasta pdfs.

Coloquei prints para indicar quando os arquivos eram salvos corretamente e tratei possíveis erros de acesso à página.

Executei o script:

python main.py


Resultado: apenas os PDFs especificados foram baixados e salvos na pasta pdfs.

Script de Compactação

Criei um arquivo zipar_pdfs.py.

Importe funções para listar arquivos e criar arquivos .zip.

Listei os PDFs na pasta pdfs e adicionei ao ZIP.

Coloquei prints para informar que o ZIP foi criado com sucesso.

Executei o script:

python zipar_pdfs.py


Observação: Para melhor organização, criei dois arquivos (baixar_pdfs.py e zipar_pdfs.py) seguindo o conceito de responsabilidade única (SRP).

Resumo do Teste 1:

Criação da pasta do projeto e ativação do ambiente virtual.

Instalação das bibliotecas requests e beautifulsoup4.

baixar_pdfs.py: acessar site, interpretar HTML, filtrar PDFs, baixar arquivos.

Pasta pdfs criada manualmente.

zipar_pdfs.py: ler arquivos na pasta pdfs e criar ZIP.

Execução dos scripts para baixar e compactar PDFs.


TESTE 2 – Iniciado dia 12/11/2025 às 09h, finalizado às 17h

Instalei as bibliotecas:

tabula-py → para extrair planilhas de PDFs.

pandas → para manipular os dados extraídos.

Extraí todas as tabelas do PDF e juntei em um único DataFrame do pandas.

Salvei os dados extraídos em CSV e compacteio em ZIP conforme solicitado.

Criei Corrigir_abreviacoes.py para:

Ler o CSV original com pd.read_csv(csv_original, sep=';').

Corrigir células conforme solicitado.

Salvar o CSV corrigido separadamente.

Estrutura final das pastas até essa etapa:

PDF baixados e compactados.

CSV extraído e corrigido.



TESTE 3 – Banco de Dados – Iniciado dia 13/11/2025 às 08h, finalizado às 11:30h

Instalei MySQL 8 e testei o servidor.

Criei pasta teste banco de dados no VSCode.

Criei baixar_rep_2024_2025.py para baixar o repositório do site indicado via Python.

Criei uma pasta DATA para salvar os arquivos dos últimos 2 anos.

Usei uma função para baixar e extrair todos os arquivos ZIP encontrados.

Baixei os dados cadastrais via Python (baixar_dados_csv.py).

Criei conexão com banco teste_nivelamento no MySQL e testei a conexão.

Criei as tabelas e corrigi problemas na coluna registro_operacional.

Renomeei arquivos de trimestres para melhor identificação.

Compilei todos os CSVs em uma única tabela no MySQL.

Iniciei a análise conforme item 3.5:

Filtrei categorias “EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR”.

Somei despesas por operadora (REG_ANS) usando o saldo final.

Filtrei dados do último trimestre e gerei tabela top 10 do último trimestre.

Gere tabela top 10 do último ano móvel (01/01/2024 a 31/12/2024).



TESTE 4 – Frontend e API – Iniciado dia 13/11/2025 às 11:58, finalizado às 19:05

Instalei Vue.js na pasta teste_nivelamento com:

npm install -g @vue/cli


Desenvolvi o frontend (base do layout).

Criei a API em Python com FastAPI e rodei localmente com uvicorn.

Integrei o frontend com backend via axios.

Instalei Postman e criei uma coleção para demonstração dos resultados.

Criei pasta no backend para armazenar resultados da API.

Realizei testes para identificar possíveis erros.

Ajustei responsividade do layout para todos os dispositivos móveis.



Resumo Geral:

Teste 1: baixei e compactei PDFs.

Teste 2: extrai e corrigi CSVs de PDFs.

Teste 3: importei CSVs no MySQL, corrigi e analisei dados.

Teste 4: criei frontend em Vue.js, API FastAPI, integração e testes, layout responsivo.