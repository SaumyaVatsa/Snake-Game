# Imports
import time
from turtle import Turtle, Screen

# Objects
myScreen = Screen()
x_cor = [0, -20, -40]
snake = []

# Main Program
myScreen.setup(height=600, width=600)
myScreen.bgcolor("black")
myScreen.title("Snake Game")
myScreen.tracer(0)

for i in range(0, 3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_cor[i], y=0)
    snake.append(new_turtle)


game_is_on = True

while game_is_on:
    myScreen.update()
    time.sleep(0.1)
    for turtle_num in range(len(snake)-1, 0, -1):
        new_x = snake[turtle_num-1].xcor()
        new_y = snake[turtle_num - 1].ycor()
        snake[turtle_num].goto(new_x, new_y)
    snake[0].forward(20)
    snake[0].right(90)




myScreen.exitonclick()
