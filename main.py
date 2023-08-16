# Imports
from turtle import Turtle, Screen

# Objects
myScreen = Screen()
x_cor = [0, -20, -40]


# Functions


# Main Program
myScreen.setup(height=600, width=600)
myScreen.bgcolor("black")
myScreen.title("Snake Game")

for i in range(0, 3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.goto(x=x_cor[i], y=0)




myScreen.exitonclick()
