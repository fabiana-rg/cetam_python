biblioteca = []

while True:

    print("\n=====SISTEMA DE BIBLIOTECA=====")
    print("1 - Pesquisar livro")
    print("2 - Cadrastrar livro")
    print("3 - Listar livros")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")
#BUSCA
    if opcao == "1":
        pesquisa = input("Pesquisar livro: ")
        encontrado = False

        for livro in biblioteca:
            if livro["Código"] == pesquisa:
                print("Livro encontrado")
                encontrado = True
                break




    
#CHAMADA 
    elif opcao == "2":        
        codigo = int(input("Código do livro: "))
        
        existe = False
        
        for livro in biblioteca:
            if livro[0] == codigo:
                existe = True
        
        if existe:
            print("Código já cadasdrado!")
        else:
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano_publicacao = int(input("Ano de publicação: "))

            livro_adicionado = {"Título": titulo, "Autor": autor, "Ano": ano_publicacao}
            biblioteca.append(livro_adicionado)

            print("Livro adicionado com sucesso!")

#EDIDIÇÃO DA BIBLIOTECA       
    elif opcao == "3":
        print(biblioteca)   

    elif opcao == "4":
        pass

    elif opcao == "5":
        pass
    elif opcao == "6":
        break
    else:
        print("Opção inválida!")

