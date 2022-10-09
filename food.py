from turtle import Turtle
import random

class Food(Turtle):   #Food Class Inheriting From Turtle Class

    def __init__(self):
        super().__init__()   #I can call directly from Turtle because we pulled from that class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid=0.5) #Usually 20 x 20 now it is 10 x 10 circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode = "r") as highscore:
            self.high_score=int(highscore.read())

        self.color("white")
        self.penup()
        self.goto(x=0,y=281)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", move=False, align="center", font=("courier", 12, "normal"))

    def scores(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", move=False, align="center", font=("courier", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=("courier", 18, "normal"))

    def reset(self):
        print(self.score)
        print(self.high_score)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt",mode="w") as highscore:
                highscore.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", move=False, align="center", font=("courier", 12, "normal"))


