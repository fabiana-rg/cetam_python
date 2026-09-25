""" #Declaração de uma função simples, sem parâmentro e sem retorno
def saudacao():
    print("Estudo Python!")
#Chamando a função
saudacao()

#Outra forma de fazer a mesma coisa
#Declarando uma função que irá receber um parâmentro nomeado
def saudacao_com_parametro(recebe_mensagem):
    print(recebe_mensagem)

 #Chamando a função com paramêtro

boas_vindas = "Seja bem vindo ao sistema função!"
saudacao_com_parametro(boas_vindas)  

logout = input("Digite mensagem de despedida: ")
saudacao_com_parametro(logout)
 """
# exemplo

def somar(a, b):
    resultado = a + b
    print(resultado)
somar(10, 5)
