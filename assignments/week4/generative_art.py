#sometimes I need to rerun the code to show the display, I hope its just for me like that
# I took the petalform from here (just the sizing) : https://www.geeksforgeeks.org/python/draw-a-flower-using-turtle-in-python/
from turtle import *
import random

#the set up
width = 400
height = 400
setup(width, height)
tracer(0, 0)
bgcolor('lightgreen')
flower = Turtle()
flower.hideturtle()
flower.speed(0)
flower.pensize(3)
#the code

color = ['blue', 'yellow', 'pink', 'red', 'orange', 'darkblue', 'violet', 'darkred']
flower.color = random.choice(color)

flower_positions = [
    (50, 170),
    (-60, 160),
    (-150, 98),
    (-50, 85),
    (70, 70),
    (150, 90),
    (-150, 0),
    (-50, 0),
    (50, 0),
    (150, 0),
    (-150, -60),
    (-50, -86),
    (52, -75),
    (150, -95),

]

for i, (x, y) in enumerate(flower_positions):
    flower.penup()
    flower.goto(x, y)
    flower.pendown()

    def draw_petal():
        flower.begin_fill()
        flower.circle(70, 60)
        flower.left(120)
        flower.circle(70, 60)
        flower.left(120)
        flower.goto(x, y)
        flower.end_fill()

    for _ in range(15):
        flower.color(random.choice(color)) #pycharm offerd it
        draw_petal()
        flower.left(60)


    if x == 50 or y > 150:
        pencolor('gold')
        flower.fillcolor('gold')
        flower.begin_fill()
        flower.circle(5, 360)
        flower.end_fill()
        # it should be centered
    else:
        flower.penup()
        flower.goto(x, y)
        flower.setheading(-90)
        flower.pendown()
        flower.color('darkgreen')
        flower.pensize(4)
        flower.forward(100)



update()
exitonclick()
