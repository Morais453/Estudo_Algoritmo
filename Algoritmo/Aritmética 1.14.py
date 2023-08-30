from math import pi

R= float(input('Insira o raio da esfera:  '))

VE= (4/3)*pi*R**3

A= float(input('Insira o valor da aresta:  '))

VC= A**3

print('O volume livre que contenha uma esfera inscrita em um cubo é {}'.format(VC-VE))