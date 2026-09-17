produtos = []

for i in range(6):
    produto = input(f"Digite o {i+1}º produto: ")
    produtos.append(produto)

for indice, produto in enumerate(produtos):
    print(f"{indice} - {produto}")

"""
for produto in produtos:
    print(produto)"""

pesquisa = input("Digite o nome do produto: ").lower()

for pesquisa in produtos:
    print("Produto encontrado!")
else:
    print("Não encotrado!")

print(f"Quantidade de produtos cadrasytados: {len(produtos)}")

#desafio

remova = input("Digite um produto pra remover da lista: ")

produtos.remove(remova)

print(produtos)
