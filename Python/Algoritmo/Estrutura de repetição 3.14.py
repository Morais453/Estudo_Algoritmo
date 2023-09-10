MAIOR = MENOR = soma = media = POSITIVO = NEGATIVO = 0
cont = 1
while cont < 11:

    NUMERO = int(input(f'Insira o valor {cont}: '))

    if NUMERO > 20:
        print('Valor incorreto, insira um valor positivo.')
        continue

    soma += NUMERO
    media = soma / cont

    if NUMERO > MAIOR:
        MAIOR = NUMERO

    if NUMERO < MENOR or cont == 1:
        MENOR = NUMERO

    if NUMERO > 0:
        POSITIVO += 1
    if NUMERO < 0:
        NEGATIVO += 1
    cont += 1
print(f'O MAIOR número foi {MAIOR} e o MENOR foi {MENOR}'
      f'\nDos números {(POSITIVO/(cont-1))*100}% deles são positivos e {(NEGATIVO/(cont-1))*100}% são negativos'
      f'\nA soma entre os números informados foi {soma} e a média foi {media}')
