#Snake'S Den Game

from turtle import Screen
#Turtle library for graphics.
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#To start game again.
def reset_game():
    global snake,food,scoreboard,game_is_on
    screen.clear()
    screen.bgcolor("black")  
    screen.tracer(0)
    
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    game_is_on = True
    
    screen.listen()#For listening events like key press.
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    

def game_over():
    global game_is_on
    scoreboard.game_over()
    screen.update()
    time.sleep(0.5) #Pause for a moment to display the game over message.
    
    #Prompt user to play again.
    
    response = screen.textinput("Game Over", "Do you want to play again? (Yes/No)").lower()
    if response == "yes":  
        reset_game()
    else:
        screen.bye()

    
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake's Den")
screen.tracer(0)

reset_game() #Initilize the game.




while True:
    if game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        #Detect collision with food.
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            snake.extend(food.get_color())
            food.refresh()
            

        #Detect collision with wall.
        if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
            game_is_on = False
            game_over()
            
            
        #Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                game_over()
    else:
        game_over()        
         
screen.mainloop()