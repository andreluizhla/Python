from colorama import init
init()
entrada = input("Digite algo: ")

print("Tipo do primitivo: \033[1;34m{}\033[m".format(type(entrada)))
print("Só tem espaços? \033[1;36m{}\033[m".format(entrada.isspace()))
print("É numérico? \033[1;35m{}\033[m".format(entrada.isnumeric()))
print("É alfabético? \033[1;31m{}\033[m".format(entrada.isalpha()))
print("É alfanumérico? \033[1;33m{}\033[m".format(entrada.isalnum()))
print("Só tem maiúsculas? \033[1;32m{}\033[m".format(entrada.isupper()))
print("Só tem minúsculas? \033[1;37m{}\033[m".format(entrada.islower()))
print("Está capitalizada? \033[7;30;47m{}\033[m".format(entrada.istitle()))
