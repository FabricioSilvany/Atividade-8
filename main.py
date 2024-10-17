import os

from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando Banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão com o banco de dados.

Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#Criando tabela
Base = declarative_base()

def menu ():
    print("""
           == RH SISTEM == 
    1 || Adicionar funcionário.
    2 || Consultar um funcionário.
    3 || Atualizar os dados de um funcionário.
    4 || Excluir um funcionário.
    5 || Listar todos os funcionários.
    0 || Sair do sistema.   
    """)

class Funcionario(Base):
    __tablename__ = "funcionarios"

    #Campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", String)
    salario = Column("salario", Float)
    funcao = Column("funcao", String)
    telefone = Column("telefone", Integer)

    def __init__(self, nome: str, idade: int, cpf: int, setor: str, salario: Float, funcao: str, telefone: int):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.salario = salario
        self.funcao = funcao
        self.telefone = telefone

    #Criando tabela no banco de dados
    Base.metadata.create_all(bind=MEU_BANCO)

    #Salvando banco de dados
    os.system("cls || clear")

while True:
    menu()
    opcao = input("\nDigite o numero da operação desejada: ")
    
    match(opcao):
        case 1:
            #1 || Adicionar funcionário.
        case 2:
            #2 || Consultar um funcionário.
        case 3:
            #3 || Atualizar os dados de um funcionário.
        case 4:
            #4 || Excluir um funcionário.
        case 5:
            #5 || Listar todos os funcionários.
        case 0:
            #0 || Sair do sistema.
            break
        case _:
            print("Opção invalida \nTente novamente")