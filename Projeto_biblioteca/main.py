import livros
import alunos
import emprestimo

while True:
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Sistema de livros")
    print("2 - Sistema de alunos")
    print("3 - Sistema de empréstimo")
    print("4 - Encerrrar a sessão")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        livros.Menu_livros()

    elif opcao == "2":
        alunos.Menu_alunos()
    
    elif opcao == "3":
        emprestimo.Menu_emprestimo()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")