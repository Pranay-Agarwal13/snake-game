from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_SIZE = 600
BOUNDARY = 280  

def play_round(screen):
    
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

   
    food.refresh([seg.position() for seg in snake.segments])

  
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.listen()

    base_delay = 0.1
    min_delay = 0.03
    game_is_on = True

    while game_is_on:
        
        screen.update()
        delay = max(min_delay, base_delay - (scoreboard.score * 0.007))
        time.sleep(delay)
        snake.move()

        if snake.head.distance(food) < 15:
            
            food.refresh([seg.position() for seg in snake.segments])
            snake.extend()
            scoreboard.increase_score()

       
        if (snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY
                or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY):
            game_is_on = False
            scoreboard.game_over()

        
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                break

    
    answer = screen.textinput("Play again?", "Type 'y' to play again, anything else to quit:")
    play_again = bool(answer and answer.lower().strip() == 'y')

    
    try:
        for seg in snake.segments:
            seg.hideturtle()
        food.hideturtle()
        scoreboard.clear()
        scoreboard.hideturtle()
    except Exception:
        
        pass

    return play_again


def main():
   
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    
    try:
        while True:
            play_again = play_round(screen)
            if not play_again:
                break
    except Exception as e:
        
        try:
            screen.bye()
        except Exception:
            pass
        raise e

    
    screen.bye()


if __name__ == "__main__":
    main()
