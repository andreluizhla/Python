from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year

idade = ano - nascimento

print('Você têm \033[4;33m{} anos\033[m de idade em {}'.format(idade, ano))

print('Então você se encaixa na categoria: ', end='')
if idade <= 9:
    print('\033[34mMIRIM\033[m')
elif idade <= 14:
    print('\033[34mINFANTIL\033[m')
elif idade <= 19:
    print('\033[34mJUNIOR\033[m')
elif idade == 20:
    print('\033[34mSÊNIOR\033[m')
else:
    print('\033[34mMASTER\033[m')
