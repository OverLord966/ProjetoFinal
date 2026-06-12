from dal.tarefas_repository import carregar_tarefas, guardar_tarefas
from datetime import datetime

# A camada de serviço trata a lógica de negócio das tarefas.
# Ela carrega e salva os dados usando o repositório e aplica regras simples.

def listar_tarefas():
    """Retorna todas as tarefas armazenadas."""
    return carregar_tarefas()


def criar_tarefa(titulo, descricao, prioridade, prazo):
    """Cria uma nova tarefa e grava no repositório."""
    tarefas = carregar_tarefas()

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo": prazo,
        "estado": "pendente",
        # Armazena a data e hora atual no formato AAAA-MM-DD HH:MM
        "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tarefas.append(nova_tarefa)
    guardar_tarefas(tarefas)


def editar_tarefa(id_tarefa, titulo, descricao, prioridade, prazo):
    """Edita os dados de uma tarefa existente."""
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
    """Marca uma tarefa como concluída."""
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["estado"] = "concluída"
            break

    guardar_tarefas(tarefas)


def apagar_tarefa(id_tarefa):
    """Remove uma tarefa e reorganiza os IDs restantes."""
    tarefas = carregar_tarefas()

    # Remove a tarefa com o ID informado.
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]

    # Reatribui IDs sequenciais para manter a ordem consistente.
    for i, tarefa in enumerate(tarefas, start=1):
        tarefa["id"] = i

    guardar_tarefas(tarefas)


def mover_tarefa(id_tarefa, nova_posicao):
    """Move uma tarefa para uma nova posição na lista."""
    tarefas = carregar_tarefas()

    tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
    if not tarefa:
        return False

    # Remove a tarefa da posição atual.
    tarefas.remove(tarefa)

    # Limita a nova posição ao intervalo válido da lista.
    nova_posicao = max(1, min(nova_posicao, len(tarefas) + 1))
    tarefas.insert(nova_posicao - 1, tarefa)

    # Atualiza os IDs após a mudança de ordem.
    for i, t in enumerate(tarefas, start=1):
        t["id"] = i

    guardar_tarefas(tarefas)
    return True

