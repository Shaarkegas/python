V = int(input())
A = int(input())
F = int(input())
P = int(input())

T = A+F+P
if V - T >= 0:
    print(3)
elif V - (A+F) >= 0 or V - (P+F) >= 0 or V - (A+P) >= 0:
    print(2)
elif V - A >= 0 or V - F >= 0 or V - P >= 0:
    print(1)
else:
    print(0)
