from random import choice

priAluno = input("Digite o nome do Primeiro aluno: ")
segAluno = input("Digite o nome do Segundo aluno: ")
terAluno = input("Digite o nome do Terceiro aluno: ")
quarAluno = input("Digite o nome do Quarto aluno: ")
lista = [priAluno, segAluno, terAluno, quarAluno]
escolhido = choice(lista)

print("O aluno escolhido foi: {}".format(escolhido))
