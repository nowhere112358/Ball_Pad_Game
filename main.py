from turtle import Turtle, Screen
from paddle import Pad
from ball import  Ball
from score import Score
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

padr = Pad(350, 0)
padl = Pad(-350, 0)
ball = Ball()
score = Score()
score.up_date_score()
screen.update()


screen.listen()
screen.onkey(padr.go_up, "Up")
screen.onkey(padr.go_down, "Down")
screen.onkey(padl.go_up, "w")
screen.onkey(padl.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        print(ball.ycor())
        ball.bounce_wall()
    elif ball.distance(padr) < 50 and ball.xcor() > 330 or ball.distance(padl) < 50 and ball.xcor() < -330:
        ball.bounce_pad()
    if ball.xcor() > 380:
        ball.set_pos_ori()
        score.lscore += 1
        score.up_date_score()
    if ball.xcor() < -380:
        ball.set_pos_ori()
        score.rscore += 1
        score.up_date_score()
    screen.update()



screen.exitonclick()
