"""
Program that simulates a race amoung turtles
Author: Jose Amarante
FULL SCREEN FOR PROPER VIEW
"""

# IMPORTS MODULES
import time
import turtle
import random

# INITIALIZES IMPORTANT VARIABLE SUCH AS PEN AND SCREEN

window = turtle.Screen()
window.setup(1250, 1000)
window.bgcolor("#89CFF0")
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
turtle.title("TURTLE RACE | BIGGEST RACE OF 2021")
finish = 490


# TURTLE 1
turtle1 = turtle.Turtle()
turtle1.color("#3498DB")
turtle1.shape('turtle')
turtle1.up()
turtle1.hideturtle()

# TURTLE 2
turtle2 = turtle.Turtle()
turtle2.color("#2ECC71")
turtle2.shape('turtle')
turtle2.up()
turtle2.hideturtle()

# TURTLE 3
turtle3 = turtle.Turtle()
turtle3.color("#E74C3C")
turtle3.shape('turtle')
turtle3.hideturtle()

# DIFFERENT FUNCTIONS

def init():
    # TURTLE 1 POSITION
    turtle1.up()
    turtle1.goto(-500, 250)
    turtle1.showturtle()
    turtle1.shapesize(3, 3, 10)
    # TURTLE 2 POSITION
    turtle2.up()
    turtle2.goto(-500, 0)
    turtle2.showturtle()
    turtle2.shapesize(3, 3, 10)
    # TURTLE 3 POSITION
    turtle3.up()
    turtle3.goto(-500, -250)
    turtle3.showturtle()
    turtle3.shapesize(3, 3, 10)


def title():
    # FIRST SCREEN MESSAGE
    pen.up()
    pen.goto(0, 0)
    pen.down()
    pen.write("THE BIGGEST RACE OF 2021!!!!",
              align="center", font=("Verdana", 50, "bold"))
    time.sleep(5)
    pen.clear()

    # SECOND SCREEN MESSAGE
    pen.up()
    pen.goto(0, 0)
    pen.down()
    pen.write("ARE YOU READY???!!!", align="center",
              font=("Verdana", 50, "bold"))
    time.sleep(5)
    pen.clear()

    # THIRD SCREEN ASKS FOR USER TO CLICK
    pen.up()
    pen.goto(0, 0)
    pen.down()
    pen.write("HERE WE GOOOOO!!!", align="center",
              font=("Verdana", 50, "bold"))
    time.sleep(3)
    pen.clear()
    # WILL HOLD UNTIL USER CLICKS ON SCREEN
    # CLICK IS WORK IN PROGRESS
    userClick()


def userClick():
    # LOOPS THROUGH 3,2,1
    for p in range(3, 0, -1):
        pen.up()
        pen.goto(0, 0)
        pen.down()
        pen.write(f"{p}", align="center", font=("Verdana", 100, "bold"))
        time.sleep(1)
        pen.clear()
    pen.write("START", align="center", font=("Verdana", 50, "bold"))
    pen.clear()
    raceInit()


def raceBanner():
    # BANNER ON TOP
    pen.up()
    pen.goto(0, 400)
    pen.down()
    pen.color("white")
    window.bgcolor("#E394C0")
    pen.write("THE AMAZING TURTLE RACE OF 2021",align="center", font=("Verdana", 40, "bold"))
    pen.up()
    pen.goto(-500, 380)
    pen.down()
    pen.pensize(15)
    pen.fd(1000)
    pen.up()

# DRAWS FINISHLINE AND RACETRACK LINES
def finishLine():
    pen.goto(550, 350)
    pen.right(90)
    pen.down()
    pen.pensize(20)
    pen.fd(750)

    # DRAWS FIRST RACE LINES
    pen.pensize(10)
    pen.speed(10)
    pen.up()
    pen.goto(-500,125)
    pen.left(90)
    pen.down()
    pen.forward(1000)
    pen.up()
    pen.goto(-400,220)
    pen.down()
    pen.write("1", font=("Verdana", 40, "bold"))
    # DRAWS NUMBER FOR MIDDLE TURTLE
    pen.up()
    pen.goto(-400,-10)
    pen.write("2", font=("Verdana", 40, "bold"))
    # DRAWS SECOND RACE LINES
    pen.up()
    pen.goto(-500,-125)
    pen.down()
    pen.forward(1000)
    pen.up()
    pen.goto(-400,-300)
    pen.down()
    pen.write("3", font=("Verdana", 40, "bold"))

# ACTUAL RACE MECHANIC
def race(userInput, name):
    # RANDOMIZES SPEED FOR TURTLE
    speed1 = random.randint(20,45)
    speed2 = random.randint(20,45)
    speed3 = random.randint(20,45)
    global count
    global check
    check = 0
    count = 0
    # IF TURTLE REACHES X = 360 THEY WIN
    # INDIVIDUAL FOR EACH OF CHECK WHILE OR FOR LOOP
    while turtle1.xcor() < finish or turtle2.xcor() < finish or turtle3.xcor() < finish:
        turtle1.fd(speed1)
        if turtle1.xcor() > finish:
            check = 1
            break
        turtle2.fd(speed2)
        
        if turtle2.xcor() > finish:
            check = 2
            break
        turtle3.fd(speed3)
        if turtle3.xcor() > finish:
            check = 3
            break
        count+=1
    time.sleep(1)
    # CHECKS WHO WON
    window.clear()
    window.bgcolor("#E394C0")
    pen.color("white")
    if check == 1 and userInput == 1:
        pen.up()
        pen.goto(0,0)
        pen.down()
        podium(1)
    elif check ==1 and userInput != 1:
        pen.up()
        pen.goto(0,0)
        pen.down()
        window.clear()
        window.bgcolor("#E394C0")
        pen.color("white")
        podium(4)

    elif check ==2 and userInput == 2:
        pen.up()
        pen.goto(0,0)
        pen.down()
        podium(2)
    elif check == 2 and userInput != 2:
        pen.up()
        pen.goto(0,0)
        pen.down()
        podium(5)

    elif check ==3 and userInput == 3:
        pen.up()
        pen.goto(0,0)
        pen.down()
        pen.write(f"Congratulations {name}, number {userInput} won and your choice was correct :)\n the turtle ran the race in {count} seconds "
        ,align="center",font=("Verdana", 25, "bold"))
        podium(3)
    elif check == 3 and userInput != 3:
        pen.up()
        pen.goto(0,0)
        pen.down()
        pen.write(f"Congratulations {name}, number {userInput} did not win. :)\n The turtle ran the race in {count} seconds "
        ,align="center",font=("Verdana", 25, "bold"))
        podium(6)

def podium(winner):
    # DISPLAYS WINNER
    window.clear()
    window.bgcolor("#E394C0")
    pen.color("white")
     # TURTLE 1
    turtle1 = turtle.Turtle()
    turtle1.color("#3498DB")
    turtle1.shape('turtle')
    turtle1.up()
    turtle1.hideturtle()

    # TURTLE 2
    turtle2 = turtle.Turtle()
    turtle2.color("#2ECC71")
    turtle2.shape('turtle')
    turtle2.up()
    turtle2.hideturtle()

    # TURTLE 3
    turtle3 = turtle.Turtle()
    turtle3.color("#E74C3C")
    turtle3.shape('turtle')
    turtle3.up()
    turtle3.hideturtle()
    if winner == 1:
        # ALL THE WINS AMOUNG TURTLES 
        window.clear()
        window.bgcolor("#E394C0")
        window.clear()
        window.bgcolor("#E394C0")
        pen.color("white")
        turtle1.up()
        turtle1.hideturtle()
        turtle1.goto(0,300)
        turtle1.lt(90)
        turtle1.showturtle()
        turtle1.down()
        turtle1.shapesize(5,5,10)
        pen.up()
        pen.goto(0,350)
        pen.down()
        pen.write("GOLD MEDAL FOR BLUE \n RAN IN "+ str(count)+" TURTLE SECONDS \n CONGRATS " + str(name) +" YOU DOUBLED YOUR MONEY",align="center",font=("Verdana",30,"bold"))
        
        # OTHER TURTLES
        # LEFT
        turtle2.up()
        turtle2.ht()
        turtle2.goto(0,175)
        turtle2.st()
        pen.up()
        pen.goto(0,200)
        pen.down()
        pen.write("NO MEDALS FOR GREEN",align="center",font=("Verdana",20,"bold"))
        # RIGHT
        turtle3.up()
        turtle3.ht()
        turtle3.goto(0,75)
        turtle3.st()
        pen.up()
        pen.goto(0,100)
        pen.down()
        pen.write("NO MEDALS FOR RED",align="center",font=("Verdana",20,"bold"))

    elif winner == 2:
        turtle2.up()
        turtle2.ht()
        turtle2.goto(0,300)
        turtle2.lt(90)
        turtle2.st()
        turtle2.shapesize(5,5,10)
        pen.up()
        pen.goto(0,350)
        pen.down()
        comment = pen.write(f"Congratulations {name}, you doubled your life savings. :)\n The turtle ran the race in {str(count)} turtle seconds "
        ,align="center",font=("Verdana", 25, "bold"))
        pen.write("GOLD MEDAL" + comment,align="center",font=("Verdana",50,"bold"))
        # OTHER TURTLES
        # LEFT
        turtle1.up()
        turtle1.ht()
        turtle1.goto(0,175)
        turtle1.st()
        pen.up()
        pen.goto(0,200)
        pen.down()
        pen.write("NO MEDALS ",align="center",font=("Verdana",20,"bold"))
        # RIGHT
        turtle3.up()
        turtle3.ht()
        turtle3.goto(0,75)
        turtle3.st()
        pen.up()
        pen.goto(0,100)
        pen.down()
        pen.write("NO MEDALS ",align="center",font=("Verdana",20,"bold"))

    elif winner ==3:
        turtle3.up()
        turtle3.ht()
        turtle3.goto(0,300)
        turtle3.lt(90)
        turtle3.st()
        turtle3.shapesize(7,7,12)
        pen.up()
        pen.goto(0,350)
        pen.down()
        pen.write("GOLD MEDAL FOR RED \n RAN IN "+ str(count)+" TURTLE SECONDS \n CONGRATS " + str(name) +" YOU DOUBLED YOUR MONEY",align="center",font=("Verdana",30,"bold"))
        # OTHER TURTLES
        # LEFT
        turtle1.up()
        turtle1.ht()
        turtle1.goto(0,175)
        turtle1.st()
        pen.up()
        pen.goto(0,200)
        pen.down()
        pen.write("NO MEDALS",align="center",font=("Verdana",20,"bold"))
        # RIGHT
        turtle2.up()
        turtle2.ht()
        turtle2.goto(0,75)
        turtle2.st()
        pen.up()
        pen.goto(0,100)
        pen.down()
        pen.write("NO MEDALS",align="center",font=("Verdana",20,"bold"))
    # ALL THE LOSES 
    elif winner ==4:
        pen.up()
        pen.goto(0,350)
        pen.down()
        pen.write(" BLUE WON A GOLD MEDAL",align="center",font=("Verdana",50,"bold"))
        pen.up()
        pen.goto(0,250)
        pen.down()
        pen.write(f"Congratulations {name}, you lost all of your live savings. :)\n The blue turtle ran the race in {count} turtle seconds "
        ,align="center",font=("Verdana", 27, "bold"))

        turtle2.up()
        turtle2.ht()
        turtle2.goto(0,175)
        turtle2.st()
        pen.up()
        pen.goto(0,200)
        pen.down()
        pen.write("NO MEDALS FOR GREEN",align="center",font=("Verdana",20,"bold"))
        # RIGHT
        turtle3.up()
        turtle3.ht()
        turtle3.goto(0,75)
        turtle3.st()
        pen.up()
        pen.goto(0,100)
        pen.down()
        pen.write("NO MEDALS FOR RED",align="center",font=("Verdana",20,"bold"))
    elif winner ==5:
        pen.up()
        pen.goto(0,350)
        pen.down()
        pen.write(" GREEN WON A GOLD MEDAL",align="center",font=("Verdana",50,"bold"))
        pen.up()
        pen.goto(0,250)
        pen.down()
        pen.write(f"Congratulations {name}, you lost all of your live savings. :)\n The Green turtle ran the race in {count} turtle seconds "
        ,align="center",font=("Verdana", 27, "bold"))

        # OTHER TURTLES
        # LEFT
        turtle1.up()
        turtle1.ht()
        turtle1.goto(0,175)
        turtle1.st()
        pen.up()
        pen.goto(0,200)
        pen.down()
        pen.write("NO MEDALS ",align="center",font=("Verdana",20,"bold"))
        # RIGHT
        turtle3.up()
        turtle3.ht()
        turtle3.goto(0,75)
        turtle3.st()
        pen.up()
        pen.goto(0,100)
        pen.down()
        pen.write("NO MEDALS ",align="center",font=("Verdana",20,"bold"))
        
    elif winner ==6:
        pen.up()
        pen.goto(0,350)
        pen.down()
        pen.write(" RED WON A GOLD MEDAL",align="center",font=("Verdana",50,"bold"))
        pen.up()
        pen.goto(0,250)
        pen.down()
        pen.write(f"Congratulations {name}, you lost all of your live savings. :)\n The RED turtle ran the race in {count} turtle seconds "
        ,align="center",font=("Verdana", 27, "bold"))

         # OTHER TURTLES
        # LEFT
        turtle1.up()
        turtle1.ht()
        turtle1.goto(0,175)
        turtle1.st()
        pen.up()
        pen.goto(0,200)
        pen.down()
        pen.write("NO MEDALS",align="center",font=("Verdana",20,"bold"))
        # RIGHT
        turtle2.up()
        turtle2.ht()
        turtle2.goto(0,75)
        turtle2.st()
        pen.up()
        pen.goto(0,100)
        pen.down()
        pen.write("NO MEDALS",align="center",font=("Verdana",20,"bold"))

        
    restart = window.textinput("RESTART", "Want to play again. (Y FOR YES, N FOR NO)")
    if restart == 'Y' or restart == 'y':
        pen.clear()
        window.bgcolor("#89CFF0")
        turtle1.ht()
        turtle2.ht()
        turtle3.ht()
        title()
    else:
        turtle.exitonclick()


# INITS ENTIRE RACE 
def raceInit():
    # BANNER ON TOP and FINISH LINE
    raceBanner()
    finishLine()
    # SPAWNS IN TURTLE and sets background
    init()
    time.sleep(1)
    # ASK USER FOR PREDICTION
    userInput = window.textinput("Prediction", "Who is going to win(1 for Blue , 2 for Green, and 3 for Red)")
    user = int(userInput)
    global name
    name = window.textinput("Name", "Enter your name.")
    pen.up()
    pen.goto(0,-400)
    pen.down()
    pen.write(f"ALL MY MONEY IS ON {user}!!",align="center",font=("Verdana", 30, "bold"))
    # STARTS
    race(user,name)

# STARTS RUNNING EVERYTHING
title()

# WHO YOU THINK IS GOING TO WIN -- USER INPUT

turtle.exitonclick()
