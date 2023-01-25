from turtle import Screen
import time
from snake import Snake
from food import Food
from scorecard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.update()

game_is_on = True

while game_is_on:

    screen.listen()
    screen.onkeyrelease(snake.up, "w", )
    screen.onkeyrelease(snake.down, "s", )
    screen.onkeyrelease(snake.left, "a", )
    screen.onkeyrelease(snake.right, "d", )

    screen.update()
    time.sleep(0.2)
    snake.move(20)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.new_segment()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # score.score()
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset()


screen.exitonclick()
