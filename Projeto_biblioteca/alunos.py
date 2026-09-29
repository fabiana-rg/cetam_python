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
        if contador[1] == matricula:
            matricula_encontrada = True

    if matricula_encontrada == True:
        print("Essa matrícula já está cadastrada!")
        2
    else:
        alunos.append([nome, matricula])
        print("Aluno cadastrado!")

# Listagem de alunos
def Listar_aluno():
    print("\n---- ALUNOS CADASTRADOS ----")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado ainda.")

    for contador in alunos:
        print("Nome:", contador[0].title())
        print("Matrícula:", contador[1],)
        
# Pesquisa de aluno
def Pesquisar_aluno():
#adicionar um menu para escolher como pesquisar pelo nome do aluno (.lower() e trocar o contador por [0])
    pesquisa = input("Digite a matrícula que deseja pesquisar: ")
    if pesquisa.isdigit() == False:
        print("A mtrícula deve conetr apenas números.")
        return

    aluno_encontrado = False

    for contador in alunos:
        if contador[1] == pesquisa:
            aluno_encontrado = True
            print("Aluno encontrado!")
            print("Nome:", contador[0].title())
            print("Matrícula:", contador[1])

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
        if contador[1] == pesquisa:
            aluno_encontrado = True
            alunos.remove(contador)
            print("Aluno excluído!")

    if aluno_encontrado == False:
        print("Aluno não encontrado.")

# Quantidade de alunos
def Quantidade_aluno():
    print("Quantidade de alunos:", len(alunos))

def Menu_alunos():
    while True:

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

        elif opcao == "2":
            Listar_aluno()

        elif opcao == "3":
            Pesquisar_aluno()

        elif opcao == "4":
            Excluir_aluno()

        elif opcao == "5":
            Quantidade_aluno()

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")