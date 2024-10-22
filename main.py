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
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    salario = Column("salario", Float)
    funcao = Column("funcao", String)
    telefone = Column("telefone", String)

    def __init__(self, nome: str, idade: int, cpf: str, setor: str, salario: Float, funcao: str, telefone: str):
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
    inserir_idade = int(input("Insira sua idade: "))
    inserir_cpf = input("Insira seu cpf: ")
    inserir_setor = input("Insira seu setor: ")
    inserir_salario = float(input("Insira seu salário: "))
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
    print(f"{funcionario}")
 
def atualizar_funcionario(funcionario):
    cpf_funcionario = input("Informe o cpf do funcionário: ")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

    novos_dados = Funcionario(
        nome = input("Informe o nome do funcionário: "),
        idade = int(input("Informe a idade do funcionário: ")),
        cpf = input("Informe o cpf do funcionário: "),
        setor = input("Informe o setor do funcionário: "),
        salario = float(input("Informe o salário do funcionário: "))
        funcao = input("Informe qual função o funcionário exerce: ")
        telefone = input("Informe ")
    )


while True:
    menu()
    opcao = input("\nDigite o numero da operação desejada: ")
    
    match(opcao):
        case 1:
            pass
            #1 || Adicionar funcionário.
            adicionando_funcionario = salvar_funcionarios()
        case 2:
            busca_funcionario = pesquisar_funcionario()
            #2 || Consultar um funcionário.
        case 3:
            pass
            #3 || Atualizar os dados de um funcionário.
        case 4:
            pass
            #4 || Excluir um funcionário.
        case 5:
            listando_funcionario = listar_todos_funcionarios()
            #5 || Listar todos os funcionários.
        case 0:
            #0 || Sair do sistema.
            break
        case _:
            print("Opção invalida \nTente novamente")


    
