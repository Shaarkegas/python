n = int(input())
v = []
i = 1
q = 0
while i <= n:
    if (n%i) == 0:
        print(f'{i} eh divisor!')
        q = q + 1
        i = i + 1
    else:
        i = i + 1

if q == 2:
    print('NUMERO PRIMO!')
else:
    print(f'{n} tem {q} divisores!')