#ENTRATADA DE Dados
nome_cliente = str(input("Nome:"))
velocidade = float(input("Velocidade contratada em Mbps: "))

#PROCESSAMENTO DE DADOS
if velocidade < 50:
    plano = "Plano Básico"
elif velocidade >= 50 and velocidade <= 199:
    plano = "Plano Intermediário"
elif velocidade >= 200 and velocidade <= 499:
    plano = "Plano Avançado"
else:
    plano = "Plano Ultra"

#SAIDA DE DADOS
print(" ")
print("--- Resumo do Cliente ---")
print(f"Nome do cliente: {nome_cliente}")
print(f"Velocidade contratada: {velocidade} Mbps")
print(f"Classificação: {plano}")
