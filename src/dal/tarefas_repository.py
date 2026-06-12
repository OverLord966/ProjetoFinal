import json
import os

# Caminho para a pasta de dados e o ficheiro JSON usado para armazenar tarefas.
PASTA_DATA = os.path.join("src", "data")
CAMINHO_FICHEIRO = os.path.join(PASTA_DATA, "tarefas.json")

def garantir_estrutura():
    """Garante que a pasta e o ficheiro JSON existem antes de ler ou escrever."""
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)

    if not os.path.exists(CAMINHO_FICHEIRO):
        with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as f:
            # Cria um ficheiro vazio com uma lista JSON vazia.
            json.dump([], f, indent=4, ensure_ascii=False)

def carregar_tarefas():
    """Carrega as tarefas do ficheiro JSON. Retorna lista vazia se o ficheiro estiver inválido."""
    garantir_estrutura()

    with open(CAMINHO_FICHEIRO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Se o ficheiro estiver corrompido ou vazio, retorna uma lista vazia.
            return []

def guardar_tarefas(tarefas):
    """Guarda a lista de tarefas no ficheiro JSON."""
    garantir_estrutura()

    with open(CAMINHO_FICHEIRO, "w", encoding="utf-8") as f:
        # Escreve o JSON com identação para facilitar a leitura manual.
        json.dump(tarefas, f, indent=4, ensure_ascii=False)
