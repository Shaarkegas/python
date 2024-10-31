import math
a, b, c = map(float, input().split())
d = (b**2) - 4*(a*c)

if (d < 0) or (2*a == 0):
    print('Impossivel calcular')
else:
    R1 = -b + math.sqrt(d)
    R1 = R1/(2*a)
    R2 = -b - math.sqrt(d)
    R2 = R2/(2*a)
    print('R1 = %.5f' % R1)
    print('R2 = %.5f' % R2)
