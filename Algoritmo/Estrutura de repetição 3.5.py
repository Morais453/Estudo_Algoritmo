n = int(input('Insira o valor para obter a tabuada: ' ))
while n <=0:
    n = int(input('Valor inserido incorreto, informe apenas números positivos: '))
for c in range(1,11):
    print(f'{n} x {c} = {n*c}')