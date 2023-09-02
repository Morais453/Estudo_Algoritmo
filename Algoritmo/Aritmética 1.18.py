p1 = float(input('Digite o valor do produto:  '))
p2 = float(input('Digite o valor do produto:  '))
p3 = float(input('Digite o valor do produto:  '))
p4 = float(input('Digite o valor do produto:  '))
p5 = float(input('Digite o valor do produto:  '))

Total = p1+p2+p3+p4+p5
print(f'Valor total a pagar R${Total:0.2f}')
pg= float(input('Insira o valor pago:  '))
print(f'O troco a ser devolvido é R${pg-Total:0.2f}')

#V2
TOTAL = 0
for c in range(0,5):
    Valor = float(input(f'Insira o valor do produto {c+1}'))
    TOTAL += Valor
print(f'Valor total a pagar R${TOTAL:0.2f}')
PAGAMENTO= float(input('Insira o valor pago:  '))
print(f'O troco a ser devolvido é R${PAGAMENTO-TOTAL:0.2f}')