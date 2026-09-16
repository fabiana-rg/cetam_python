nomes = ["Ana", "Carlos", "João"]

print(nomes[0]) # Ana
print(nomes[2]) # João

print(nomes[-1]) # Maria
print(nomes[-2]) # João

print(len(nomes)) #3

nomes = ["Ana", "Carlos", "João"]
nomes[1] = "Pedro"
print(nomes) # ["Ana", "Pedro", "João"]

nomes.append("Maria") 
print(nomes) # ['Ana', 'Pedro', 'João', 'Maria']

nomes.insert(1, "Lucas")
print(nomes) # ['Ana', 'Lucas', 'Pedro', 'João', 'Maria']

nomes.remove("Pedro")
print(nomes) # ['Ana', 'Lucas', 'João', 'Maria']

nomes.pop(0)
print(nomes) # ['Lucas', 'João', 'Maria']

"""
lista.append(valor)
lista.insert(posição, valor)
lista.remove(valor)
lista.pop(posição)
len(lista)
"""
for nome in nomes:
    print(nome)
"""
Lucas
João
Maria"""

idades = [16, 17, 18, 20]
for idade in idades:
    print(idade)
"""
16
17
18
20"""    

notas = [7, 8, 6, 9]
soma = 0
for nota in notas:
    soma = soma + nota
    print(soma)
"""
7
15
21
30
"""
for indice, nome in enumerate(nomes):
    print(indice, nome)
"""
0 Lucas
1 João
2 Maria
"""
nomes = ["Ana", "Carlos", "João"]
nome = "Carlos"
if nome in nomes:
    print("Nome encontrado!")
else:
    print("Nome não encontrado.")

# Nome encontrado!

# exemplo prático
produtos = ["Teclado", "Mouse", "Monitor", "Headset"]

for produto in produtos:
    print(produto)
"""
Teclado
Mouse
Monitor
Headset
"""    
produtos.append("Webcam")
print(produtos) # ['Teclado', 'Mouse', 'Monitor', 'Headset', 'Webcam']

produtos[1] = "Mouse sem fio"
print(produtos) # ['Teclado', 'Mouse sem fio', 'Monitor', 'Headset', 'Webcam']

if "Monitor" in produtos:
    print("Produto encontrado!") # Produto encontrado!

produtos.remove("Headset")
print(produtos) # ['Teclado', 'Mouse sem fio', 'Monitor', 'Webcam']