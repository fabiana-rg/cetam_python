import os

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

alunos = []

# Cadastro de aluno
def Cadastrar_aluno():
    nome = input("Digite o nome: ").lower()
    
    if nome.replace(" ", "").isalpha() == False:
        print("O nome deve conter letras.")
        return

    matricula = input("Digite a matrícula: ")
    if matricula.isdigit() == False:
        print("A matrícula deve conter apenas números.")
        return

    matricula_encontrada = False

    for contador in alunos:
        #if contador[1] == matricula:
        if contador.matricula == matricula:
            matricula_encontrada = True

    if matricula_encontrada == True:
        print("Essa matrícula já está cadastrada!")
        2
    else:
        #alunos.append([nome, matricula])
        alunos.append(Aluno(nome, matricula))
        print("Aluno cadastrado!")

# Listagem de alunos
def Listar_aluno():
    print("\n---- ALUNOS CADASTRADOS ----")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado ainda.")

    for contador in alunos:
        #print("Nome:", contador[0].title())
        #print("Matrícula:", contador[1],)
        print("Nome:", contador.nome.title())
        print("Matrícula:", contador.matricula)
        
        
# Pesquisa de aluno
def Pesquisar_aluno():
#adicionar um menu para escolher como pesquisar pelo nome do aluno (.lower() e trocar o contador por [0])
    pesquisa = input("Digite a matrícula que deseja pesquisar: ")
    if pesquisa.isdigit() == False:
        print("A mtrícula deve conetr apenas números.")
        return

    aluno_encontrado = False

    for contador in alunos:
        #if contador[1] == pesquisa:
        if contador.matricula == pesquisa:
            aluno_encontrado = True
            print("Aluno encontrado!")
            #print("Nome:", contador[0].title())
            #print("Matrícula:", contador[1])
            print("Nome:", contador.nome.title())
            print("Matrícula:", contador.matricula)

    if aluno_encontrado == False:
        print("Aluno não encontrado.") 

# Exclusão de aluno
def Excluir_aluno():

    pesquisa = input("Digite a matrícula que deseja excluir: ")
    if pesquisa.isdigit() == False:
        print("A mtrícula deve conetr apenas números.")
        return

    aluno_encontrado = False

    for contador in alunos:
        #if contador[1] == pesquisa:
        if contador.matricula == pesquisa:
            aluno_encontrado = True
            alunos.remove(contador)######modificar
            print("Aluno excluído!")

    if aluno_encontrado == False:
        print("Aluno não encontrado.")

# Quantidade de alunos
def Quantidade_aluno():
    print("Quantidade de alunos:", len(alunos))

def Menu_alunos():
    while True:
        os.system("cls")

        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Pesquisar aluno")
        print("4 - Excluir aluno")
        print("5 - Quantidade de alunos")
        print("6 - Voltar ao menu anterior")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            Cadastrar_aluno()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "2":
            Listar_aluno()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "3":
            Pesquisar_aluno()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "4":
            Excluir_aluno()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "5":
            Quantidade_aluno()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para voltar ao menu...")