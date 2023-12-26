import random
from turtle import Turtle,Screen
screen = Screen()
screen.setup(width=500,height=500)
turtle_color=['red','green','blue','cyan','black','gray']
y_position = [70,40,-10,-20,-40,-60]
user_bet = screen.textinput(title="Enter the turtle bet.",prompt="Which turtle will win the race? Enter the color")
is_race = True
all_turtle = []
for turtle in range(0,6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(turtle_color[turtle])
    t.goto(x=-230,y=y_position[turtle])
    all_turtle.append(t)
while is_race:
    for all_t in all_turtle:
        all_t.forward(random.randint(0, 10))
        all_t.speed(0)
        if all_t.xcor()>230:
            is_race = False
            winning_color = all_t.pencolor()
            if winning_color == user_bet:
                print(f"The winner is {winning_color} turtle .")
            else:
                print(f"You lost the race. The winner is {winning_color} turtle.")
screen.exitonclick()