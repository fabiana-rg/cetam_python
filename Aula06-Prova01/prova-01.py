#ENTRADA DE DADO

print("=================================")
print("     SISTEMA PARA BIBLIOTECA")
print("=================================")
print("")
""" 
operacoes = int(input("Quanatas operações deseja realizar?"))
for i in range (operacoes):
 """

print("\n1 - Cadastrar livros")
print("2 - Cadastrar Alunos")
print("3 - Realizar Empréstimo")
print("4 - Sair")
print("")
opcao = int(input("Escolha uma opção: "))

#Caso informe uma opção diferente de 1, 2, 3 ou 4, o sistema deverá informar que a opção é inválida.
valido = True
#PROCESSAMENTO COM CONDIÇÕES E ENTRADA DE DADOS
if opcao == 1: #Cadastrar Livros
    qtd_livro_cadastrada = int(input("Quantos livros deseja cadastra?  "))
    
    for i in range(qtd_livro_cadastrada):
        i += 1
        
        cod_livro = int(input("\nCódigo do livro: "))
        
        titulo_livro = str(input("Título do livro: "))
        if titulo_livro == "":
            print("Erro: Título deve ser válido.")
            valido = False
        
        nome_autor = str(input("Nome do autor: "))
        if nome_autor == "":
            print("Erro: Nome do autor deve ser válido. ")
            valido = False
        
        ano_publicação = int(input("Ano de publicação: "))
        if ano_publicação < 0 or ano_publicação > 2026:
            print("Erro: Ano deve ser válido.")
            valido = False

        qtd_disponivel = int(input("Quantidade disponível: "))
        if qtd_disponivel <= 0:
            print("Erro: Quantidade deve ser válida.")
        
        print(f"\n----- LIVRO {i} -----")
        print(f"Código: {cod_livro}")
        print(f"Título: {titulo_livro}")
        print(f"Autor: {nome_autor}")
        print(f"Ano: {ano_publicação}")
        print(f"Quantidade: {qtd_disponivel}")
        print("\nLivro cadastrado com sucesso!")

        
elif opcao == 2:
    qtd_alunos_cadastrada = int(input("Quantos alunos deseja cadastrar? "))
    for i in range(qtd_alunos_cadastrada):
        i += 1

        #valido = True
        matricula = int(input("\nMatrícula: "))
        if matricula == "":
            print("Erro: Matrícula deve ser válida.")
            valido = False
        
        nome_aluno = str(input("Nome do aluno: "))
        if nome_aluno == "":
            print("Erro: Nome deve ser válido.")
            valido = False

        turma = int(input("Turma: "))
        if turma == "":
            print("Erro: Turma deve ser válida. ")
            valido = False

        print(f"\n----- ALUNO {i} -----")
        print(f"Matrícula: {matricula}")
        print(f"Nome: {nome_aluno}")
        print(f"Turma: {turma}")
        print(f"\nAluno cadastrado com sucesso!")
 
elif opcao == 3:
    
    cod_livro = int(input("\nCódigo do livro: "))
    if cod_livro == "":
        print("Erro: Código deve ser válida.")
        valido = False

    matricula = int(input("Matrícula: "))
    if matricula == "":
        print("Erro: Matrícula deve ser válida.")
        valido = False

    qtd_disponivel = int(input("Quantidade disponível: "))
   

    print("\n----- EMPRÉSTIMO -----")
    print(f"\nCódigo do livro: {cod_livro}")
    print(f"Matrícula do aluno: {matricula}")
    print(f"Quantidade disponível: {qtd_disponivel}")
      
    if qtd_disponivel > 0:
        print("\nEmpréstimo realizado com sucesso!")
    elif qtd_disponivel == 0:
        print("\nNão é possível realizar o empréstimo.")
        print("Não há exemplares disponíveis.")

elif opcao == 4:
    print("Saindo do sistema")