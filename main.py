from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

game_is_on=True
screen.listen()
while game_is_on:
    screen.update()
    snake.move()
    screen.onkey(snake.Up,"Up")
    screen.onkey(snake.Right,"Right")
    screen.onkey(snake.Left,"Left")
    screen.onkey(snake.Down,"Down")
    
    if snake.snakes[0].distance(food)<15:
        snake.extend_snake()
        food.refresh()
        scoreboard.addscore()

    if snake.snakes[0].xcor()>290 or snake.snakes[0].xcor()<-290 or snake.snakes[0].ycor()>290 or snake.snakes[0].ycor()<-290:
        scoreboard.reset()
        snake.deletesnake()
        snake.newsnake()
        time.sleep(1)
       

    for s in snake.snakes[2:]:
        if snake.snakes[0].distance(s)<10:
            scoreboard.reset()
            snake.deletesnake()
            snake.newsnake()
            time.sleep(1)
          
   

screen.exitonclick()