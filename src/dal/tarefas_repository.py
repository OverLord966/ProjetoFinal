import json
import os

# Caminho absoluto para a pasta src
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pasta data dentro de src
PASTA_DATA = os.path.join(BASE_DIR, "data")
CAMINHO_FICHEIRO = os.path.join(PASTA_DATA, "tarefas.json")

def garantir_estrutura():
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)

def carregar_tarefas():
    garantir_estrutura()
    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_tarefas(tarefas):
    garantir_estrutura()
    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)
