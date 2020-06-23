import turtle
import winsound

#window 

wn= turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score 
score_a = 0
score_b= 0

#Paddle A
pd_a = turtle.Turtle()
pd_a.speed(0)
pd_a.shape("square")
pd_a.color("white")
pd_a.shapesize(stretch_wid=5,stretch_len=1)
pd_a.penup()
pd_a.goto(-350, 0)

#Paddle B
pd_b = turtle.Turtle()
pd_b.speed(0)
pd_b.shape("square")
pd_b.color("white")
pd_b.shapesize(stretch_wid=5,stretch_len=1)
pd_b.penup()
pd_b.goto(+350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.5
ball.dy=-0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Courier",24,"normal"))


#move paddle Function
def pd_a_up():
	y=pd_a.ycor()
	y += 20
	pd_a.sety(y)

def pd_a_down():
	y=pd_a.ycor()
	y -= 20
	pd_a.sety(y)

def pd_b_up():
	y=pd_b.ycor()
	y += 20
	pd_b.sety(y)

def pd_b_down():
	y=pd_b.ycor()
	y -= 20
	pd_b.sety(y)

def gameover():
	ball.goto(0,0)
	turtle.color('white')
	style = ('Times New Roman', 30, 'normal')
	turtle.write('Game Over!', font=style, align='center')
	turtle.hideturtle()




#keyboard binding 
wn.listen()
wn.onkeypress(pd_a_up,"w")
wn.onkeypress(pd_a_down,"s")
wn.onkeypress(pd_b_up,"Up")
wn.onkeypress(pd_b_down,"Down")

#main game loop 
while True:
	wn.update()

	#move ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if ball.xcor() > 390:
		ball.goto(0,0 )
		ball.dx *= -1
		score_a += 1
		winsound.PlaySound("whistle.wav", winsound.SND_ASYNC)
		pen.clear()
		pen.write("Player A: {}      Player B: {}".format (score_a,score_b), align="center", font=("Courier",24,"normal"))


	if ball.xcor() < -390:
		ball.goto(0,0 )
		ball.dx *= -1 
		score_b += 1
		winsound.PlaySound("whistle.wav", winsound.SND_ASYNC)
		pen.clear()
		pen.write("Player A: {}      Player B: {}".format (score_a,score_b), align="center", font=("Courier",24,"normal"))

	#paddle and ball colission 
	if ball.xcor()>340 and ball.xcor()< 350 and (ball.ycor() < pd_b.ycor()+50 and ball.ycor()> pd_b.ycor()-50):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
	if ball.xcor() < -340 and ball.xcor()> -350 and (ball.ycor() < pd_a.ycor()+50 and ball.ycor()> pd_a.ycor()-50):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if score_a == 5 or score_b == 5:
		gameover()