maior = menor = soma = media = P = N = 0
cont = 1
v = 11
while True:
    while cont < v:

        n = int(input(f'Insira o valor {cont}: '))
        print('-' * 40)
        if n > 20:
            print('Valor incorreto, insira um valor positivo.')
            continue

        soma += n
        media = soma / cont

        if n > maior:
            maior = n

        if n < menor or cont == 1:
            menor = n

        if n > 0:
            P += 1
        if n < 0:
            N += 1
        cont += 1
    print(f'O maior número foi {maior} e o menor foi {menor}.\nDos {cont-1} números {P} deles são positivos e {N} são negativos\na soma entre os números informados foi {soma} e a média foi {media}')

    print('-'*40)
    print('Quantos valores você ainda quer somar?')
    n = int(input('Insira quantos ainda quer: '))
    print('-' * 40)
    if n == 0:
        break
    else:
        v += n
print('Programa encerrado volte sempre')