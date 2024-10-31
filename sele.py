a, b, c, d = map(int, input().split())
if (b > c) and (d > a):
    if (c+d > a+b) and (d > 0):
        a%2
        if (a%2 == 0) and (c > 0):
            print('Valores aceitos')
else:
    print('Valores nao aceitos')