# turtle imported
import turtle
wind=turtle.Screen()
wind.title("ping pong by Shawara")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)
# 1st madrab
madrab1 = turtle.Turtle() # initialaize turtle object
madrab1.color("blue") # shape color
madrab1.shape("square") # shape of object
madrab1.speed(0) # object speed
madrab1.penup() # stop making lines while moving
madrab1.goto(-350,0) # sets object place
madrab1.shapesize(stretch_wid=5,stretch_len=1) # modifies object size
# 2nd madrab
madrab2 = turtle.Turtle()
madrab2.color("red")
madrab2.shape("square")
madrab2.speed(0)
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)
# ball
ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3
# score
score1=0
score2=0
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.goto(0, 260)
score.speed(0)
score.penup()

score.write("player1:0 player2:0", align="center", font=("arial", 24))



# functions
def madrab1_up():
    y = madrab1.ycor()# get y cordinat of madrab1
    y += 20 # move the madrab up by 20 pixle
    madrab1.sety(y) #set the new y value
    if (madrab1.ycor()>250):
        madrab1.sety(250)
def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)
    if (madrab2.ycor() > 250):
        madrab2.sety(250)
def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)
    if (madrab1.ycor() < -250):
        madrab1.sety(-250)
def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)
    if (madrab2.ycor() < -250):
        madrab2.sety(-250)
#keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up,"q") #move madrab 1 up when pressing on letter q
wind.onkeypress(madrab1_down,"a")
wind.onkeypress(madrab2_up,"Up") #to use up arrow we write Up
wind.onkeypress(madrab2_down,"Down")


while True:
    wind.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()
        score.write("player1:{} player2:{}".format(score1,score2), align="center", font=("arial", 24))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2 += 1
        score.clear()
        score.write("player1:{} player2:{}".format(score1,score2), align="center", font=("arial", 24))

    #ball hit madrab
    if (ball.xcor()> 340 and ball.xcor() <350 and (ball.ycor() <madrab2.ycor()+40) and (ball.ycor()> madrab2.ycor()-40) ):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor() >-350 and (ball.ycor() <madrab1.ycor()+40) and (ball.ycor()> madrab1.ycor()-40) ):
        ball.setx(-340)
        ball.dx*=-1




