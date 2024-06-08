from view.menu import *

def le_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Opção inválida! Por favor insira um número")

def escolhe_tipo_manifestacao():
    tipos = ["Reclamação", "Elogio", "Sugestão"]
    while True:

        try:
            menu_de_manifestacoes()
            categoria = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.\n")
            continue

        if categoria == 1:
            return tipos[0]
        elif categoria == 2:
            return tipos[1]
        elif categoria == 3:
            return tipos[2]
        else:
            print("Opção inválida. Tente novamente!")
