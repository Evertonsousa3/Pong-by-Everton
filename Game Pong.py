import turtle
import winsound

# Config. da tela do jogo
wn = turtle.Screen()
wn.title("Pong by Everton")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontuação
pontuacao_a = 0
pontuacao_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.04

#Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador 1: {}  Jogador 2: {}".format(pontuacao_a, pontuacao_b), align="center", font=("Courier", 24, "normal"))


#Funções das paddles 

#função de subir para o paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#função de descer para o paddle A
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#função de subir para o paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#função de descer para o paddle B
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)        


#Pegar o clique do teclado
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#Loop do jogo principal

while True:
    wn.update()

    #Movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Checagem da borda
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pontuacao_a += 1
        placar.clear()
        placar.write("Jogador 1: {}  Jogador 2: {}".format(pontuacao_a, pontuacao_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1   
        pontuacao_b += 1
        placar.clear()
        placar.write("Jogador 1: {}  Jogador 2: {}".format(pontuacao_a, pontuacao_b), align="center", font=("Courier", 24, "normal"))

    #Colisão entre o paddle e a bola        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1    
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)