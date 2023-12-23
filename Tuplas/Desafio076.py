produtos = ('Pão', 2, 
            'Peru', 19.99, 
            'Mochila', 119.99, 
            'Hidratante', 20, 
            'Chocolate', 10.2, 
            'Caderno', 8.50)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='') 
    else:
        print(f'R${produtos[posicao]:>7.2f}')
print('-' * 40)
