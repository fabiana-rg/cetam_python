""" 
- Mostre todos os múltiplos de 3 entre 1 e 30.
- Pense em como o range() pode ajudar.
- Use uma condição para selecionar os valores. """

for numero in range(1, 31):
    if numero % 3 == 0:
        print(numero)

