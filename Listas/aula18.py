dados = ['nome', 'idade']
pessoas = list()
for c in range(0, 3):
    dados[0] = input('Digite seu nome: ')
    dados[1] = int(input('Digite a sua idade: '))
    pessoas.append(dados[:])
    #dados.clear()
print(pessoas)


#pessoas = [[['Andre', 'Luiz', 'Hlatchuk'], 16], [['Maisa', 'Leticia', 'Hlatchuk'], 12]]
#print(pessoas[0][0][2])


#lista = [[4, 3, 1, 5], [1, 7, 2, 5, 8]]
#lista.sort() pega o primeiro valor e ordena
#lista[0].sort() pega os valores da lista[0] e ordena
#print(lista)