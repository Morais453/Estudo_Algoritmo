v0 = int(input('Insira a valocidade inicial do veículo m/s:  '))
a = int(input('Insira a aceleração do veículo em m/s²:  '))
t = int(input('insira o tempo em segundos:  '))
vf = v0 + a * t
print(f'A velocidade final do veiculo a partir dos dados informados é {vf*3.6:0.1f}Km/h')