import time
from  Snake import *
from Food import *
from Scoreboard import *


with open('art_snake.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"w")
screen.onkey(snake.down , "s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep ( 0.1 )
    snake.move()

    #Eat Food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.inscrease_score()

    #Wall Hit
    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or  snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on  = False
        scoreboard.game_over()

    #Detect collisiton with tail
    for segment in snake.segments[1:]:
        if snake.head.distance( segment ) < 10 :
            game_is_on = False
            scoreboard.game_over()








screen.exitonclick()