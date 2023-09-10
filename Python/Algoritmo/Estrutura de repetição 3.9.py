n1 = n2 = n3 = 1

cont = 3
print(f'{n1} => {n2} => {n3}', end=' => ')
while cont < 20:
    soma = n1+n2+n3
    cont += 1
    print(soma, end=" => ")

    n1 = n2
    n2 = n3
    n3 = soma
