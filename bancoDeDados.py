import mysql.connector
from mysql.connector import Error
import pandas as pd

class BancoDeDados:
    def __init__(self, host, usuario, senha, banco_de_dados):
        """
        Inicializa a classe BancoDeDados com as informações de conexão.
        
        Parametros:
            host (str): Host do banco de dados.
            usuario (str): Nome de usuário do banco de dados.
            senha (str): Senha do usuário do banco de dados.
            banco_de_dados (str): Nome do banco de dados.
        """
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco_de_dados = banco_de_dados
        self.conexao = None

        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco_de_dados
            )
            print("Conexão ao banco de dados estabelecida.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def desconectar(self):
        """
        Encerra a conexão com o banco de dados MySQL.
        """
        if self.conexao:
            self.conexao.close()
            print("Conexão ao banco de dados encerrada.")

    def inserir_usuario(self, tabela, nome, email, senha, cargo, projeto, area):
        """
        Insere dados em uma tabela específica no banco de dados.

        Parametros:
            tabela (str): Nome da tabela onde os dados serão inseridos.
            dados (dict): Um dicionário contendo os dados a serem inseridos na tabela.
        """
        dados = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "cargo": cargo,
            "projeto": projeto,
            "area": area
        }
        try:
            cursor = self.conexao.cursor()
            placeholders = ', '.join(['%s' for _ in dados])
            colunas = ', '.join(dados.keys())
            valores = tuple(dados.values())
            consulta = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"
            cursor.execute(consulta, valores)
            self.conexao.commit()
            print("Dados inseridos com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")

    def ler_dados(self, tabela, colunas='*', condicao=None):
        """
        Lê dados de uma tabela no banco de dados.

        Parametros:
            tabela (str): Nome da tabela a partir da qual os dados serão lidos.
            colunas (str): Colunas a serem selecionadas na consulta (por padrão, todas as colunas).
            condicao (str): Uma condição opcional para filtrar os resultados (por padrão, sem filtro).

        Returns:
            list: Uma lista de tuplas contendo os resultados da consulta.
        """
        try:
            cursor = self.conexao.cursor()
            consulta = f"SELECT {colunas} FROM {tabela}"
            if condicao:
                consulta += f" WHERE {condicao}"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as err:
            print(f"Erro ao ler dados: {err}")
            return []

    def atualizar_dados(self, tabela, novos_dados, condicao):
        """
        Atualiza dados em uma tabela com base em uma condição.

        Parametros:
            tabela (str): Nome da tabela onde os dados serão atualizados.
            novos_dados (dict): Um dicionário contendo os novos valores a serem atualizados.
            condicao (str): Uma condição que determina quais registros serão atualizados.
        """
        try:
            cursor = self.conexao.cursor()
            colunas = ', '.join([f"{coluna} = %s" for coluna in novos_dados.keys()])
            valores = tuple(novos_dados.values())
            consulta = f"UPDATE {tabela} SET {colunas} WHERE {condicao}"
            cursor.execute(consulta, valores)
            self.conexao.commit()
            print("Dados atualizados com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar dados: {err}")



