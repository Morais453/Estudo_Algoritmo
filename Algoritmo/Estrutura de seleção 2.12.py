a = int(input('Insira a aceleração do veículo: m/s²'))
V0 = int(input('Insira a velocidade inicial:  m/s'))
t = int(input('Insira o tempo de percurso: s'))
Vms2 = V0 + a * t
Km = Vms2 * 3.6
print(f'Sua velocida média de foi igual a {Vms2}m/s ou {Km}Km/h')
if Km <= 40:
    print('Muito lento')
if 40 < Km <= 60:
    print('Velocidade permitida')
if 60 < Km <= 80:
    print('Velocidade de cruzeiro')
if 8 < Km <= 120:
    print('Sr. ta meio rápido, né?')
if Km >120:
    print('Quer conhecer Jeusus mais cedo?')