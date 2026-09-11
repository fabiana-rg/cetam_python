#ENTRADA DE DADOS
nome_do_usuario = str(input("Nome do usuário: "))
print(" ")
print("Classifique seu problema: ")
print("1 - Indisponibilidade total do sistema")
print("2 - Sistema funcionando, mas com lentidão ou erros")
print("3 - Problema que não impede o trabalho")
print("4 - Outros problemas")
print(" ")
tipo_problema = int(input("Tipo de problema: "))
print(" ")
print("Classifique há quanto tempo o problema persiste: ")
print("1 - Há 1 a 3 dias.")
print("2 - Há 4 a 6 dias.")
print("3 - Há 7 a 9 dias.")
print("4 - Há 10 a 12 dias.")
print(" ")
tempo_problema = int(input("Tempo que problema está  ocorrendo: "))
print(" ")


# PROCESSAMENTO DE DADOS
problema  =  " "
prioridade = " "


if tipo_problema == 1:
    problema = "Indisponibilidade total do sistema"
    prioridade = "Crítica"

elif tipo_problema == 2 and tempo_problema == 3 or tempo_problema == 4:
    problema = "Sistema funcionando, mas com lentidão ou erros"
    prioridade = "Crítico"
elif tipo_problema == 2 and tempo_problema == 1 or tempo_problema == 2:
    problema = "Sistema funcionando, mas com lentidão ou erros"
    prioridade = "Alto"

elif tipo_problema == 3 and tempo_problema == 3 or tempo_problema == 4:
    problema = "Problema que não impede o trabalho"
    prioridade = "Alto"

elif tipo_problema == 3 and tempo_problema == 1 or tempo_problema == 2:
    problema = "Problema que não impede o trabalho"
    prioridade = "Média"

else:
    problema = "Outros problemas"
    prioridade = "Baixa"

# SAÍDA DE DADOS
print("=============================================")
print("RESULTADO: ")
print(f"Nome do usuário: {nome_do_usuario}")
print(f"Problema informado: {problema}")
print(f"Prioridade atribuída: {prioridade}")
print("=============================================")
















""" 
if tipo_problema == 1:
    print(f"Nome do usuário: {nome_do_usuario}")
    print(f"Problema informado: {tipo_problema} - Indisponibilidade total do sistema")
    print(f"Prioridade atribuída: Crítica.")    
elif tipo_problema == 2:
    print(f"Nome do usuário: {nome_do_usuario}")
    print(f"Problema informado: {tipo_problema} - Sistema funcionando, mas com lentidão ou erros")
    print(f"Prioridade atribuída: Alta.")
elif tipo_problema == 3:
    print(f"Nome do usuário: {nome_do_usuario}")
    print(f"Problema informado: {tipo_problema} - Problema que não impede o trabalho")
    print(f"Prioridade atribuída: Média.")
elif tipo_problema == 4:
    print(f"Nome do usuário: {nome_do_usuario}")
    print(f"Problema informado: {tipo_problema} - Outros problemas ")
    print(f"Prioridade atribuída: Baixa.")

 """