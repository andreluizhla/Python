extenso =  ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
            'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número: '))
while 0 > num or num > 20:
    print('Tente novamente.', end=' ')
    num = int(input('Digite um número: '))
print(f'Você digitou o número {extenso[num]}')
