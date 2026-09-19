biblioteca = []

while True:

    print("\n=====SISTEMA DE BIBLIOTECA=====")
    print("1 - Cadrastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Sair")

    opcao = input("Escolha uma opação: ")
    
#cadastrar

    if opcao == "1":
        
        codigo = int(input("Código do livro: "))
        
        existe = False
        
        for livro in biblioteca:
            if livro[0] == codigo:
                existe = True
        
        if existe:
            print("Código já cadasdrado!")
        