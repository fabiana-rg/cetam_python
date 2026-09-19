#EXERCICIO DE FIXAÇÃO

# 1 - Contagem - Faça um programa que mostre os números de 1 até 10 usando while.
""" contador = 1

while contador < 10:
    print(contador,end=", ")
    contador = contador + 1

print(contador, end=".")    """ 
        #saída:  1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

# 2 — Números pares - Faça um programa que mostre os números pares de 2 até 20 usando while.
""" 
contador = 2

while contador <= 20:
    print(contador)
    contador = contador + 2 """
"""
        #saída: 2
                4
                6
                8
                10
                12
                14
                16
                18
                20
                22. """

# 3 — Cadastro - Pergunte quantos alunos serão cadastrados. Para cada aluno, peça o nome e mostre “Aluno cadastrado: nome”. Use while para controlar a quantidade.
""" 
qtd_aluno = int(input("Quantos alunos quer cadrastra: "))
contador = 0

while contador < qtd_aluno:
    nome = input("Digite o nome do aluno: ")
    print("Aluno cadastrado.")
    contador = contador + 1 """

""" enquando contador (que é 0) """
""" 
saída:  Quantos alunos quer cadrastra: 3
        Digite o nome do aluno: Ana 
        Aluno cadastrado.
        Digite o nome do aluno: Fabio
        Aluno cadastrado.
        Digite o nome do aluno: Fabiana
        Aluno cadastrado. """

#EXERCICIO DE APLICAÇÃO

# 4 - Menu simples - Crie um menu com as opções: 1 — Cadastrar livro; 2 — Listar livros; 3 — Sair. O menu deve continuar aparecendo até o usuário escolher 3.
""" 
opcao = 0

while opcao != 3:
    
    print("="*14)
    print("     MENU")
    print("="*14)
    print("1 - Cadrastrar livro.")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        print("\nLivro cadrastrado.")
    elif opcao == 2:
        print("\nLista de livros.")
    elif opcao == 3:
        print("\nSaindo........\n")
    else:
        print("Opção inválida")  """
        
""" saída:
==============
     MENU
==============
1 - Cadrastrar livro.
2 - Listar livros
3 - Sair
Digite a opção: 1

Livro cadrastrado.
==============
     MENU
==============
1 - Cadrastrar livro.
2 - Listar livros
3 - Sair
Digite a opção: 2

Lista de livros.
==============
     MENU
==============
1 - Cadrastrar livro.
2 - Listar livros
3 - Sair
Digite a opção: 3

Saindo........
"""

# 5 — Validação -Peça uma idade. Enquanto a idade for menor que 0 ou maior que 120, informe que o valor é inválido e peça novamente.
""" 
idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 120:
    if idade < 0 or idade > 120:
        print("Valor inválido!")
    
    idade = int(input("Digite sua idade novamente: "))  """
    
# 6 - Senha - Crie um programa que peça uma senha até que o usuário digite a senha correta. Ao acertar, mostre “Acesso permitido!”.
"""     
senha = ""

while senha != "gato16#":
    senha = input("Digite a senha: ")
    if senha != "gatos16#":
        print("Senha inválida.")
    
    
print("Senha válida!")
 """
""" saída: 
cicio-while.py"
Digite a senha: 1234
Senha inválida.
Digite a senha: abcd 
Senha inválida.
Digite a senha: gato16#]
Senha inválida.
Digite a senha: gato16# 
Senha inválida.
Senha válida!
"""

# DESAFIO - CADRASTRATO DE LIVROS

""" Crie um programa que pergunte quantos livros o usuário deseja cadastrar. Para cada livro, peça:
• Título
• Autor
• Ano de publicação
Depois de cada cadastro, mostre os dados informados. Ao final, mostre “Cadastro finalizado!”. Use while para controlar a quantidade de cadastros.
 """
 
""" qtd_livros = int(input("Quantos livros deseja cadastrar: "))
 
contador = 1

while contador <= qtd_livros:
        
    titulo = input("Título do livro: ")
    autor = input("Nome do autor: ")
    ano_publicacao = input("Ano de publicação: ")

    print("===Dados do Livro===")    
    print(f"Título: {titulo}") 
    print(f"Autor: {autor}")
    print(f"Ano de publicação: {ano_publicacao}")  
    contador += 1

print("Cadrastro finalizado!") """
        