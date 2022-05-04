import random
pm=50
pc=0
g1=0
a=10

while g1==0 and a>=2:
    stri="enter a number bw 1-"+str(a)+" :"
    n1=int(input(stri))
    nc1=random.randint(1,a )
    if (n1==0):
        g1=2
        print("game ended")
        print("current winnings",pm,"$")
    elif (n1==nc1 or n1>10 or n1<0):
        pc=pm
        pm=0
        g1=1
        print("game over")
        print("money lost",pc,"$")
    else:
        pm=pm*2
        a=a-1
        print("you won ",pm/2,"$")
        print("current money:",pm,"$")
else:
    if (g1==0):
        print("Thats enough for now")