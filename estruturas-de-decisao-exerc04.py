#ENTRADA DE DADOS

nome_aluno = str(input("Nome: "))
idade = int(input("Idades:"))
cadrastro = str(input("Possui cadrastro, (sim ou não): "))


#PROCESSAMENTO DE DADOS
if idade >= 18 and cadrastro == "sim":
    situacao = "Acesso permitido."
elif idade < 17  or idade > 14 and cadrastro == "sim":
    situacao = "Acesso permitido."
elif idade < 14 and cadrastro == "sim":
    situacao = "Acesso permitido somente com acompanhanto."
else:
    situacao = "Acesso negado"

#SAIDA DE DADOS
print(" ")
print(f"Nome: {nome_aluno}")
print(f"Situação de acesso: {situacao}")