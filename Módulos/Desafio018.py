from math import radians, sin, tan, cos

ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang))
print('O ângulo de \033[1;34m{}\033[m tem o \033[4;36mSENO de {:.2f}\033[m'.format(ang, seno))

cosseno = cos(radians(ang))
print('O ângulo de \033[1;34m{}\033[m tem o \033[4;36mCOSSENO de {:.2f}\033[m'.format(ang, cosseno))

tangente = tan(radians(ang))
print('O ângulo de \033[1;34m{}\033[m tem a \033[4;36mTANGENTE de {:.2f}\033[m'.format(ang, tangente))
