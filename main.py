# Imports
import time
from turtle import Screen
from snake import Snake

# Objects
myScreen = Screen()
snake = Snake()

# Main Program
myScreen.setup(height=600, width=600)
myScreen.bgcolor("black")
myScreen.title("Snake Game")
myScreen.tracer(0)


game_is_on = True

while game_is_on:
    myScreen.update()
    time.sleep(0.1)
    snake.move()





myScreen.exitonclick()
