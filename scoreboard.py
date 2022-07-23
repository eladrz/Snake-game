from turtle import Turtle
FONT=('courier', 21, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"score= {self.score}",move=False,align="center",font=FONT)

    def addscore(self):
        self.score+=1
        self.clear()
        self.speed(0)
        self.goto(0,270)
        self.write(arg=f"score= {self.score}",move=False,align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",move=False,align="center",font=('Arial', 21, 'normal'))