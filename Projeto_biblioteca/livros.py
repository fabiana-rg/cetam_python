import os

livros = []

# Cadrastro
def Cadastrar_livro():
    titulo = input("Digite o título: ").lower()
    autor = input("Digite o autor: ").lower()

    livros.append([titulo, autor])

    print("Livro cadastrado!")

# Listagem de livro
def Listar_livro():
    print("\n--- LIVROS CADASTRADOS ---")

    if len(livros) == 0:
        print("Nenhum livro cadrastrado ainda.")

    for contador in livros:
        print("Título:", contador[0].title())
        print("Autor:", contador[1].title())
        print("")

# Pesquisa de livro
def Pesquisar_livro():
    
    pesquisa = input("Digite o título que deseja pesquisar: ").lower() 
    livro_encontrado = False 

    for contador in livros:
        if contador[0] == pesquisa:
            livro_encontrado = True  
            print("Livro encontrado!")
            print("Título:", contador[0].title())
            print("Autor:", contador[1].title())

       
    if livro_encontrado == False:
        print("Livro não encontrado.")
    
# Exclusão de livro
def Excluir_livro():

    pesquisa = input("Digite o título que deseja excluir: ").lower()
        
    livro_encontrado = False

    for contador in livros:
        if contador[0] == pesquisa:
            livro_encontrado = True  
            livros.remove(contador)
            print("Livro excluído!")
        
    if livro_encontrado == False:
        print("Livro não encontrado.")        

# Quatidade de livros
def Quantidade_livro():
        print("Quantidade de livros:", len(livros))

def Menu_livros():
    while True:
        os.system("cls")

        print("\n===== SISTEMA DE LIVROS =====")
        print("1 - Cadrastrar livro")
        print("2 - Listar livros")
        print("3 - Pesquisar livro")        
        print("4 - Excluir livro")
        print("5 - Quantidade de livros")
        print("6 - Voltar ao menu anterior")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            Cadastrar_livro()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "2":
            Listar_livro()
            input("\nPressione ENTER para voltar ao menu...")
        
        elif opcao == "3":
            Pesquisar_livro()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "4":
            Excluir_livro()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "5":
            Quantidade_livro()
            input("\nPressione ENTER para voltar ao menu...")
    # Encerramento     
        elif opcao == "6":
            break
        
        else:
            print("Opção inválida!")
            input("\nPressione ENTER para voltar ao menu...")