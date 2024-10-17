import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando Banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão com o banco de dados.

Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#Criando tabela
Base = declarative_base()


class Funcionario(Base):
    __tablename__ = "funcionarios"

    #Campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", String)
    salario = Column("salario", float)
    funcao = Column("funcao", String)
    telefone = Column("telefone", Integer)

    def __init__(self, nome: str, idade: int, cpf: int, setor: str, salario: float, funcao: str, telefone: int):
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

