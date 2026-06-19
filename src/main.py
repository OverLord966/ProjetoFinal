from ui.menu import (
    mostrar_menu,
    opcao_criar,
    opcao_listar,
    opcao_editar,
    opcao_mover,
    opcao_concluir,
    opcao_apagar,
    opcao_guardar,
    opcao_carregar
)

# Ponto de entrada principal da aplicação.
# Mostra o menu e encaminha a opção escolhida para a função correspondente.

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
        elif opcao == "7":
            opcao_guardar()
        elif opcao == "8":
            opcao_carregar()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("❌ Opção inválida!")

# Só corre no Main.py. sem este código ele não iria correr código que devia
if __name__ == "__main__":
    main()
