import requests 
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)

if response.status_code == 200:
    # Recebe todos os dados requisitados da api em formato JSON
    dados_json = response.json()
    # print(dados_json) # Exibe todos os dados requisitados da api
    dados_restaurante = {}
    for item in dados_json:
        # Recebe o nome do restaurante acessando a chave do dicionario "Company"
        nome_do_restaurante = item["Company"]
        # Caso o nome nao esteja no dicionario dados_restaurante 
        if nome_do_restaurante not in dados_restaurante:
            # Cria uma lista com para um nome especifico de restaurante
            dados_restaurante[nome_do_restaurante] = []

        # Com a lista criada adicionamos um dicionario com as infomacoes necessarias para o restaurante com nome especifico
        dados_restaurante[nome_do_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"] 
        })  

else:
    print(f"Ocorreu um erro {response.status_code}")

# Printa 
# print(dados_restaurante["McDonald’s"]) 

# Criacao de arquivos json para cada restaurante da API
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f"{nome_do_restaurante}.json" # Cria um nome para o arquivo conforme o nome do restaurante
    # Abre um arquivo com a funco "w", ou seja, write
    with open(nome_do_arquivo, "w") as arquivo_restaurante:
        # json.dump cria os arquivos, com (dados que vao ser exibidos, nome do arquivo, personalizacao)
        json.dump(dados, arquivo_restaurante, indent=4)