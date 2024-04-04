from turtle import *

speed(0)

penup()
goto(-100, -101)
pendown()
pensize(3)
color("yellow")
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

penup()
goto(-127, 70)
color("brown")
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

penup()
goto(-30, -20)
color("green")
pendown()
begin_fill()
for i in range(1):
    forward(20)
    right(90)
    forward(80)
    right(90)
    forward(30)
    right(90)
    forward(85)
    right(90)
    forward(20)
end_fill()

penup()
goto(20, 50)
color("white")
pendown()
begin_fill()
for i in range(1):
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
end_fill()


exitonclick()