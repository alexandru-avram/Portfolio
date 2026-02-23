import turtle
import time
import _tkinter
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall


# Create the screen
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize snake and food
wall = Wall()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


# Commands for the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_on = True
while game_on:
    try:
        screen.update()
        time.sleep(0.115)
        snake.move()
        
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            scoreboard.inscrease_score()
        
        # Detect collision with wall
        if snake.head.xcor() >= 420 or snake.head.xcor() <= -420 or snake.head.ycor() >= 420 or snake.head.ycor() <= -420:
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    except _tkinter.TclError:
        # This error occurs when the turtle window is closed.
        print("Turtle window closed. Exiting game.")
        game_on = False