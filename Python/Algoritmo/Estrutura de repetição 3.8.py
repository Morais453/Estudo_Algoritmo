CONTADOR = 3
#n = int(input('Quantos números da sequência Fibonacci você quer exibir:'))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end=' -> ')
while CONTADOR <= 30:
    soma = n1 + n2
    print(f'{soma}', end=' -> ')
    n1 = n2
    n2 = soma
    CONTADOR += 1
print('Fim')
