v1 = int(input('Pridmeiro valor: '))
v2 = int(input('Segundo valor: '))
soma = (v1 + v2) 
resultado = soma % 2
if resultado == 0:
    print('O número {} é Par'.format(soma)) 
else:
    print('O número {} é Ímpar'.format(soma)) 