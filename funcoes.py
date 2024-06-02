from operacoesbd import *
import mysql.connector

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

def menu_principal():
    print(" === Menu de Opções ===")
    print("1. Listagem das Manifestações")
    print("2. Listagem de Manifestações por Tipo")
    print("3. Criar uma nova Manifestação ")
    print("4. Exibir quantidade de Manifestações ")
    print("5. Pesquisar uma Manifestação por Código")
    print("6. Excluir uma Manifestação pelo Código")
    print("7. Sair do Sistema.")

def menu_de_manifestacoes():
    print(" == Menu de Manifestações == ")
    print("Escolha o tipo de manifestação:")
    print("1. Reclamação")
    print("2. Elogio")
    print("3. Sugestão")

def lista_manifestacoes():
    con = criarConexao("127.0.0.1","root","981105976","locadora")

    consultaLista = "select * from manifestacoes"
    manifestacao = listarBancoDados(con,consultaLista)
    if len(manifestacao) == 0:
        print("Não existe Manifestações!")
    else:
        print("Lista de Manifestações")
        for item in manifestacao:
            print("Código -",item[0],"| Tipo -",item[1],"| Manifestação -",item[2])

    encerrarBancoDados(con)

def lista_manifestacoes_por_tipo():
    con = criarConexao("127.0.0.1", "root", "981105976", "locadora")
    tipo = input("Digite o tipo de manifestação: ")

    consultaLista = "select * from manifestacoes where tipo = '" + tipo + "'"
    manifestacao = listarBancoDados(con, consultaLista)
    if tipo in manifestacao == None:
        print("Essa Categoria não existe!")
    elif len(manifestacao) == 0:
        print("Não existe manifestações dessa categoria")
    else:
        print("Lista de Manifestações da Categoria",tipo)
        for item in manifestacao:
            print("Código -", item[0], "| Tipo -", item[1], "| Manifestação -", item[2])

    encerrarBancoDados(con)

def cria_manifestacoes():
    global manifestacoes
    con = criarConexao("127.0.0.1","root","981105976","locadora")
    tipo = escolhe_tipo_manifestacao()
    descricao = input("Digite a mensagem da manifestação: ")
    manifestacoes = [tipo,descricao]
    print("Manifestação criada com sucesso!")

    consultInsert = "INSERT INTO MANIFESTACOES (tipo,manifestacao) VALUES (%s,%s)"
    insertNoBancoDados(con,consultInsert,manifestacoes)
    encerrarBancoDados(con)

def pesquisar_manifestacao_por_codigo():
    con = criarConexao("127.0.0.1", "root", "981105976", "locadora")
    codigo = le_int("Digite o Código: ")
    consultaListar = "select * from manifestacoes where codigo =" + str(codigo)
    manifestacao = listarBancoDados(con, consultaListar)
    if len(manifestacao) == 0:
        print("Não existe manifestação para o código informado! ")
    else:
        print("Manifestação pesquisada")
        for item in manifestacao:
            print("Código -", item[0], "| Tipo -", item[1], "| Manifestação -", item[2])

    encerrarBancoDados(con)

def exibe_quantidade_de_manifestacoes():
    con = criarConexao("127.0.0.1", "root", "981105976", "locadora")

    consultaLista = "SELECT COUNT(*) FROM manifestacoes"
    quantidadeDeManifestacoes = listarBancoDados(con, consultaLista)
    if len(quantidadeDeManifestacoes) == 0:
        print("Não existe Manifestações!")
    else:
        print("Quantidade de manifestações: ",quantidadeDeManifestacoes)

    encerrarBancoDados(con)

def exclui_manifestacao():
    con = criarConexao("127.0.0.1", "root", "981105976", "locadora")

    cursor = con.cursor()

    codigo = le_int("Digite o Código: ")
    consultaLista = "DELETE FROM manifestacoes WHERE CODIGO = %s"
    excluirBancoDados(con, consultaLista, (codigo,))

    if cursor.rowcount == 0:
        print("Código inserido não existe! ")
    else:
        print(f"Manifestação com código {codigo} excluído com sucesso.")


    encerrarBancoDados(con)






