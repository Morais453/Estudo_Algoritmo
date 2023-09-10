nome = []
idade = []
Quant_Mulher = 0
for c in range(0,20):
    n = input('Informe seu nome: ').upper().strip()
    i = input('Informe sua idade: ').strip()
    s = input('Informe seu sexo[M/F]: ').upper().strip()
    if s in 'F':
        nome.append(n)
        idade.append(i)
        Quant_Mulher += 1
if Quant_Mulher > 0:
    print('As mulheres listadas são: ')
    for i in range(Quant_Mulher):
        print(f'{nome[i]} com {idade[i]} anos')
else:
    print('Nenhuma mulher foi listada')