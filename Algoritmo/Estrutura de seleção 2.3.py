v1 = float(input('Insira um valor: '))
v2 = float(input('Insira outro: '))

if v1 == v2:
    print('-'*36)
    print('Os valores identificados são iguais!')
    print('-' * 36)
elif v1 > v2:
    print('O valor ',v1,' é maior')
else:
    print('O valor ', v2, ' é maior')