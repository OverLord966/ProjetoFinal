from datetime import datetime, timedelta

from dal.tarefas_repository import guardar_tarefas, carregar_tarefas

from bll.tarefas_service import (
    listar_tarefas,
    criar_tarefa,
    editar_tarefa,
    concluir_tarefa,
    apagar_tarefa,
    mover_tarefa
)

# ============================================================
# Funções de validação
# ============================================================

def pedir_texto(mensagem):
    """Lê um texto não vazio do utilizador."""
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("❌ Este campo não pode estar vazio.")


def pedir_prioridade():
    """Lê e valida a prioridade da tarefa."""
    prioridades_validas = ["baixa", "média", "alta"]

    while True:
        prioridade = input("Prioridade (baixa/média/alta): ").lower().strip()
        if prioridade in prioridades_validas:
            return prioridade
        print("❌ Prioridade inválida! As opções são: baixa, média ou alta.")


def pedir_data():
    """Lê uma data válida e futura para o prazo da tarefa."""
    while True:
        data_str = input("Prazo (AAAA-MM-DD): ").strip()

        try:
            data = datetime.strptime(data_str, "%Y-%m-%d").date()
            hoje = datetime.now().date()
            limite_max = hoje + timedelta(days=365 * 5)

            if data < hoje:
                print("❌ A data não pode ser anterior ao dia de hoje.")
                continue

            if data > limite_max:
                print("❌ A data é demasiado distante. Máximo permitido: 5 anos.")
                continue

            return data_str

        except ValueError:
            print("❌ Data inválida! Usa o formato AAAA-MM-DD.")


def pedir_id_tarefa():
    """Lê um ID de tarefa existente a partir do utilizador."""
    tarefas = listar_tarefas()

    while True:
        try:
            id_tarefa = int(input("ID da tarefa: "))
        except ValueError:
            print("❌ O ID deve ser um número inteiro.")
            continue

        if any(t["id"] == id_tarefa for t in tarefas):
            return id_tarefa

        print("❌ Não existe nenhuma tarefa com esse ID.")


# ============================================================
# Menu principal
# ============================================================

def mostrar_menu():
    print("\n=== Gestão de Tarefas ===")
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Editar tarefa")
    print("4. Marcar como concluída")
    print("5. Apagar tarefa")
    print("6. Mover tarefa")
    print("7. Guardar tarefas")
    print("8. Carregar tarefas")
    print("0. Sair")


# ============================================================
# Opções do menu
# ============================================================

def opcao_criar():
    titulo = pedir_texto("Título: ")
    descricao = pedir_texto("Descrição: ")
    prioridade = pedir_prioridade()
    prazo = pedir_data()

    criar_tarefa(titulo, descricao, prioridade, prazo)
    print("\n✔ Tarefa criada com sucesso!\n")


def opcao_listar():
    tarefas = listar_tarefas()

    if not tarefas:
        print("\nNão existem tarefas registadas.\n")
        return

    print("\n========== LISTA DE TAREFAS ==========\n")

    for t in tarefas:
        print(f"ID:          {t['id']}")
        print(f"Título:      {t['titulo']}")
        print(f"Descrição:   {t['descricao']}")
        print(f"Prioridade:  {t['prioridade']}")
        print(f"Estado:      {t['estado']}")
        print(f"Prazo:       {t['prazo']}")
        print(f"Criado em:   {t['criado_em']}")
        print("-" * 40)

    print()


def opcao_editar():
    id_tarefa = pedir_id_tarefa()
    opcao = submenu_editar()

    tarefas = listar_tarefas()
    tarefa = next(t for t in tarefas if t["id"] == id_tarefa)

    if opcao == "1":
        novo_titulo = pedir_texto("Novo título: ")
        editar_tarefa(id_tarefa, novo_titulo, tarefa["descricao"], tarefa["prioridade"], tarefa["prazo"])

    elif opcao == "2":
        nova_desc = pedir_texto("Nova descrição: ")
        editar_tarefa(id_tarefa, tarefa["titulo"], nova_desc, tarefa["prioridade"], tarefa["prazo"])

    elif opcao == "3":
        nova_prioridade = pedir_prioridade()
        editar_tarefa(id_tarefa, tarefa["titulo"], tarefa["descricao"], nova_prioridade, tarefa["prazo"])

    elif opcao == "4":
        opc_data = submenu_editar_data()

        ano, mes, dia = tarefa["prazo"].split("-")

        if opc_data == "1":
            novo_dia = input("Novo dia (1-31): ").strip().zfill(2)

            if not validar_data(ano, mes, novo_dia):
                print("❌ Dia inválido para esse mês.")
                return

            if not data_nao_passada(ano, mes, novo_dia):
                print("❌ A nova data não pode ser anterior ao dia de hoje.")
                return

            novo_prazo = f"{ano}-{mes}-{novo_dia}"

        elif opc_data == "2":
            novo_mes = input("Novo mês (1-12): ").strip().zfill(2)

            if not validar_data(ano, novo_mes, dia):
                print("❌ Mês inválido ou dia não existe nesse mês.")
                return

            if not data_nao_passada(ano, novo_mes, dia):
                print("❌ A nova data não pode ser anterior ao dia de hoje.")
                return

            novo_prazo = f"{ano}-{novo_mes}-{dia}"

        elif opc_data == "3":
            novo_ano = input("Novo ano (ex: 2026): ").strip()

            if not validar_data(novo_ano, mes, dia):
                print("❌ Ano inválido ou data impossível.")
                return

            if not data_nao_passada(novo_ano, mes, dia):
                print("❌ A nova data não pode ser anterior ao dia de hoje.")
                return

            novo_prazo = f"{novo_ano}-{mes}-{dia}"

        elif opc_data == "4":
            novo_prazo = pedir_data()

        else:
            print("\nOperação cancelada.\n")
            return

        editar_tarefa(id_tarefa, tarefa["titulo"], tarefa["descricao"], tarefa["prioridade"], novo_prazo)

    else:
        print("\nOperação cancelada.\n")
        return

    print("\n✔ Tarefa editada com sucesso!\n")


# ============================================================
# Validações de data
# ============================================================

def validar_data(ano, mes, dia):
    try:
        datetime(int(ano), int(mes), int(dia))
        return True
    except ValueError:
        return False


def data_nao_passada(ano, mes, dia):
    try:
        nova_data = datetime(int(ano), int(mes), int(dia)).date()
        return nova_data >= datetime.now().date()
    except ValueError:
        return False


# ============================================================
# Submenus
# ============================================================

def submenu_editar():
    print("\n--- Editar Tarefa ---")
    print("1. Título")
    print("2. Descrição")
    print("3. Prioridade")
    print("4. Prazo (alterar apenas o dia)")
    print("0. Cancelar")
    return input("Escolha o campo a editar: ")


def submenu_editar_data():
    print("\n--- Editar Data ---")
    print("1. Alterar apenas o dia")
    print("2. Alterar apenas o mês")
    print("3. Alterar apenas o ano")
    print("4. Alterar a data completa")
    print("0. Cancelar")
    return input("Escolha uma opção: ")


# ============================================================
# Outras operações
# ============================================================

def opcao_concluir():
    id_tarefa = pedir_id_tarefa()
    concluir_tarefa(id_tarefa)
    print("\n✔ Tarefa concluída com sucesso!\n")


def opcao_apagar():
    id_tarefa = pedir_id_tarefa()
    apagar_tarefa(id_tarefa)
    print("\n✔ Tarefa apagada com sucesso!\n")


def opcao_mover():
    id_tarefa = pedir_id_tarefa()
    nova_pos = int(input("Nova posição na lista: "))

    if mover_tarefa(id_tarefa, nova_pos):
        print("\n✔ Tarefa movida com sucesso!\n")
    else:
        print("\n❌ Erro ao mover tarefa.\n")


# ============================================================
# Guardar e carregar tarefas
# ============================================================

def opcao_guardar():
    tarefas = listar_tarefas()   # usa as tarefas atuais
    guardar_tarefas(tarefas)
    print("\n✔ Tarefas guardadas\n")


def opcao_carregar():
    carregar_tarefas()
    print("\n✔ Tarefas carregadas \n")
