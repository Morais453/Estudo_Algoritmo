b = float(input('Insira o valor da base do terreno:  '))
h = float(input('Insira o valor da altura do terreno:  '))

a= b*h
if a>100:
    print('Terreno grande com área igual a {}'.format(a))
else:
    print(f'Terreno pequeno de área {a}')