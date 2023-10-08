matriz = [['', '', ''], ['', '', ''], ['', '', '']]

print(f'''{matriz[0][0]:^3}|{matriz[0][1]:^3}|{matriz[0][2]:^3}\n---|---|---
{matriz[1][0]:^3}|{matriz[1][1]:^3}|{matriz[1][2]:^3}\n---|---|---
{matriz[2][0]:^3}|{matriz[2][1]:^3}|{matriz[2][2]:^3}''')

#DEFINIR NOME DOS PLAYERS
player1 = input('Informe seu nome: ')
player2 = input('Informe seu nome: ')

#VARIAVEIS PARA MARCAÇÃO
VAR_QUALQUER = True
simbolo = 'X'
Player = 'i'

#JOGO EM SI, LAÇO CONT COM O N° MÁXIMO DE JOGADAS POSSIVEIS
for i in range(1,10):
    
    #DEFINIÇÃO DE NOME E SIMBOLO DE JOGADOR
    if i % 2 == 1:
        Player = player1
        simbolo = 'X'
    else:
        Player = player2
        simbolo = 'O'     

    print(f'É a vez de {Player}:')

    #LAÇO CONTINUO
    while VAR_QUALQUER:  
        
        #DEFINIÇÃO DA JOGADA, LINHA E COLUNA
        linha = int(input('Informe onde adicionar seu simbolo na linha[0,1,2]: '))
        coluna = int(input('Informe onde adicionar seu simbolo na coluna [0,1,2]: '))

        #VERIFICAÇÃO SE A MATRIZ ESTÁ DISPONIVEL OU NÃO, SE SIM ADICIONA O SIMBOLO EQUIVALENTE AO JOGADOR E QUEBRA O LAÇO CONTINUO
        #SE NÃO ESCREVE QUE JÁ TEM ITEM E CONTINUA PEDINDO UMA COORDENADA PARA O SIMBOLO
        if matriz[linha][coluna] == '':
            matriz[linha][coluna] = simbolo
            break
        else:
            print('Já contém item, tente novamente')

    #MOSTRA O TABULEIRO A CADA RODADA
    print(f'''{matriz[0][0]:^3}|{matriz[0][1]:^3}|{matriz[0][2]:^3}\n---|---|---
{matriz[1][0]:^3}|{matriz[1][1]:^3}|{matriz[1][2]:^3}\n---|---|---
{matriz[2][0]:^3}|{matriz[2][1]:^3}|{matriz[2][2]:^3}''')

    #VERIFICAR CONDIÇÃO DE VITÓRIA A PARTIR DA QUINTA JOGADA    
    if i > 4:
        
        for l in range(0,3):
            #VERIFICA LINHA
            if matriz[l][0] == matriz[l][1] == matriz[l][2]:
                print(f'A vitória foi de {Player}')
                VAR_QUALQUER = False #INTERROMPE O LAÇO CONTINUO
                break #INTERROMPE O 'FOR'

            #VERIFICA COLUNA
            elif matriz[0][l] == matriz[1][l] == matriz[2][l]:
                print(f'A vitória foi de {Player}')
                VAR_QUALQUER = False
                break

            #VERIFICA AS DIAGONAIS
            elif matriz[0][0] == matriz[1][1] == matriz[2][2] or matriz[0][2] == matriz[1][1] == matriz[2][0]:
                print(f'A vitória foi de {Player}')
                VAR_QUALQUER = False
                break
            
            #SE CHEGAR A 9 JOGADAS SEM VITÓRIA DECLARAR EMPATE
            else:
                if i == 9: 
                    print('Empate')
                    break
    #SE A VARIAVEL DE CONTROLE RECEBER FALSE ANTES DO LOOP PRINCIPAL ACABAR, INTERROMPER O LOOP
    if VAR_QUALQUER == False:
        break
        