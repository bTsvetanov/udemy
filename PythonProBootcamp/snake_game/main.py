from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
gameison = True
while gameison:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.update()
        snake.extend()
    
    if snake.outof_border():
        gameison = False
        scoreboard.gameover()
    for seg in snake.segments[1:]:
         if snake.head.distance(seg) <10 :
            gameison = False
            scoreboard.gameover()

          
        
    

screen.exitonclick()