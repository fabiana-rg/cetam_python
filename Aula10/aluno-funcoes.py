alunos = []

# Cadastro de aluno
def cadastrar_aluno():
    nome = input("Digite o nome: ").lower()
    matricula = input("Digite a matrícula: ")

    matricula_encontrada = False

    for contador in alunos:
        if contador[1] == matricula:
            matricula_encontrada = True

    if matricula_encontrada == True:
        print("Essa matrícula já está cadastrada!")

    else:
        alunos.append([nome, matricula])
        print("Aluno cadastrado!")


    """ alunos.append([nome, matricula])

    print("Aluno cadastrado!") """


# Listagem de alunos
def listar_aluno():
    print("\n--- ALUNOS CADASTRADOS ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado ainda.")

    for contador in alunos:
        print("Nome:", contador[0].title())
        print("Matrícula:", contador[1])
        print("")


# Pesquisa de aluno
def pesquisar_aluno():

    pesquisa = input("Digite a matrícula que deseja pesquisar: ")

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
def excluir_aluno():

    pesquisa = input("Digite a matrícula que deseja excluir: ")

    aluno_encontrado = False

    for contador in alunos:
        if contador[1] == pesquisa:
            aluno_encontrado = True
            alunos.remove(contador)
            print("Aluno excluído!")

    if aluno_encontrado == False:
        print("Aluno não encontrado.")


# Quantidade de alunos
def quantidade_aluno():
    print("Quantidade de alunos:", len(alunos))


# Menu
while True:

    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Excluir aluno")
    print("5 - Quantidade de alunos")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_aluno()

    elif opcao == "3":
        pesquisar_aluno()

    elif opcao == "4":
        excluir_aluno()

    elif opcao == "5":
        quantidade_aluno()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")