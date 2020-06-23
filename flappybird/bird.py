import turtle 
import time 
import winsound


#creating window
wn= turtle.Screen()
wn.title("Flappy Bird")
wn.bgcolor("blue")
wn.bgpic("bg.png")
wn.setup(width=500 , height=800)
wn.tracer(0)


#creating bird 
player= turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.shapesize(stretch_wid=1, stretch_len=1, outline=None)
player.goto(-200,0)
player.dx=0
player.dy=1

#score 
score = 0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,220)
pen.write("Score: 0", align="center", font=("Courier",24,"normal"))

#final score
final = turtle.Turtle()
final.speed(0)
final.color("white")
final.penup()
final.hideturtle()
final.goto(+150,-40)

#game Over
over = turtle.Turtle()
over.speed(0)
over.color("white")
over.penup()
over.hideturtle()
over.goto(+20,-10)
 


#creating pipes
#pipe 1
pipe1_top= turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=16, stretch_len=3, outline=None)
pipe1_top.goto(0,250)
pipe1_top.dx=-6
pipe1_top.dy=0
pipe1_top.value=1

pipe1_bottom= turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=16, stretch_len=3, outline=None)
pipe1_bottom.goto(0,-250)
pipe1_bottom.dx=-6
pipe1_bottom.dy=0

#pipe2
pipe2_top= turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=16, stretch_len=3, outline=None)
pipe2_top.goto(1000,300)
pipe2_top.dx=-6
pipe2_top.dy=0
pipe2_top.value=1

pipe2_bottom= turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=16, stretch_len=3, outline=None)
pipe2_bottom.goto(1000,-200)
pipe2_bottom.dx=-6
pipe2_bottom.dy=0


gravity = -0.7

#movement function 
def go_up():
	winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
	player.dy += 13

	if player.dy > 13:
		player.dy = 13



#resume function 
def resume():
	score=0
	wn.update()
	pipe1_top.setx(300)
	pipe1_bottom.setx(300)
	pipe2_top.setx(1000)
	pipe2_bottom.setx(1000)
	player.goto(-200,0)
	player.dy = 0
	final.clear()
	over.clear()
#colission function 
def gameover():
	gravity = 55
	turtle.color('white')
	style = ('Times New Roman', 30, 'normal')
	over.write('Game Over!' ,font=style, align='center')
	final.write("Your Score: {}".format (score), align="right", font=("Courier",24,"normal"))
	wn.update()
	time.sleep(3)
	turtle.hideturtle()



#keyboard binding
wn.listen()
wn.onkeypress(go_up,"space")
wn.onkeypress(resume,"s")

#main game loop 
while True:
	#pause 
	time.sleep(0.02)
	#update screen 
	wn.update()
	#adding gravity 
	player.dy += gravity

	#move bird
	y= player.ycor()
	y += player.dy
	player.sety(y)

	#bottom border 
	if player.ycor() < -340:
		player.dy = 0
		player.sety(-340)

	#move pipes1
	x = pipe1_top.xcor()
	x += pipe1_top.dx
	pipe1_top.setx(x)

	x = pipe1_bottom.xcor()
	x += pipe1_bottom.dx
	pipe1_bottom.setx(x)

	#return pipes to start 
	if pipe1_top.xcor() < - 350 :
		pipe1_top.setx(350)
		pipe1_bottom.setx(350)
		pipe1_top.value=1

	#move pipes2
	x = pipe2_top.xcor()
	x += pipe2_top.dx
	pipe2_top.setx(x)

	x = pipe2_bottom.xcor()
	x += pipe2_bottom.dx
	pipe2_bottom.setx(x)

	#return pipes to start 
	if pipe2_top.xcor() < - 350 :
		pipe2_top.setx(350)
		pipe2_bottom.setx(350)
		pipe2_top.value=1



# check for collision 
#pipe 1
	if (player.xcor() +10 >pipe1_top.xcor() - 30) and (player.xcor()-10 < pipe1_top.xcor() + 30) :
		if (player.ycor() + 10 > pipe1_top.ycor()-160) or (player.ycor() - 10 < pipe1_bottom.ycor()+ 160) :
			gameover()

	#check score 		
	if pipe1_top.xcor() + 30 < player.xcor() - 10:
		score += pipe1_top.value
		pen.clear()
		pen.write("Score: {}".format (score), align="center", font=("Courier",24,"normal"))
			

#pipe 2
	if (player.xcor() +10 >pipe2_top.xcor() - 30) and (player.xcor()-10 < pipe2_top.xcor() + 30) :
		if (player.ycor() + 10 > pipe2_top.ycor()-160) or (player.ycor() - 10 < pipe2_bottom.ycor()+ 160) :
			gameover()

	#check score 		
	if pipe2_top.xcor() + 30 < player.xcor() - 10:
		score += pipe2_top.value
		pen.clear()
		pen.write("Score: {}".format (score), align="center", font=("Courier",24,"normal"))

		





#mainloop 
wn.mainloop()