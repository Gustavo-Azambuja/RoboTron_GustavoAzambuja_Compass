v = 0
x = []
while int(v) < 2:
    v = input()
for i in range(0,int(v)):
    if i % 2!=0:
        x.append(i)
    else:
        pass
print(*x)
