import turtle #pip install turtle
import random
import pygame # pip install pygame

pygame.init()

pygame.mixer.music.load('bgmusic.mp3')
pygame.mixer.music.play()

screen = turtle.Screen()
screen.title("Balls Game")
screen.bgcolor("black")
screen.tracer(0)


balls = []

for i in range(30):
    balls.append(turtle.Turtle())

#colors
colors = ["yellow","red","white","orange","blue"]


#handling multiple balls
for ball in balls:
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.up()
    ball.speed(0)
    x = random.randint(-260,260)
    y = random.randint(-260,260)
    ball.goto(x,y)
    ball.dy = 0
    ball.dx = random.randint(-0,3)
    ball.da = 0

gravity = 0.1

while True:
    screen.update()
    for ball in balls:

        ball.dy -= gravity
        ball.rt(ball.da)

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # checking for wall collistion
        if ball.xcor() > 260:
            ball.dx *= -1

        if ball.xcor() < -260:
            ball.dx *= -1

        # checking for jump
        if ball.ycor() < -260:
            ball.dy *= -1


screen.mainloop()
