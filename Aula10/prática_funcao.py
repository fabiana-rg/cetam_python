#TESTE
"""
def calcular_total(preco, quantidade):
    return preco * quantidade
resultado = calcular_total(20, 4)
print(resultado) """

# Desafio 2: crie cadastrar_livro() para adicionar um livro à lista.
biblioteca = []

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")

    livros = [titulo, autor]
    biblioteca.append(livros)

cadastrar_livro()

# Desafio 3: crie listar_livros() para exibir todos os registros.
def listar_livros():
    for contador in biblioteca:
        print(contador[0], "-", contador[1])

listar_livros()

# Desafio 4: crie buscar_livro() para procurar um título na lista.
def buscar_livro():
    busca = input("Digite o título para pesquisar: ")

    for contador in biblioteca:
        if contador[0] == busca:
            print("Livro encontrado")
            print(f"Título: {contador[0]}, Autor: {contador[1]}")

buscar_livro()

# Desafio 5: crie remover_livro() para retirar um registro da lista.

def remover_livro():
    titulo = input("Digite o titulo do livro que deseja remover: ")
    biblioteca.remove(titulo)

remover_livro