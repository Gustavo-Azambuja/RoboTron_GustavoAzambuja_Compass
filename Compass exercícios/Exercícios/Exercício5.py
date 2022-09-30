tamanho = mediaA = x = 0 
for y in range (1,21):
    x = int(input('{}º valor: '.format(y)))
    if x % 2 == 0:
        mediaA += x
        tamanho += 1
print('Média aritimética igual a:', mediaA/tamanho)