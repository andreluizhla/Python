serieA = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 
          'Botafogo', 'Bragantino', 'Fluminence', 'Athlético-PR', 
          'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 
          'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 
          'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('BRASILEIRÃO SÉRIE A 2023')
print('-=-' * 20)
print(f'Os 5 primeiros colocados são: {serieA[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos colocados são: {serieA[-4:]}')
print('-=-' * 20)
print(f'Os times em ordem alfabética: {sorted(serieA)}')
print('-=-' * 20)
print(f'O Vasco da Gama está na {serieA.index('Vasco da Gama') + 1}ª posição')
