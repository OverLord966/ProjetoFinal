# Aqui vai o código principal do meu projeto
#

def mostrar_menu():
    print("\n===== GESTOR DE TAREFAS =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Editar tarefa")
    print("4. Remover tarefa")
    print("5. Guardar tarefas")
    print("6. Carregar tarefas")
    print("0. Sair")
    print("==============================")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção ainda não implementada.")

if __name__ == "__main__":
    main()

