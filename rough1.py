import turtle
import time
from turtle import Turtle, Screen
from defer import return_value

k=0

# setting up the screen
wn=turtle.Screen()
wn.title("way_of_life")
wn.bgcolor("black")
wn.setup(width=810, height= 810)
wn.tracer(0)

#creating a pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.hideturtle()
pen.penup()
pen.color("Green")
pen.goto(-300, 150)
# giving the instructions
txt="Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection."
txl=list(txt)
#pen.write("Instructions:\n1.Enter the number of cells you want\nto be alive at start, max 8\n2.Select the boxes and the game will \nstart once you have finished your selection.", align="left", font=("Courier", 18, "normal"))
pen.write(txt,font=("Courier", 18, "normal"))
#wn.update()
# pen.clear()



# # creating a cell
# def create():
#     cell=turtle.Turtle()

#     cell.resizemode("user")
#     cell.turtlesize(0.5, 0.5)
    
#     cell.speed(0)
#     cell.color("white")
#     cell.shape("square")
#     cell.hideturtle()
#     cell.penup()

#     return cell

#updating the screen
def updates(x, y):
    global pen
    pen.clear()
    #wn.update()
    wn.tracer(1)

# getting the coordinates
def get_coor(x,y):
    return x, y


class cells(Turtle):

    def __init__(self):
        super().__init__(shape="square", visible=True)
        # self.turtle=turtle.Turtle()
        self.speed(0)

        self.shapesize(0.5)

        self.color("white")
        # self.hideturtle()
        # self.shape("square")
        self.penup()


# creating the lists
# list of lists
out=[]
bi= []

# lists for turtles
for i in range (0, 40, 1):
    list=[]
    out.append(list)
    arr=[0 for i in range(40)]
    bi.append(arr)

# cell= cells()

# creating the turtles
for list in out:
    for i in range (0, 40, 1):
        # cell= create()
        cell= cells()
        cell.goto(-395+k*20, 395-(i*20))
        list.append(cell)
        # list[i][k].goto((-390+k*20, 390-(i*20)))

    k+=1

turtle.onscreenclick(updates)

# turtle.mainloop()

# GAME
# n= turtle.textinput("Enter the number of cells", "")

# for i in range(n):



turtle.done()