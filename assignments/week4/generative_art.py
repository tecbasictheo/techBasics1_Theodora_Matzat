#sometimes I need to rerun the code to show the display

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

color = ['blue', 'yellow', 'pink', 'red', 'orange']
flower.color = random.choice(color)

flower = Turtle()
flower.hideturtle()
flower.speed(0)

flower_positions = [
    (-100, 100),
    (100, 150),
    (-50, -100),
    (150, -50),
    (0, 0),
    (50, 50)
]

for i, (x, y) in enumerate(flower_positions):
    flower.penup()
    flower.goto(x, y)
    flower.pendown()

    def draw_petal():
        flower.begin_fill()
        flower.circle(100, 60)
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)
        flower.goto(x, y)
        flower.end_fill()

    for _ in range(7):
        flower.color(random.choice(color)) #pycharm offerd it
        draw_petal()
        flower.left(60)


    if x == 0 and y == 0:
        flower.fillcolor('gold')
        flower.begin_fill()
        flower.circle(10, 360)
        flower.end_fill()
    else:
        flower.penup()
        flower.goto(x, y)
        flower.setheading(-90)
        flower.pendown()
        flower.color('darkgreen')
        flower.pensize(3)
        flower.forward(100)



update()
exitonclick()
# anforderung

#- Your code should include at least one set of nested loops and one conditional statement
#- Use `random` and list together to introduce some randomness
#- Feel free to find another drawing to recreate in code. In such case, provide a link of your reference image in comment
#- Introduce color (palette) into your drawing
#- Integrate other methods of turtle from [official documentation](https://docs.python.org/3.12/library/turtle.html)
