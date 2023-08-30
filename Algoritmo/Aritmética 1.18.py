p1 = float(input('Digite o valor do produto:  '))
p2 = float(input('Digite o valor do produto:  '))
p3 = float(input('Digite o valor do produto:  '))
p4 = float(input('Digite o valor do produto:  '))
p5 = float(input('Digite o valor do produto:  '))

Total = p1+p2+p3+p4+p5
print(f'Valor total a pagar R${Total:0.2f}')
pg= float(input('Insira o valor pago:  '))
print(f'O troco a ser devolvido é R${pg-Total:0.2f}')