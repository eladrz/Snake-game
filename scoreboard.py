from turtle import Turtle
FONT=('courier', 21, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file: 
            self.highscore=int(file.read())
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"score= {self.score}|  High score={self.highscore}",move=False,align="center",font=FONT)

    def addscore(self):
        self.score+=1
        self.clear()
        self.speed(0)
        self.goto(0,270)
        self.write(arg=f"score= {self.score}| High score={self.highscore}",move=False,align="center",font=FONT)

    def reset(self):
        if self.score>self.highscore:
            with open("data.txt",mode="w") as file:
                file.write(f"{self.score}")
        self.score=0
        self.clear()
        self.speed(0)
        self.goto(0,270)
        with open("data.txt") as file: 
            self.highscore=int(file.read())
        self.write(arg=f"score= {self.score}| High score={self.highscore}",move=False,align="center",font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER",move=False,align="center",font=('Arial', 21, 'normal'))