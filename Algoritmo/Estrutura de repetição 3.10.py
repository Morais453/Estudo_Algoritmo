soma = 0
while True:
    n = int(input("Digite um valor para N (positivo e menor que 100): "))
    if 0 < n < 100:
        for i in range(1, n+1):
            sequencia = i**2 + 1
            #print(sequencia)
            soma += sequencia
        print(f"A soma dos primeiros {n} valores da sequência é: {soma}")
        break
    else:
        print("Valor fora do intervalo permitido. Digite um valor positivo menor que 100.")
