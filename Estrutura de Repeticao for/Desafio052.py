num = int(input('Digite um número: '))
primo = True

for c in range(2, 8):
    if num != 2 and num != 3:
        if num % c == 0:
            primo = False

if primo:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
