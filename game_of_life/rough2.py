import turtle
import os
import random
import time
import math

#setting up the game window

wn=turtle.Screen()
wn.tracer(0)
wn.bgcolor(0,0,0)
wn.title("game_of_life")
wn.colormode(255)
tracker1=turtle.Turtle()
tracker1.speed(0)
tracker1.hideturtle()
tracker1.setpos(400,-400)
tc=(152,146,241)
tracker1.pencolor(tc)
tracker1.seth(90)

n=800
for i in range(0,4):
    tracker1.fd(n)
    tracker1.lt(90)

#class cell():
 #   __init__


lr=[[0]*20]*20
turtle.speed(0)
for i in range(0,20):
    for j in range(0,20):
        lr[i][j]=turtle.Turtle()
        lr[i][j].speed(0)
        lr[i][j].penup()
        kx=-400 +20 + i*40
        ky=400 -20-j*40
        #print(kx,"  ",ky)
        lr[i][j].setpos(kx,ky)
        lr[i][j].shape("square")
        #lr[i][j].shapesize(2)
        lr[i][j].color("white")
        
wn.tracer(1)

wn.mainloop()
