v1= float(input('Insira um número:  '))
v2= float(input('Insira um número:  '))
v3= float(input('Insira um número:  '))
v4= float(input('Insira um número:  '))
print('A média entre os 4 valores inseridos é {}'.format((v1+v2+v3+v4)/4))

soma = 0
for i in range(0,4):
    valor = float(input(f'Insira o valor {i+1}: '))
    soma += valor
print(f'A média dos valores inseridos corresponde a {soma/4}')