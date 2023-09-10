from statistics import geometric_mean
n1= int(input('Informe o primeiro valor: '))

n2= int(input('Informe o segundo valor: '))

valores= [n1 , n2]

mg= geometric_mean(valores)

print(mg)

VALOR_1 = int(input('Informe o primeiro valor: '))
VALOR_2 = int(input('Informe o segundo valor: '))
MEDIA_GEOMETRICA = (VALOR_1*VALOR_2)**(1/2)
print(f'A média geométrica dos valores inseridos é {MEDIA_GEOMETRICA}')