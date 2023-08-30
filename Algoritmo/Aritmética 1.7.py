from statistics import geometric_mean
n1= int(input('Informe o primeiro valor: '))

n2= int(input('Informe o segundo valo: '))

valores= [n1 , n2]

mg= geometric_mean(valores)

print(mg)
