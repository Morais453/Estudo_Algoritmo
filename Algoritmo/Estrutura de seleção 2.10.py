a= int(input('Indique o primeiro termo:  '))
b= int(input('indique o segundo termo:  '))
c= int(input('Indique o termo independente:  '))
delta= b**2 -4*a*c

if b>0 and c>0:
    print(f' A função informada foi {a}x²+{b}x+{c}')
elif c>0:
    print(f' A função informada foi {a}x²{b}x+{c}')
elif b>0:
    print(f' A função informada foi {a}x²+{b}x{c}')
else:
    print(f' A função informada foi {a}x²{b}x{c}')

print("delta igual a", delta)
if delta>0:
    print('Raízes diferentes')
    x1= (-b + delta**(1/2)) / (2*a)
    x2= (-b - delta**(1/2)) / (2*a)
    print('As raízes encontradas são {} e {}'.format(x1,x2))
elif delta==0:
    print('Raízes iguais')
    x= (-b + delta**(1/2)) / (2*a)
    print(f'A raíz encontrada foi {x}')
else:
    print('Não há raiz real')
    