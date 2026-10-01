import os
import livros
import alunos
from datetime import datetime

emprestimos = []

def Realizar_emprestimo():
    data_emprestimo = datetime.today()

    matricula = input("Digite a matrícula do aluno: ")

    titulo = input("Digite o título do livro: ").lower()

    aluno_encontrado = False
    livro_encontrado = False
    livro_emprestado = False

    for contador in alunos.alunos:
        if contador[1] == matricula:
            aluno_encontrado = True

    for contador in livros.livros:
        if contador[0] == titulo:
            livro_encontrado = True

    for contador in emprestimos:
        if contador[1] == titulo:
            livro_emprestado = True

    if aluno_encontrado == False:
        print("Aluno não encontrado.")

    elif livro_encontrado == False:
        print("Livro não encontrado.")

    elif livro_emprestado == True:
        print("Livro não dísponivel para empréstimo.")

    else:
        emprestimos.append([matricula, titulo, data_emprestimo])
        print("Empréstimo realizado!")
        print(f"Data do empréstimo: {data_emprestimo.strftime('%d/%m/%Y')}")

def Listar_emprestimo():
    print("\n--- EMPRÉSTIMOS ---")

    if len(emprestimos) == 0:
        print("Nenhum empréstimo realizado.")

    for contador in emprestimos:
        print(f"Matrícula: {contador[0]}")
        print(f"Livro: {contador[1].title()}")
        print(f"Data do empréstimo: {contador[2].strftime('%d/%m/%Y')}")

def Menu_emprestimo():
    while True:
        os.system("cls")

        print("\n===== SISTEMA DE EMPRÉSTIMOS =====")
        
        print("1 - Realizar empréstimo")
        print("2 - Listar empréstimo")
        print("3 - Voltar ao menu anterior")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            Realizar_emprestimo()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "2":
            Listar_emprestimo()
            input("\nPressione ENTER para voltar ao menu...")
        
        elif opcao == "3":
            break

        else:
            print("Opção inválida!")
            input("\nPressione ENTER para voltar ao menu...")