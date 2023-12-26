import random
import turtle as t
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('download.jpeg', 6)
color_list = [(234, 231, 225), (229, 232, 238), (238, 229, 234), (227, 235, 230), (196, 162, 106), (67, 90, 125)]
def make_rgb():
    rgb_color = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_color.append(new_color)
t.colormode(255)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 100
def my_own():
    for dot_count in range(num_of_dots):
            if dot_count == 0:
                for i in range(10):
                    t.dot(20, random.choice(color_list))
                    t.forward(50)

            if dot_count == 10 or dot_count == 30 or dot_count == 50 or dot_count == 70 or dot_count == 90:
                    t.setheading(90)
                    t.forward(50)
                    for i in range(10):
                        t.setheading(180)
                        t.dot(20, random.choice(color_list))
                        t.forward(50)
            if dot_count == 20 or dot_count == 40 or dot_count == 60 or dot_count == 80 or dot_count == 100:
                    t.setheading(90)
                    t.forward(50)
                    for i in range(10):
                        t.setheading(0)
                        t.dot(20, random.choice(color_list))
                        t.forward(50)
for dot in range(1,num_of_dots+1):
    t.dot(20,random.choice(color_list))
    t.forward(50)
    if dot % 10 == 0:
        print(dot)
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        # t.dot(20, random.choice(color_list))
        t.forward(500)
        t.setheading(0)
screen = t.Screen()
screen.exitonclick()