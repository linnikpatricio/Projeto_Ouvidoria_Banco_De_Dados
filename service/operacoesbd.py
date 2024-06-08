import mysql.connector

def criarConexao(endereco,usuario, senha, bancodedados):
      return mysql.connector.connect(
  host=endereco,user=usuario, password=senha,database=bancodedados)

def encerrarBancoDados(connection):
      connection.close()

def insertNoBancoDados(dados):
      connection = criarConexao("127.0.0.1", "root", "981105976", "locadora")
      sql = "INSERT INTO MANIFESTACOES (tipo,manifestacao) VALUES (%s,%s)"
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      id = cursor.lastrowid
      cursor.close()
      encerrarBancoDados(connection)
      return id

def listarBancoDados():
      connection = criarConexao("127.0.0.1", "root", "981105976", "locadora")
      cursor = connection.cursor()
      sql = "select * from manifestacoes"
      cursor.execute(sql)
      manifestacao = cursor.fetchall()
      if len(manifestacao) == 0:
            print("Não existe Manifestações!")
      else:
            print("Lista de Manifestações")
            for item in manifestacao:
                  print("Código -", item[0], "| Tipo -", item[1], "| Manifestação -", item[2])
      cursor.close()
      encerrarBancoDados(connection)

def listarBancoDadosPorTipo(tipo):
      connection = criarConexao("127.0.0.1", "root", "981105976", "locadora")
      cursor = connection.cursor()
      sql = "select * from manifestacoes where tipo = %s "
      cursor.execute(sql, (tipo,))
      manifestacao = cursor.fetchall()
      if len(manifestacao) == 0:
            print("Não existe manifestações dessa categoria")
      else:
            print("Lista de Manifestações da Categoria", tipo)
            for item in manifestacao:
                  print("Código -", item[0], "| Tipo -", item[1], "| Manifestação -", item[2])
      cursor.close()
      encerrarBancoDados(connection)


def pesquisarManifestacao_PorCodigo_BancoDeDados(codigo):
      connection = criarConexao("127.0.0.1", "root", "981105976", "locadora")
      cursor = connection.cursor()
      sql = "select * from manifestacoes where codigo = %s "
      cursor.execute(sql,(codigo,))
      lista = cursor.fetchall()
      if len(lista) == 0:
            print("Não existe Manifestação com o Código pesquisado!")
      else:
            print("Manifestação pesquisada")
            for item in lista:
                  print("Código -", item[0], "| Tipo -", item[1], "| Manifestação -", item[2])

      cursor.close()
      encerrarBancoDados(connection)

def atualizarBancoDados(connection,sql, dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      linhasAfetadas = cursor.rowcount
      cursor.close()
      return linhasAfetadas

def excluirBancoDados(codigo):
      connection = criarConexao("127.0.0.1", "root", "981105976", "locadora")

      cursor = connection.cursor()
      sql = "DELETE FROM manifestacoes WHERE CODIGO = %s"
      cursor.execute(sql, (codigo,))
      connection.commit()

      if cursor.rowcount == 0:
            print("Código inserido não existe! ")
      else:
            print(f"Manifestação com código {codigo} excluído com sucesso.")

      cursor.close()
      encerrarBancoDados(connection)


def exibeQuantidade():
      connection = criarConexao("127.0.0.1", "root", "981105976", "locadora")
      cursor = connection.cursor()
      cursor.execute("SELECT COUNT(*) FROM manifestacoes")
      result = cursor.fetchone()
      cursor.close()
      encerrarBancoDados(connection)
      return result[0]
