from math import pi

RAIO= float(input('Insira o raio da esfera:  '))

VOLUME_DA_ESFERA= (4/3)*pi*R**3

ARESTA= float(input('Insira o valor da aresta:  '))

VOLUME_CUBO= ARESTA**3

print('O volume livre que contenha uma esfera inscrita em um cubo é {}'.format(VOLUME_CUBO-VOLUME_DA_ESFERA))