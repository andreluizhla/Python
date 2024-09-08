from time import sleep
boletim = list()

while True:
    nome = input('Nome: ').strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    
    notas = [nota1, nota2]
    boletim.append([nome, notas, media])
    
    confirmacao = input('Deseja continuar? [S/N] ').strip()[0]
    if confirmacao in 'Nn':
        break

print('-=' * 22)
print(f'No. {'NOME': <18} MÉDIA')
print('-' * 30)
for c in range(0, len(boletim)):
    print(f'{c: <4}{boletim[c][0]: <19} {boletim[c][2]:.1f}')

print('-' * 30)

mostra_nota = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
while mostra_nota != 999:
    print(f'Notas de {boletim[mostra_nota][0]} são {boletim[mostra_nota][1]}')
    print('-' * 30)
    mostra_nota = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))

print('FINALIZANDO...')
sleep(5)
print('<<< VOLTE SEMPRE >>>')
