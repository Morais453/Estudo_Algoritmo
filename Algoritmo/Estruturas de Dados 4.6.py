nome = []
idade = []
sexo = []
cont= 0
for c in range(0,10):
    n = input('Informe seu nome: ').upper().strip()
    i = int(input('Informe sua idade: '))
    s = input('Informe seu sexo[M/F]: ').upper().strip()
    if i >= 18:
        nome.append(n)
        idade.append(i)
        if s in 'M':
            sexo.append('Homem')
        if s in 'F':
            sexo.append('Mulher')
        cont += 1
if cont > 0:
    print('As pessoas maiores de idade inseridas são: ')
    for i in range(cont):
        print(f'{nome[i]}, {sexo[i]} de {idade[i]} anos')
    print(f'Foram listadas um total de {cont} pessoas maiores de idade')
else:
    print('Das pesoas inseridas, nenhuma é maior de idade')