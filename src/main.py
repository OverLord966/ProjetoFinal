from ui.menu import (
    mostrar_menu,
    opcao_criar,
    opcao_listar,
    opcao_editar,
    opcao_mover,
    opcao_concluir,
    opcao_apagar
)

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcao_criar()
        elif opcao == "2":
            opcao_listar()
        elif opcao == "3":
            opcao_editar()
        elif opcao == "4":
            opcao_concluir()
        elif opcao == "5":
            opcao_apagar()
        elif opcao == "6":
            opcao_mover()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
