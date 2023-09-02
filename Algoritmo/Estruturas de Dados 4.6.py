nome = []
idade = []
sexo = []
cont= 0
for c in range(0,10):
    nome_inserido = input('Informe seu nome: ').upper().strip()
    idade_inserida = int(input('Informe sua idade: '))
    genero = input('Informe seu sexo[M/F]: ').upper().strip()
    if idade_inserida >= 18:
        nome.append(nome_inserido)
        idade.append(idade_inserida)
        if genero in 'M':
            sexo.append('Homem')
        if genero in 'F':
            sexo.append('Mulher')
        cont += 1
if cont > 0:
    print('As pessoas maiores de idade inseridas são: ')
    for i in range(cont):
        print(f'{nome[i]}, {sexo[i]} de {idade[i]} anos')
    print(f'Foram listadas um total de {cont} pessoas maiores de idade')
else:
    print('Das pesoas inseridas, nenhuma é maior de idade')