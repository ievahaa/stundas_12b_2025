from turtle import Turtle, Screen, colormode
from random import randint
timijs = Turtle()


timijs.pensize(8) # līnijas biezums


colormode(255)

# zieds
for i in range(6):
    timijs.penup() # paceļ zīmuli (nezīmē)
    timijs.color(randint(0, 255), randint(0, 255), randint(0, 255))
    timijs.forward(120)
    timijs.pendown() # nolaiž zīmuli (zīmē atkal)
    timijs.left(60)
    timijs.circle(50)


# varavīksne
krasas = ["red", "orange", "yellow", "green", "blue", "indigo", "violet" ]
timijs.right(90)
x = 0
for i in krasas:
    timijs.penup() # paceļ zīmuli (nezīmē)
    timijs.goto(x, 0)
    timijs.color(i)
    # timijs.forward(120)
    timijs.pendown() # nolaiž zīmuli (zīmē atkal)
    timijs.left(180)
    timijs.circle(150+x,180)
    x -= 5


screen = Screen()
screen.exitonclick()
