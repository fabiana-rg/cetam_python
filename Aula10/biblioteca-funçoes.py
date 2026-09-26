biblioteca = []

# Cadrastro
def cadastrar_livro():
    titulo = input("Digite o título: ").lower()
    autor = input("Digite o autor: ").lower()

    biblioteca.append([titulo, autor])

    print("Livro cadastrado!")

# Listagem de livro
def listar_livro():
    print("\n--- LIVROS CADASTRADOS ---")

    if len(biblioteca) == 0:
        print("Nenhum livro cadrastrado ainda.")

    for contador in biblioteca:
        print("Título:", contador[0].title())
        print("Autor:", contador[1].title())
        print("")

# Pesquisa de livro
def pesquisar_livro():
    
    pesquisa = input("Digite o título que deseja pesquisar: ").lower() 
    livro_encontrado = False 

    for contador in biblioteca:
        if contador[0] == pesquisa:
            livro_encontrado = True  
            print("Livro encontrado!")
            print("Título:", contador[0].title())
            print("Autor:", contador[1].title())

       
    if livro_encontrado == False:
        print("Livro não encontrado.")
    
# Exclusão de livro
def excluir_livro():

    pesquisa = input("Digite o título que deseja excluir: ").lower()
        
    livro_encontrado = False

    for contador in biblioteca:
        if contador[0] == pesquisa:
            livro_encontrado = True  
            biblioteca.remove(contador)
            print("Livro excluído!")
        
    if livro_encontrado == False:
        print("Livro não encontrado.")        

# Quatidade de livros
def quantidade_livro():
        print("Quantidade de livros:", len(biblioteca))

while True:

    print("\n=====SISTEMA DE BIBLIOTECA=====")
    print("1 - Cadrastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    #print("4 - Alterar livro")
    print("4 - Excluir livro")
    print("5 - Quantidade de livros")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livro()
    
    elif opcao == "3":
        pesquisar_livro()

    elif opcao == "4":
        excluir_livro()

    elif opcao == "5":
        quantidade_livro()
# Encerramento     
    elif opcao == "6":
        print("Programa encerrado.")
        break
    
    else:
        print("Opção inválida!")

