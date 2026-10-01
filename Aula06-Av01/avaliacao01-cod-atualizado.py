# PROVA
from datetime import datetime

ano_atual = datetime.now().year

continua = True 

for i in range(5):

    if continua == True:

        print("=================================")
        print("     SISTEMA PARA BIBLIOTECA")
        print("=================================")
        print("\n1 - Cadastrar livros")
        print("2 - Cadastrar Alunos")
        print("3 - Realizar Empréstimo")
        print("4 - Sair")
        print("")
        opcao = int(input("Escolha uma opção: "))

        valido = True     

        if opcao == 1: 
            qtd_livro_cadastrada = int(input("\nQuantos livros deseja cadastra?  "))
            
            for i in range(qtd_livro_cadastrada):
                i += 1
                
                cod_livro = (input("\nCódigo do livro: "))
                if cod_livro == "" or not cod_livro.isdigit():
                    print("Erro: Código deve ser válido.")
                    valido = False
                else:
                    cod_livro = int(cod_livro)
                
                titulo_livro = str(input("Título do livro: "))
                if titulo_livro == "":
                    print("Erro: Título deve ser válido.")
                    valido = False
                
                nome_autor = str(input("Nome do autor: "))
                if nome_autor == "":
                    print("Erro: Nome do autor deve ser válido. ")
                    valido = False
                
                ano_publicacao = (input("Ano de publicação: "))
                if ano_publicacao == "" or not ano_publicacao.isdigit():
                    print("Erro: Ano deve ser válido.")
                    valido = False
                else:
                    ano_publicacao = int(ano_publicacao)

                    if ano_publicacao < 0 or ano_publicacao > ano_atual:
                        print(f"Erro: Ano deve ser entre 0 e {ano_atual}.")
                        valido = False

                qtd_disponivel = int(input("Quantidade disponível: "))
                if qtd_disponivel <= 0:
                    print("Erro: Quantidade deve ser válida.")
                
                print(f"\n----- LIVRO {i} -----")
                print(f"Código: {cod_livro}")
                print(f"Título: {titulo_livro}")
                print(f"Autor: {nome_autor}")
                print(f"Ano: {ano_publicacao}")
                print(f"Quantidade: {qtd_disponivel}")
                print("\nLivro cadastrado com sucesso!")

                
        elif opcao == 2:
            qtd_alunos_cadastrada = int(input("\nQuantos alunos deseja cadastrar? "))
            for i in range(qtd_alunos_cadastrada):
                i += 1

                matricula = (input("\nMatrícula: "))
                if matricula == "" or not matricula.isdigit():
                    print("Erro: Matrícula deve ser válida.")
                    valido = False
                else:
                    matricula = int(matricula)
                
                nome_aluno = str(input("Nome do aluno: "))
                if nome_aluno == "":
                    print("Erro: Nome deve ser válido.")
                    valido = False

                turma = (input("Turma: "))
                if turma == "" or not turma.isdigit():
                    print("Erro: Turma deve ser válida. ")
                    valido = False
                else:
                    turma = int(turma)

                print(f"\n----- ALUNO {i} -----")
                print(f"Matrícula: {matricula}")
                print(f"Nome: {nome_aluno}")
                print(f"Turma: {turma}")
                print(f"\nAluno cadastrado com sucesso!")
        
        elif opcao == 3:
            
            cod_livro = (input("\nCódigo do livro: "))
            if cod_livro == "" or not cod_livro.isdigit():
                print("Erro: Código deve ser válida.")
                valido = False
            else:
                cod_livro = int(cod_livro)

            matricula = (input("Matrícula: "))
            if matricula == "" or not matricula.isdigit():
                print("Erro: Matrícula deve ser válida.")
                valido = False
            else:
                matricula = int(matricula)

            qtd_disponivel = int(input("Quantidade disponível: "))
                    
            print("\n----- EMPRÉSTIMO -----")
            print(f"\nCódigo do livro: {cod_livro}")
            print(f"Matrícula do aluno: {matricula}")
            print(f"Quantidade disponível: {qtd_disponivel}")
            
            if qtd_disponivel > 0:
                print("\nEmpréstimo realizado com sucesso!\n")
            elif qtd_disponivel == 0:
                print("\nNão é possível realizar o empréstimo.")
                print("Não há exemplares disponíveis.\n")

        elif opcao == 4:
            print("\nSaindo do sistema.\n")
            continua = False

        else:
            print("\nOpção inválida. Digite entre 1 a 4.\n")