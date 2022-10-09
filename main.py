from turtle import Screen
import time
from snake import Snake
from food import Scoreboard, Food


#step1 SetUp our screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#TURN OFF Tn RACER SO SNAKEBODY ANIMATION ISNT BLOTCHY
screen.tracer(0)

#Classes

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.title("SnakeGame")


game_is_on = True
while game_is_on:
    #screen updates showing new positions of body_part objects after they have all moved to make our snake appear together
    screen.update()#THIS LINE OF CODE TIES IN WITH TRACER. WE MUST UPDATE WHERE BODYPART OBJECTS ARE AFTERE THEY'RE MADE
    time.sleep(0.1)

    snake.move()


#Detect collision with food.
    if snake.snake_body_object[0].distance(food) < 15:  #Measures distance of snake head from food if less than 15px do:
        food.refresh()
        scoreboard.scores()
        snake.add()

#Detect Collision With Wall
    if snake.snake_body_object[0].xcor() < -290 or snake.snake_body_object[0].xcor() > 290:
        scoreboard.reset()
        snake.reset()

    if snake.snake_body_object[0].ycor() < -290 or snake.snake_body_object[0].ycor() >290:
        scoreboard.reset()
        snake.reset()
#Detect collision with tail

    for segments in snake.snake_body_object[1:]:

        if snake.snake_body_object[0].distance(segments)<15:
            scoreboard.reset()
            snake.reset




screen.exitonclick()