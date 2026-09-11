""" Solicite 4 notas, uma por vez.
Ao final, calcule e mostre a média.
Defina as variáveis antes de escrever o código. """

soma_nota = 0
qtd_notas = 4

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    soma_nota += nota

media = soma_nota / qtd_notas

print(f"media final da notas: {media:.2f}")


#NÃO TERMINADO
    