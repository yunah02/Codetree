a0 = input()

a1 = a0.split()

a = int(a1[0])
b = int(a1[1])

for i in range(b, a-1, -1) :
    print(i, end=' ')
