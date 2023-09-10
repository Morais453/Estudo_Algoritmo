import math
x = int(input('Digite o valor da base:  '))
y= int(input('Agora diga o expoente:  '))
exp= x**y
print(f'{x} elevado a  {y} é igual a {exp}')
print('log de {} na base {} é {}'.format(exp,x,math.log(exp, x)))
