maior = menor = soma = media = P = N = 0
cont = 1
while cont < 11:

    n = int(input(f'Insira o valor {cont}: '))

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