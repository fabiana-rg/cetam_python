# 1 - Contagem - Faça um programa que mostre os números de 1 até 10 usando while.
""" contador = 1

while contador < 10:
    print(contador,end=", ")
    contador = contador + 1

print(contador, end=".")    """ 
        #saída:  1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

# 2 — Números pares - Faça um programa que mostre os números pares de 2 até 20 usando while.
""" 
contador = 2

while contador <= 20:
    print(contador)
    contador = contador + 2 """
"""
        #saída: 2
                4
                6
                8
                10
                12
                14
                16
                18
                20
                22. """

# 3 — Cadastro - Pergunte quantos alunos serão cadastrados. Para cada aluno, peça o nome e mostre “Aluno cadastrado: nome”. Use while para controlar a quantidade.

qtd_aluno = int(input("Quantos alunos quer cadrastra: "))
contador = 0

while contador < qtd_aluno:
    nome = input("Digite o nome do aluno: ")
    print("Aluno cadastrado.")
    contador = contador + 1

""" enquando contador (que é 0) """

