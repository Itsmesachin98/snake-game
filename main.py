from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# Defining classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()
food.refresh()

# Event Listeners
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Making the snake move
    snake.move()

    # Detect collison with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collison with Wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collison with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()