expressao = str(input('Digite a expressão: '))
exp = list()
for n in range(0, len(expressao)):
    exp.append(expressao[n])
cont = 0
for c in range(0, len(exp)):
    if '(' in exp[c] or ')' in exp[c]:
        cont += 1
if cont % 2 == 0:
    print('A expressão é válida')
else:
    print('Essa expressão não é válida')
