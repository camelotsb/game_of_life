import turtle
from turtle import Turtle, Screen
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
d1={}
for i in range(0,20):
    for j in range(0,20):
        d1[(i,j)]=0


#start key
def startsc():
    global startk
    startk+=1     
def kill(i,j):
    global lr
    lr[i][j].color((255,255,255))
    lr[i][j].life=0

def forge(i,j):
    global lr
    lr[i][j].color((0,0,0))
    lr[i][j].life=1
  
#selecting cell life
def selec(x,y):
    global lr
    global startk
    if startk==2:
        for i in range(0,20):
            for j in range(0,20): 
                x1,y1=lr[i][j].xcor(),lr[i][j].ycor()
                if ((x-x1>=-19 and x-x1<=19) and (y-y1>=-19 and y-y1<=19)):
                    print()
                    if (lr[i][j].life==0):
                        forge(i,j)
                    elif (lr[i][j].life==1):
                        kill(i,j)
                    break

              
      

wn.listen()
wn.onkeypress(startsc,"space")
wn.onclick(selec)
class cell(Turtle):
    def __init__(self,life,xc,yc):
        super().__init__(shape='square',visible=True)
        self.life=0
        self.shapesize(1.5)
        self.speed(0)
        self.penup()
        self.setx(xc)
        self.sety(yc)
        self.showturtle()
    
 

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



lr=[]
for i in range(20):
    lc=[]
    for j in range(20):
        lc.append(0)
    lr.append(lc)

turtle.speed(0)
for i in range(0,20):
    for j in range(0,20):
        kx= -400 +20 + i*40
        ky= 400 -20-j*40
        lr[i][j]=cell(0,kx,ky)
        lr[i][j].color((255,255,255))
wn.tracer(1)





ddd=turtle.Turtle()
ddd.penup()
ddd.speed(0)
ddd.setpos(0,-350)
ddd.speed(0)
ddd.shape("square")
ddd.color("red")
dddsx,dddsy=10,10
#wn.tracer(0)
#main loop
while True:
    if startk>=3:
        for i in range(1,19):
            for j in range(1,19):
                print((i,j))
                cnl=lr[i+1][j].life+lr[i][j+1].life+lr[i-1][j].life+lr[i][j-1].life+lr[i+1][j+1].life+lr[i-1][j-1].life+lr[i+1][j-1].life+lr[i-1][j+1].life
                print(cnl)
                if (cnl==3):
                    d1[(i,j)]=1
                elif (cnl==2):
                    d1[(i,j)]=lr[i][j].life
                else:
                    d1[(i,j)]=0
        wn.tracer(0)
        for i in range(1,19):
            for j in range(1,19):
                if d1[(i,j)]==1:
                    forge(i,j)
                if d1[(i,j)]==0:
                    kill(i,j)
        wn.tracer(1)

    else:
        print(startk)
        dddx=ddd.xcor()
        dddy=ddd.ycor()
        dddx+=dddsx
        dddy+=0
        if (dddx>=-450 and dddx<=450) :
            ddd.setpos(dddx,dddy)
        else:
            dddsx=dddsx*-1


wn.mainloop()
