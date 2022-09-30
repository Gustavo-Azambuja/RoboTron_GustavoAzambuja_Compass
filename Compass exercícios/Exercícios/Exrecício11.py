x = input().split()

inicial,final=x

inicial = int(x[0])
final = int(x[1])

if inicial < final:
    duracao = final - inicial
else:
    duracao = (24 - inicial) + final
print('O JOGO DUROU {} HORA(S)'.format(duracao))