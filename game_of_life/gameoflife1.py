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

startk=0
print(startk)

#start key
def startsc():
    global startk
    startk+=1     
print(startk)

#selecting cell life


wn.listen()
wn.onkeypress(startsc,"space")
#class cell():
 #   __init__

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.hideturtle()
pen.penup()
pen.color("Green")
pen.goto(-300, 150)
txt="Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection."
txl=list(txt)
#pen.write("Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection.", align="left", font=("Courier", 18, "normal"))
s=""
i=0
wn.tracer(0)   
while True:
    if startk==0:
        while i<len(txt):
            if startk==0:
                s=s+txt[i]
                pen.clear()
                pen.write(s,font=("Courier", 18, "normal"))
                time.sleep(0.09)
                i+=1
                if (i>(len(txt)-2)):
                    startk=1
            else:
                break
    elif startk==1:
        pen.clear()
        pen.write("Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection.", align="left", font=("Courier", 18, "normal"))
    elif startk==2:
        pen.clear()
        break



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

#main loop


wn.mainloop()
