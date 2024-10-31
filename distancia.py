import math
line = input().split()
x1 = float(line[0])
y1 = float(line[1])
line2 = input().split()
x2 = float(line2[0])
y2 = float(line2[1])
dis = (x2-x1)**2 + (y2-y1)**2
math.sqrt(dis)
print("%.4f" % math.sqrt(dis))


