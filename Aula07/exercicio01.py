notas = []

for i in range(5):
    nota = float(input(f"Digite nota {i+1}: "))
    notas.append(nota)


for nota in notas:
    print(nota)

print(f"Quantidade de notas na lista: {len(notas)}")

print(f"A maior nota é {max(notas)} e a menor nota é {min(notas)}.")

