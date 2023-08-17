# Imports
from turtle import Turtle


x_cor = [0, -20, -40]

class Snake:
    def __init__(self):
        self.snake = []
        self.create()

    def create(self):
        for i in range(0, 3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=x_cor[i], y=0)
            self.snake.append(new_turtle)


    def move(self):
        for turtle_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[turtle_num-1].xcor()
            new_y = self.snake[turtle_num - 1].ycor()
            self.snake[turtle_num].goto(new_x, new_y)
            self.snake[0].forward(20)
            self.snake[0].right(90)
