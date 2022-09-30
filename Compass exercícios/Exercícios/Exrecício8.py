x = int(input()) 

def FAT(x):
    fat = 1
    for a in range(1, x+1):
        fat = fat * a
    return fat
def Tabuada (x):
    for a in  range(1,11):
        print(f'{a} X {x} =', a*x)
if x % 2 == 0:
    print('Fatorial de {} é {}' .format(x, FAT(x)))
else:
    Tabuada(x)

