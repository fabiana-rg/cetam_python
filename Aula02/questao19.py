
idade = int(input("Qual a sua idade: "))

resposta = input("Possui curso técnico (sim/não): ")
curso = (resposta == "sim")

if idade >= 18 and curso == True:
    print("Pode trabalhar e Possui curso técnico.")
else:
    print("Sem requisitos mínimo.")