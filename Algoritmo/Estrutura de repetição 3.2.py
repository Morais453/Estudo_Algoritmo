print('Insira 2 valores os quais o 2 deve ser MAIOR que o primeiro')
n1 = int(input('Insira o valor 1: '))
n2 = int(input('Insira o valor 2: '))
while n1 >= n2:
    n2 = int(input('Insira o valor 2: '))
print('Excelente, o primeiro valor informado foi {} e o segundo {}'.format(n1,n2))