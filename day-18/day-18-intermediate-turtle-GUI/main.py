import random
from turtle import Turtle, Screen
import turtle
t = Turtle()
# t.colormode(255)
colors = ['medium slate blue', 'DarkOrchid', 'SeaGreen', 'royal blue',  'wheat',
'IndianRed']
def dashline():
    for _ in range(10):
        t.shape("turtle")
        t.color('red')
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
def draw_shape(num_sides):
    angle = 360 /num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.left(angle)
# for shape_side_n in range(3,11):
#     t.color(random.choice(colors))
#     draw_shape(shape_side_n)
directions = [0,90,180,270]
turtle.colormode(255)
def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color = (r, g, b)
    return random_color
def random_walk():
    for walk in range(1,200):
        col= random_color()
        # t.color(random.choice(colors))
        t.color(col)
        t.pensize(15)
        t.forward(30)
        t.setheading(random.choice(directions))
        t.speed("fastest")
# random_walk()
# print(random_color())
def draw_spirogram(size_of_gap):
    for steps in range(int(360/size_of_gap)):
        t.color(random.choice(colors))
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)
        t.speed(0)
draw_spirogram(13)
screen = Screen()
screen.exitonclick()