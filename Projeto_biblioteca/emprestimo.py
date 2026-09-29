import livros
import alunos

#Em ajustado
emprestimos = []

def realizar_emprestimo():

    matricula = input("Digite a matrícula do aluno: ")

    titulo = input("Digite o título do livro: ").lower()

    aluno_encontrado = False
    livro_encontrado = False

    for contador in alunos.alunos:
        if contador[1] == matricula:
            aluno_encontrado = True

    for contador in livros.livros:
        if contador[0] == titulo:
            livro_encontrado = True

    if aluno_encontrado == False:
        print("Aluno não encontrado.")

    elif livro_encontrado == False:
        print("Livro não encontrado.")

    else:
        emprestimos.append([matricula, titulo])
        print("Empréstimo realizado!")

def Menu_emprestimo():
    while True:

        print("\n===== SISTEMA DE EMPRÉSTIMOS =====")
        
        print("1 - Realizar empréstimo")
        print("2 - Listar empréstimo")

        print(" - Voltar ao menu anterior")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            realizar_emprestimo()

        elif opcao == "2":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")