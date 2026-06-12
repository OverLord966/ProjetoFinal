from dal.tarefas_repository import carregar_tarefas, guardar_tarefas
from datetime import datetime

def listar_tarefas():
    return carregar_tarefas()

def criar_tarefa(titulo, descricao, prioridade, prazo):
    tarefas = carregar_tarefas()

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo": prazo,
        "estado": "pendente",
        "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tarefas.append(nova_tarefa)
    guardar_tarefas(tarefas)

def editar_tarefa(id_tarefa, titulo, descricao, prioridade, prazo):
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["titulo"] = titulo
            tarefa["descricao"] = descricao
            tarefa["prioridade"] = prioridade
            tarefa["prazo"] = prazo
            break

    guardar_tarefas(tarefas)

def concluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["estado"] = "concluída"
            break

    guardar_tarefas(tarefas)

def apagar_tarefa(id_tarefa):
    tarefas = carregar_tarefas()

    # Remover tarefa
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]

    # Reorganizar IDs
    for i, tarefa in enumerate(tarefas, start=1):
        tarefa["id"] = i

    guardar_tarefas(tarefas)
def mover_tarefa(id_tarefa, nova_posicao):
    tarefas = carregar_tarefas()

    tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
    if not tarefa:
        return False

    tarefas.remove(tarefa)

    nova_posicao = max(1, min(nova_posicao, len(tarefas) + 1))
    tarefas.insert(nova_posicao - 1, tarefa)

    for i, t in enumerate(tarefas, start=1):
        t["id"] = i

    guardar_tarefas(tarefas)
    return True

