#exemplo 
""" repetidor = 1
while repetidor == 1:
    print("Ganhou mundial.")
resposta = int(input("Ganhou mundial? sim 1 ou nao 2"))
if resposta == 2:
    print("Tente novamente...")
elif resposta ==1:
    print("Até que fiz...")
    break """

#A estrutura básica do while
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
#saída: 
# 1 
# 2 
# 3 
# 4 
# 5

# While com entrada do usuário
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")
    print("Acesso permitido!")
#saída:
""" Digite a senha: 54
Acesso permitido!
Digite a senha: 565
Acesso permitido!
Digite a senha: 1234
Acesso permitido! """

#while para repetir uma quantidade determinada de vezes
quantidade = int(input("Quantos alunos? "))

contador = 1

while contador <= quantidade:
    nome = input("Digite o nome do aluno: ")
    print("Aluno cadastrado:", nome)
    contador = contador + 1
#saída
""" Quantos alunos? 2
Digite o nome do aluno: Ana
Aluno cadastrado: Ana
Digite o nome do aluno: Caio
Aluno cadastrado: Caio """

#while com menu
opcao = 0

while opcao != 3:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("Cadastro de aluno")
    elif opcao == 2:
        print("Lista de alunos")
    elif opcao == 3:
        print("Saindo...")
    else:
        print("Opção inválida!")
#saída
""" 1 - Cadastrar aluno
2 - Listar alunos
3 - Sair
Escolha uma opção: 1
Cadastro de aluno

1 - Cadastrar aluno
2 - Listar alunos
3 - Sair
Escolha uma opção: 2
Lista de alunos

1 - Cadastrar aluno
2 - Listar alunos
3 - Sair
Escolha uma opção: 3
Saindo... """

#Um exemplo próximo da nossa atividade: cadastro de livros
quantidade = int(input("Quantos livros deseja cadastrar? "))

contador = 1
while contador <= quantidade:
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor: ")

    print("Livro:", titulo)
    print("Autor:", autor)
    
    contador = contador + 1

print("Cadastro finalizado!")
#saída
""" Quantos livros deseja cadastrar? 1
Digite o título do livro: O livro
Digite o autor: Antonio
Livro: O livro
Autor: Antonio
Cadastro finalizado! """

#while + if: repetição com decisão
contador = 1
while contador <= 5:
    idade = int(input("Digite a idade: "))
    
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
    contador = contador + 1
#saída
""" Digite a idade: 18
Maior de idade
Digite a idade: 15
Menor de idade
Digite a idade: 24
Maior de idade
Digite a idade: 12
Menor de idade
Digite a idade: 11
Menor de idade """

#while para validar dados
nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite uma nota de 0 a 10: "))

print("Nota registrada:", nota)
#saída
""" Digite uma nota de 0 a 10: 5
Nota registrada: 5.0 """

