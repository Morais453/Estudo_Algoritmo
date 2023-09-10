PESO = float(input('Insira seu peso:  '))
SEXO = int(input('Informe seu sexo, 0 para masculino e 1 para feminino:  '))
ALTURA = float(input('Informe sua altura:  '))
if SEXO == 0:
    G= False
if SEXO == 1:
    G= True
imc = PESO / ALTURA**2
print(f'Seu IMC é {imc}')
if G == True:
    if imc < 19:
        print('Abaixo do peso')
    elif 19<=imc<24:
        print('Peso adequado')
    else:
        print('Acima do peso')
if G == False:
    if imc < 20:
        print('Abaixo do peso')
    elif 20<= imc <25:
        print('Peso adequado')
    else:
        print('Acima do peso')