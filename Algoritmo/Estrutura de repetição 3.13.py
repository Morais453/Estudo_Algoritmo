maior = soma = media = 0
cont = 1
while cont < 11:

    n = int(input(f'Insira o valor {cont}: '))

    if n <= 0:
        print('Valor incorreto, insira um valor positivo.')
        continue

    soma += n
    media = soma / cont
    cont += 1

    if n > maior:
        maior = n

print(f'O maior número foi {maior}, a soma entre os números informados foi {soma} e a média foi {media}')
