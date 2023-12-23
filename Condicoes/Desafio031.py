from colorama import init
init()
distancia = float(input('Digite a distância da viagem em Km: '))

print('Você está prestes a começar uma viagem de \033[1;33m{}Km\033[m'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('Você vai pagar \033[1;32mR$ {}\033[m'.format(preco))
print('\033[4mTenha uma \033[32mBoa Viagem\033[m!')
