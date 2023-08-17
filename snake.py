# Imports
from turtle import Turtle

# Constants
x_cor = [0, -20, -40]
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.snake = []
        self.create()
        self.head = self.snake[0]

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
        self.head.forward(20)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
