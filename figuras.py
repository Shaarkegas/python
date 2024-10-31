from turtle import *
import random
title('FIGURAS')
setup(800,800)
setworldcoordinates(-200,-200,200,200)

cores=['red', 'blue', 'yellow', 'purple', 'green', 'orange', 'brown','cyan']
t = len(cores)

i = 0
n = 399

anguloexterno = 360 / n
angulointerno = (anguloexterno / 2 + 90)

penup()
forward(1)
pendown()
left(angulointerno)

for i in range(0, n):
    color(cores[random.randrange(0,t)])
    forward(2)
    left(anguloexterno)