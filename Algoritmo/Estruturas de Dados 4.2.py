l = []
for i in range(0,20):
    n = int(input(f'Insira o valor {i+1}: '))
    l.append(n)

c= int(input('Insira o valor que irá multiplicar os outros números: '))

for o in range(0,20):
    l[o] = l[o] * c
print(l)