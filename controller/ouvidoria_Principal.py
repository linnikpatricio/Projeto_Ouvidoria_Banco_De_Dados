from service.funcoes import *


def main():

    while True:
        menu_principal()
        opcao = le_int("Insira uma Opção: ")
        if opcao == 1:
            lista_manifestacoes()
        elif opcao == 2:
            lista_manifestacoes_por_tipo()
        elif opcao == 3:
            cria_manifestacoes()
        elif opcao == 4:
            exibe_quantidade_de_manifestacoes()
        elif opcao == 5:
            pesquisar_manifestacao_por_codigo()
        elif opcao == 6:
            exclui_manifestacao()
        elif opcao == 7:
            exit()
        else:
            print("Opção inválida! Por favor insira outra Opção")

