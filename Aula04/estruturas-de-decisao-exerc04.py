#ENTRADA DE DADOS

nome_aluno = str(input("Nome: "))
idade = int(input("Idade: "))
cadastro = str(input("Possui cadastro, (sim ou não): "))


#PROCESSAMENTO DE DADOS
if idade >= 18 and cadastro == "sim":
    situacao = "Acesso permitido."
elif idade < 14 and cadastro == "sim":
    situacao = "Acesso permitido somente com acompanhamento."
elif idade <= 17  or idade >= 14 and cadastro == "sim":
    situacao = "Acesso permitido."
else:
    situacao = "Acesso negado."

#SAIDA DE DADOS
print(" ")
print(f"Nome: {nome_aluno}")
print(f"Situação de acesso: {situacao}")