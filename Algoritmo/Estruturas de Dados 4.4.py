vetor = []
n = int(input('Quantos valores você quer inserir(no máximo 20)? '))
while n<1 or n>20:
    print("Quantidade inválida. Escolha entre 1 e 20.")
    n = int(input('Quantos valores você quer inserir: '))

for i in range(n):
    valor = int(input(f"Digite o valor {i + 1}: "))
    vetor.append(valor)

while True:
    numero = int(input("Digite um número para consultar sua posição: "))

    for i in range(len(vetor)):
        if vetor[i] == numero:
            print(f'Número {numero} foi encontrado na posiçção {i} do vetor')
        if (i+1 == len(vetor)) and (vetor[i] != numero):
            print('Valor não encontrado')

    continuar = input('Deseja consinuar[S/N]').upper()
    if continuar != 'S':
        break