n, m, o = map(int,input().split())
if (n<m) and (n<o):
    print(n)
    if (m<o):
        print(m)
        print(o)
    else:
        print(o)
        print(m)
elif (m<n) and (m<o):
    print(m)
    if (n<o):
        print(n)
        print(o)
    else:
        print(o)
        print(n)
elif (o<n) and (o<m):
    print(o)
    if (n<m):
        print(n)
        print(m)
    else:
        print(m)
        print(n)
print()
print(n)
print(m)
print(o)