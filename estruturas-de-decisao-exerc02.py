#ENTRADA DE DADOS

nome_produto = str(input("Nome do produto: "))
quant_disp = int(input("Quantidade dísponivel: "))
print(" ")
#PROCESSAMENTO DE DADOS COM SAIDAS
 
if quant_disp == 0:
    print("Produto esgotado.")
elif quant_disp >= 1 and quant_disp <=5:
    print("Estoque crítico.")
elif quant_disp >= 6 and quant_disp <= 20:
    print("Estoque baixo.")
else:
    print("Estoque normal.")