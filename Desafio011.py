a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
area = a * l
t = area / 2

print('A sua parede tem dimenções de {}m x {}m e sua área é de {}m²'.format(a, l, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(t))