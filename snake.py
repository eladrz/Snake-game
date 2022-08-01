from turtle import Turtle
import time
POSTIONS=[(0,0),(-20,0),(-40,0)]
MOVE_SPEED=20
class Snake():

    def __init__(self):
        self.snakes=[]
        self.create_snake()  

    def newsnake(self):
        self.snakes=[]
        self.create_snake()   

    def create_snake(self):
        for position in POSTIONS:
            self.add_snake(position)
            
    def deletesnake(self):
        for i in self.snakes:
            i.goto(700,700)
        
        
    def add_snake(self, position):
        new_snake=Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)
    
    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        time.sleep(0.1)
        for i in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[i-1].xcor()
            new_y=self.snakes[i-1].ycor()
            self.snakes[i].goto(new_x,new_y)
        self.snakes[0].forward(MOVE_SPEED)

    def Up(self):
        if  self.snakes[0].heading()==0:
            self.snakes[0].left(90)
        if self.snakes[0].heading()==180:
            self.snakes[0].right(90)
    def Right(self):
        if  self.snakes[0].heading()==90:
            self.snakes[0].right(90)
        if self.snakes[0].heading()==270:
            self.snakes[0].left(90)

    def Left(self):
        if  self.snakes[0].heading()==90:
            self.snakes[0].left(90)
        if self.snakes[0].heading()==270:
            self.snakes[0].right(90)

    def Down(self):
        if self.snakes[0].heading()==0:
            self.snakes[0].right(90)
        if self.snakes[0].heading()==180:
            self.snakes[0].left(90)