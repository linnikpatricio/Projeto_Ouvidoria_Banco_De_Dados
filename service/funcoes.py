from service.operacoesbd import *

from view.menu import *

from utils.escolheTipoManifestacao_LeInt import *


def lista_manifestacoes():
    listarBancoDados()

def lista_manifestacoes_por_tipo():
    tipo = escolhe_tipo_manifestacao()
    listarBancoDadosPorTipo(tipo)



def cria_manifestacoes():
    tipo = escolhe_tipo_manifestacao()
    descricao = input("Digite a mensagem da manifestação: ")
    manifestacoes = (tipo,descricao)
    insertNoBancoDados(manifestacoes)
    print("Manifestação criada com sucesso!")


def pesquisar_manifestacao_por_codigo():
    codigo = input("Digite o Código: ")
    pesquisarManifestacao_PorCodigo_BancoDeDados(codigo)

def exibe_quantidade_de_manifestacoes():
    cont = exibeQuantidade()
    print(f"A Quantidade de Manifestaões é: {cont}")


def exclui_manifestacao():
    codigo = le_int("Digite o Código: ")
    excluirBancoDados(codigo)









