from random import choice

priAluno = input("Digite o nome do Primeiro aluno: ")
segAluno = input("Digite o nome do Segundo aluno: ")
terAluno = input("Digite o nome do Terceiro aluno: ")
quaAluno = input("Digite o nome do Quarto aluno: ")
lista = [priAluno, segAluno, terAluno, quaAluno]
escolhido = choice(lista)

print("O aluno escolhido foi: \033[4;33m{}\033[m".format(escolhido))
