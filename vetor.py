from turtle import *
setup(400,400)
setworldcoordinates(-3,-3,3,3)

goto(0,-3)
goto(0,3)
home()
goto(3,0)
goto(-3,0)

home()
color('blue')
goto(2,1)
color('red')
goto(3,3)
penup()

home()
pendown()
color('red')
goto(1,2)
color('blue')
goto(3,3)

penup()
home()
pendown()
color('black')
goto(3,3)