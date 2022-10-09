from turtle import Turtle
from snake import SnakeBody
SnakeBody()
class MoveSnake:
    def __init__(self):

        for body_part in range(len(self.snake_body_object) - 1, 0,
                               -1):  # step is 1 or -1 tells direction to count from so for us 210
            new_xcor = self.snake_body_object[body_part - 1].xcor()
            new_ycor = self.snake_body_object[body_part - 1].ycor()
            self.snake_body_object[body_part].setposition(x=new_xcor, y=new_ycor)

        self.snake_body_object[0].forward(20)