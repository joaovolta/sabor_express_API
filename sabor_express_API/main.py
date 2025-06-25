# pip install fastapi
# pip install uvicorn
# uvicorn "nomedoarquivo":app --reload

from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello():
    """
    Endpoint que exibe uma famosa frase do mundo da programação 
    """
    return {"Hello":"World"}


@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint que exibe o cardapio dos restaurantes 
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {"Dados": dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item["Company"] == restaurante:
                dados_restaurante.append({
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"] 
                })  
        return {"Restaurante": restaurante, "Cardapio": dados_restaurante}
    else:
        return {"Erro": response.status_code}