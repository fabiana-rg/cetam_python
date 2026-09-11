
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro: "))

print( )

print("1-soma")
print("2-subtração")
print("3-multiplicação")
print("4-divisão")
#DEFINIR O TIPO DA VARIAVEL PARA INTEIRO
escolha = int(input("Qual operação: "))

import time
time.sleep(1)

print( )
#CONDICÕES PARA EXECUTAR AS OPERAÇÕES COM BASE NA ESCOLHA
if escolha == 1:
    soma = numero1 + numero2
    print("Resultado", soma)
elif escolha == 2:
    subtracao = numero1 - numero2
    print("Resultado", subtracao)
elif escolha == 3:
    multiplicacao = numero1 * numero2
    print("Resultado", multiplicacao)
elif escolha == 4:
    if numero2 != 0:
        divisao = numero1 / numero2
        print("Resultado", divisao)
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Escolha inexistente")