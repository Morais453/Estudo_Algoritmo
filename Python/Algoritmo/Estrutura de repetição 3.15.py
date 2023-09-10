maior = menor = soma = media = POSITIVOS = NEGATIVOS = 0
cont = 1
VALOR_MOSTRAR = int(input('Quantos valores você quer somar?'))+1
while True:
    while cont < VALOR_MOSTRAR:

        NUMERO = int(input(f'Insira o valor {cont}[menor igual a 20]: '))
        print('-' * 40)
        if NUMERO > 20:
            print('Valor incorreto, insira um valor válido[menor igual a 20].')
            continue

        soma += NUMERO
        media = soma / cont

        if NUMERO > maior or cont == 1:
            maior = NUMERO

        if NUMERO < menor or cont == 1:
            menor = NUMERO

        if NUMERO > 0:
            POSITIVOS += 1
        if NUMERO < 0:
            NEGATIVOS += 1
        cont += 1
    print(f'O maior número foi {maior} e o menor foi {menor}.'
          f'\nDos {cont-1} valores inseridos:'
          f'\n{(POSITIVOS/(cont-1))*100:.1f}% deles são positivos'
          f'\n{(NEGATIVOS/(cont-1))*100:.1f}% são negativos'
          f'\na soma entre os números informados foi {soma} e a média foi {media}')

    print('-'*40)
    print('Quantos valores você ainda quer somar?')
    NUMERO = int(input('Insira quantos ainda quer: '))
    print('-' * 40)
    if NUMERO == 0:
        break
    else:
        VALOR_MOSTRAR += NUMERO
print('Programa encerrado volte sempre')
