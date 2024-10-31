a, b, c = map(float,input().split())
ar = ((a+b)*c)/2
pe = a+b+c
if (a+b > c) and (a+c >b):
    if (c+b > a):
        print('Perimetro = %.1f' % pe)
    else:
        print('Area = %.1f' % ar)  
else:
    print('Area = %.1f' % ar)