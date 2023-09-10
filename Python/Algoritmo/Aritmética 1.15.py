dolar = float(input('Diga o valor em dolar a ser convertido em real: '))

print(f'O valor inserido de US${dolar} na cotação para o real corresponde a R${dolar*4.85:0.2f}')

#V2
from forex_python.converter import CurrencyRates

c = CurrencyRates()

dolar = float(input('Diga o valor em dolar a ser convertido em real: '))

Reais = c.convert("USD", "BRL", dolar)

print(f'O valor inserido de US${dolar} na cotação para o real corresponde a R${Reais:0.2f}')