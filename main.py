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


#Criando funções
def salvar_funcionarios(funcionario):
    inserir_nome = input("Insira seu nome: ")
    inserir_idade = input("Insira sua idade: ")
    inserir_cpf = input("Insira seu cpf: ")
    inserir_setor = input("Insira seu setor: ")
    inserir_salario = input("Insira seu salário: ")
    inserir_funcao = input("Insira seu setor: ")
    inserir_telefone = input("Insira seu telefone: ")

    funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, salario=inserir_salario, funcao=inserir_funcao, telefone=inserir_telefone)

    session.add(funcionario)
    session.commit()

    return funcionario

def listar_todos_funcionarios():
    lista_funcionarios = session.query(Funcionario).all()

    for funcionario in lista_funcionarios:
        print(f"{funcionario.nome} \n{funcionario.idade} \n{funcionario.cpf} \n{funcionario.setor} \n{funcionario.salario} \n{funcionario.funcao} \n{funcionario.telefone}")
    

def pesquisar_funcionario(funcionario):
    cpf_funcionario = input("Informe o cpf do funcionário: ")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

    return funcionario

while True:
    menu()
    opcao = input("\nDigite o numero da operação desejada: ")
    
    match(opcao):
        case 1:
            pass
            #1 || Adicionar funcionário.
        case 2:
            pass
            #2 || Consultar um funcionário.
        case 3:
            pass
            #3 || Atualizar os dados de um funcionário.
        case 4:
            pass
            #4 || Excluir um funcionário.
        case 5:
            pass
            #5 || Listar todos os funcionários.
        case 0:
            #0 || Sair do sistema.
            break
        case _:
            print("Opção invalida \nTente novamente")


    
