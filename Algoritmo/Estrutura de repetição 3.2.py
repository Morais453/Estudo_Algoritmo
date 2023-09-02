print('Insira 2 valores os quais o segundo deve ser MAIOR que o primeiro')

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

while n1 >= n2:
    print('O segundo valor tem que ser maior que o primeiro')
    n2 = int(input('Insira o segundo valor novamente: '))

print(f'Excelente, o primeiro valor informado foi {n1} e o segundo {n2}')