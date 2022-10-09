from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_body_object = []
        self.create_snake()

    # step2 MakingSnake Body#######################
    def create_snake(self):
        for _ in range(3):
            body_part = Turtle(shape="square")
            body_part.penup()
            body_part.color("white")
            body_part.setposition(x=0 - (20 * _), y=0)
            self.snake_body_object.append(body_part)

    # Step3 MOVING SNAKE BODY###################

    def move(self):

        for body_part in range(len(self.snake_body_object) - 1, 0,
                               -1):  # step is 1 or -1 tells direction to count from so for us 210
            new_xcor = self.snake_body_object[body_part - 1].xcor()
            new_ycor = self.snake_body_object[body_part - 1].ycor()
            self.snake_body_object[body_part].setposition(x=new_xcor, y=new_ycor)

        self.snake_body_object[0].forward(20)

    def up(self):
        if self.snake_body_object[0].heading() == 0.0 :
            self.snake_body_object[0].left(90)
        elif self.snake_body_object[0].heading() == 180.0:
            self.snake_body_object[0].right(90)

    def left(self):
        if self.snake_body_object[0].heading() == 90:
            self.snake_body_object[0].left(90)
        elif self.snake_body_object[0].heading() == 270.0:
            self.snake_body_object[0].right(90)


    def right(self):
        if self.snake_body_object[0].heading() == 90:
            self.snake_body_object[0].right(90)
        elif self.snake_body_object[0].heading() == 270.0:
            self.snake_body_object[0].left(90)

    def down(self):
        if self.snake_body_object[0].heading() == 0.0:
            self.snake_body_object[0].right(90)
        elif self.snake_body_object[0].heading() == 180:
            self.snake_body_object[0].left(90)

    def collision_tail(self):
        for segments in range(1,len(self.snake_body_object)):
            if self.snake_body_object[0].position() == self.snake_body_object[segments].position():
                return True
        return False

    def add(self):
        last_segment = self.snake_body_object[len(self.snake_body_object)-1]
        body_part = Turtle(shape="square")
        body_part.penup()
        body_part.color("white")
        body_part.setposition(x= last_segment.xcor(), y=last_segment.ycor())
        self.snake_body_object.append(body_part)

    def reset(self):
        for segments in self.snake_body_object:
            segments.goto(1000,1000)
        self.snake_body_object.clear()
        self.create_snake()