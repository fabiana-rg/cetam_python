livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
   
    # Alteração:Adicionado a opção 5 com nova opção no MENU
    print("5 - Quantidade de livros")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

# Cadastro de livro
    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

# Listagem de livro
    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])

# Pesquisa de livro
    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")
        #Alteração: Variável para mostrar se o livro existe na lista
        livro_encontrado = False 

        for contador in livros:
            if contador[0] == pesquisa:
                livro_encontrado = True  # Alteração: Validar se o livro for encontrado
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
        # Alteração: If para mostrar o livro que não encontrado
        if livro_encontrado == False:
            print("Livro não encontrado.")
    
# Exclusão de livro
    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        # Alteração: Variável para mostrar se o livro existe na lista
        livro_encontrado = False

        for contador in livros:
            if contador[0] == pesquisa:
                livro_encontrado = True  # Alteração: Validar se o livro for encontrado
                livros.remove(contador)
                print("Livro excluído!")
        # Alteração: If para mostrar o livro que não encontrado
        if livro_encontrado == False:
                    print("Livro não encontrado.")        

# Alteração: Adicionado a opção para mostrar a quantidade de livros na lista com len()
# Quatidade de livros
    elif opcao == "5":

        print("Quantidade de livros:", len(livros))

# Encerramento 
    elif opcao == "6":

        print("Programa encerrado.")
        break
    
    else:

        print("Opção inválida!")