from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
import serial
ArduinoData = serial.Serial('com3', 9600)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
while (ArduinoData.inWaiting() == 0):
    pass
game_is_on = True
screen.listen()
while game_is_on:
    screen.update()
    snake.move()
    screen.onkey(snake.Up, "Up")
    screen.onkey(snake.Right, "Right")
    screen.onkey(snake.Left, "Left")
    screen.onkey(snake.Down, "Down")

    dataPacket = ArduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    dataPacket = dataPacket.split()
    Xval = int(dataPacket[0])
    Yval = int(dataPacket[1])
    SWval = int(dataPacket[2])
    if Xval >= 700:
        snake.Right()
    if Xval <= 300:
        snake.Left()
    if Yval <= 300:
        snake.Up()
    if Yval >= 700:
        snake.Down()

    if snake.snakes[0].distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        scoreboard.addscore()

    if snake.snakes[0].xcor() > 290 or snake.snakes[0].xcor() < -290 or snake.snakes[0].ycor() > 290 or snake.snakes[0].ycor() < -290 or SWval == 0:
        scoreboard.reset()
        snake.deletesnake()
        snake.newsnake()
        time.sleep(1)

    for s in snake.snakes[2:]:
        if snake.snakes[0].distance(s) < 10:
            scoreboard.reset()
            snake.deletesnake()
            snake.newsnake()
            time.sleep(1)


screen.exitonclick()
