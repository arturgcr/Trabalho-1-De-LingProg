import mysql.connector
from mysql.connector import Error
import pandas as pd

class BancoDeDados:
    def __init__(self, host="localhost", usuario="admBots", senha="senha", banco_de_dados="minervabots"):
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

        
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco_de_dados
        )
        print("Conexão ao banco de dados estabelecida.")


    def desconectar(self):
        """
        Encerra a conexão com o banco de dados MySQL.
        """
        if self.conexao:
            self.conexao.close()
            print("Conexão ao banco de dados encerrada.")

    def inserir_usuario(self, nome, email, senha, cargo):
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
        }
        try:
            cursor = self.conexao.cursor()
            placeholders = ', '.join(['%s' for _ in dados])
            colunas = ', '.join(dados.keys())
            valores = tuple(dados.values())
            consulta = f"INSERT INTO usuario ({colunas}) VALUES ({placeholders})"
            cursor.execute(consulta, valores)
            self.conexao.commit()
            print("Dados inseridos com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")

    def inserir_area(self, nome_area, email_usuario):
        """
        Insere dados em uma tabela de áreas associados a um usuário específico.

        Parametros:
            nome_area (str): Nome da área a ser inserida.
            email_usuario (str): Email do usuário ao qual a área está associada.
        """
        try:
            cursor = self.conexao.cursor()
            consulta = "INSERT INTO area (nome_area, FK_area_usuario_email) VALUES (%s, %s)"
            valores = (nome_area, email_usuario)
            cursor.execute(consulta, valores)
            self.conexao.commit()
            print("Dados de área inseridos com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados de área: {err}")

    def inserir_projeto(self, nome_projeto, email_usuario):
        """
        Insere dados em uma tabela de projetos associados a um usuário específico.

        Parametros:
            nome_projeto (str): Nome do projeto a ser inserido.
            email_usuario (str): Email do usuário ao qual o projeto está associado.
        """
        try:
            cursor = self.conexao.cursor()
            consulta = "INSERT INTO projeto (nome_projeto, FK_projeto_usuario_email) VALUES (%s, %s)"
            valores = (nome_projeto, email_usuario)
            cursor.execute(consulta, valores)
            self.conexao.commit()
            print("Dados de projeto inseridos com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados de projeto: {err}")

    def ler_dados(self, tabela="usuario", colunas='*', condicao=None):
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

    def criar_colunas_tabela(self, tabela, colunas):
        """
        Cria colunas em uma tabela no banco de dados.

        Parametros:
            tabela (str): Nome da tabela onde as colunas serão criadas.
            colunas (dict): Um dicionário que mapeia o nome da coluna para o tipo de dados.

        Onde usamos:
            colunas = {
                'nome': 'VARCHAR(255)',
                'email': 'VARCHAR(255)',
                'senha': 'VARCHAR(255)',
                'cargo': 'VARCHAR(255)',
                'projeto': 'VARCHAR(255)',
                'area': 'VARCHAR(255)'
            }
            banco_de_dados.criar_colunas_tabela('banco_de_usuarios', colunas)
        """
        try:
            cursor = self.conexao.cursor()
            for coluna, tipo in colunas.items():
                consulta = f"ALTER TABLE {tabela} ADD COLUMN {coluna} {tipo}"
                cursor.execute(consulta)
            self.conexao.commit()
            print("Colunas criadas com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar colunas: {err}")



    def excluir_dado(self, tabela, identificador, selecionado):
        """
        Exclui um usuário por completo do banco de dados.

        Parametros:
            id_usuario (int): O ID (ou outra identificação única) do usuário a ser excluído.
        """
        try:
            cursor = self.conexao.cursor()
            consulta = f"DELETE FROM {tabela} WHERE {identificador} = %s" 
            cursor.execute(consulta, (selecionado,))
            self.conexao.commit()
            print("Usuário excluído com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao excluir usuário: {err}")