p = float(input('Insira seu peso:  '))
s = int(input('Informe seu sexo, 0 para masculino e 1 para feminino:  '))
h = float(input('Informe sua altura:  '))
if s == 0:
    G= False
if s == 1:
    G= True
imc = p / h**2
print(f'Seu IMC é {imc} {s}')
if G == True:
    if imc < 19:
        print('Ta abaixo do peso irmã')
    elif 19<=imc<24:
        print('Tá na média')
    else:
        print('A irmã ta pesada ein')
if G == False:
    if imc < 20:
        print('Famoso peso pena kkkkk')
    elif 20<= imc <25:
        print('Peso certin né parça')
    else:
        print('Famoso peso pesado KKKKK')