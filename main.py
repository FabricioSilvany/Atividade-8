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
    inserir_nome = input("Insira o nome do funcionário: ")
    inserir_idade = int(input("Insira a idade do funcionário: "))
    inserir_cpf = input("Insira o cpf do funcionário: ")
    inserir_setor = input("Insira o setor do funcionário: ")
    inserir_salario = float(input("Insira o salário do funcionário: "))
    inserir_funcao = input("Insira a função do funcionário: ")
    inserir_telefone = input("Insira o telefone do funcionário: ")

    funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, salario=inserir_salario, funcao=inserir_funcao, telefone=inserir_telefone)

    session.add(funcionario)
    session.commit()

    os.system("cls || clear")
    print("Funcionário salvo!")

    return funcionario

def listar_todos_funcionarios(funcionario):
    lista_funcionarios = session.query(Funcionario).all()

    for funcionario in lista_funcionarios:
        print(f"Nome: {funcionario.nome} \nIdade: {funcionario.idade} \nCPF: {funcionario.cpf} \nSetor: {funcionario.setor} \nSalário: {funcionario.salario} \nFunção: {funcionario.funcao} \nTelefone: {funcionario.telefone}\n")   

def pesquisar_funcionario(funcionario):
    cpf_funcionario = input("Informe o cpf do funcionário: ")
    os.system("cls || clear")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

    print(f"Dados do funcionário: \nNome: {funcionario.nome} \nIdade: {funcionario.idade} \nCPF: {funcionario.cpf} \nSetor: {funcionario.setor} \nSalário: {funcionario.salario} \nFunção: {funcionario.funcao} \nTelefone: {funcionario.telefone}")

def atualizar_funcionario(funcionario):
    cpf_funcionario = input("Informe o cpf do funcionário para atualização: ")
    os.system("cls || clear")

    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

    novos_dados = Funcionario(
        nome = input("Informe o nome do funcionário: "),
        idade = int(input("Informe a idade do funcionário: ")),
        cpf = input("Informe o cpf do funcionário: "),
        setor = input("Informe o setor do funcionário: "),
        salario = float(input("Informe o salário do funcionário: ")),
        funcao = input("Informe qual função o funcionário exerce: "),
        telefone = input("Informe o telefone do funcionário: "))
    
    funcionario = novos_dados
    session.add(funcionario)
    session.commit()

    os.system("cls || clear")
    print("Funcionário atualizado")
    return funcionario, novos_dados

def excluir_funcionario(funcionario):
    cpf_funcionario = input("Digite o cpf do funcionario a ser excluido: ")

    funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()
    session.delete(funcionario)
    session.commit()

    print("\nFuncionário excluido.")

while True:
    menu()
    opcao = int(input("\nDigite o numero da operação desejada: "))

    os.system("cls || clear")
    
    match(opcao):
        case 1:
            pass
            #1 || Adicionar funcionário.
            adicionando_funcionario = salvar_funcionarios(opcao)

            adicionando_funcionario

        case 2:
            busca_funcionario = pesquisar_funcionario(opcao)

            busca_funcionario
            #2 || Consultar um funcionário.
        case 3:
            funcionario_atualizado = atualizar_funcionario(opcao)

            funcionario_atualizado
            #3 || Atualizar os dados de um funcionário.

        case 4:
            deletando_funcionario = excluir_funcionario(opcao)

            deletando_funcionario
            #4 || Excluir um funcionário.

        case 5:
            listando_funcionario = listar_todos_funcionarios(opcao)

            listando_funcionario
            #5 || Listar todos os funcionários.

        case 0:
            #0 || Sair do sistema.
            break

        case _:
            print("Opção invalida \nTente novamente")


#Fechando conexão.
session.close()