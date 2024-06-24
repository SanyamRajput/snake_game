from turtle import Screen
from snake import Snake
from food import Food
import time
from scorebord import ScoreBoard

scr = Screen()
scr.setup(600, 600)
scr.bgcolor('black')
scr.title('snake')
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

scr.listen()
scr.onkey(snake.up, 'Up')
scr.onkey(snake.down, 'Down')
scr.onkey(snake.left, 'Left')
scr.onkey(snake.right, 'Right')


ongame = True
while ongame:
    scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()



scr.exitonclick()
