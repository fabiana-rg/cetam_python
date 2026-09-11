
salario_atual = float(input("Qual o valor do salário: "))
reajuste = float(input("Quanto a %  de reajuste: "))

valor_reajuste = salario_atual + (reajuste / 100)
salario_novo = salario_atual + reajuste

print("O reajuste foi de ", reajuste)
print("O valor do novo salario é ", salario_novo) 
