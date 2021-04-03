#Space Invaders

import turtle
#turtle is a pre-installed Python library that enables users to
#create pictures and shapes by providing them with a virtual canvas.
#The onscreen pen that you use for drawing
#is called the turtle and this is what gives the library its name.

import os
#The OS module in Python provides functions for interacting with the
#operating system.
#OS comes under Python's standard utility modules.

import math
import random

#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("pokeball.gif")

#Register the shapes
turtle.register_shape("pika.gif")
turtle.register_shape("greninja.gif")
turtle.register_shape("yellowline.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)#0 is the fastest speed
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
#The pen originially starts at the
#center (0,0), but now we are making the pen start at bottom left.
border_pen.pendown()
border_pen.pensize(3)#makes the pen size thicker
for side in range (4):
    border_pen.fd(600)#moves the pen forwards 600 pixels
    border_pen.lt(90)#moves pen left 90 degrees
border_pen.hideturtle()#the pen is called turtle so then we hide the pen.

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Draw my name
myname_pen = turtle.Turtle()
myname_pen.speed(0)
myname_pen.color("red")
myname_pen.penup()
myname_pen.setposition(-500, 280)
mynamestring = "BY SAMI BAJWA" 
myname_pen.write(mynamestring, False, align = "left", font=("Arial", 14, "normal"))
myname_pen.hideturtle()


#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("pika.gif")
player.penup()
player.speed()
player.setposition(0, -250)
#player.setheading(90)

playerspeed = 15

#Choose a number of enemies
number_of_enemies = 4

#Create an empty list
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):#for loop iterating 5 times
    #Create the enemy
    enemies.append(turtle.Turtle())#appends enemies 5 times

for enemy in enemies: #enemy = an red circular object. enemies = 5
    enemy.color("red")
    enemy.shape("greninja.gif")
    enemy.penup()
    enemy.speed(0)
    #To have the new enemies in random areas within the boundaries below
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemyspeed = 5

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
bulletstate = "ready"


#Move the player left and right
def move_left():
    x = player.xcor()#should be 0 at start of game
    x -= playerspeed #x -= 15 so 0 -= 15 = -15
    if x < -280:
        x = -280
    player.setx(x)#changes location to new x so now it's at -15

def move_right():
    x = player.xcor()#should be 0 at start of game
    x += playerspeed #x += 15 so 0 += 15 = +15
    if x > 280:
        x = 280
    player.setx(x)#changes location to new x so now it's at +15

def fire_bullet():
    #Declare bulletstate as glabal if it needs changing
    global bulletstate
    if bulletstate == "ready":
        #bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
#Create keyboard bindings
turtle.listen()#tells keyboard to listen
turtle.onkey(move_left, "Left")#Left arrow key => move_left
turtle.onkey(move_right, "Right")#Right arrow key => move_right
turtle.onkey(fire_bullet, "space")#Fires bullet when presses space

#Main game loop
while True:
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()#gets current x coordinate of enemy
        x+= enemyspeed#adds enemy speed (which we set to 2)
        enemy.setx(x)#We set the x coordinate to the new x coordinate
        
        #Move the enemy back and down
        if enemy.xcor() > 280:#if the enemy reaches the right boundary
            for e in enemies:
                #Moves all enemies down
                y = e.ycor()#Gets current y coordinate of enemy
                y -= 40#Decreases enemy y coordinate by 40 (drops the enemy down)
                e.sety(y)#Sets the enemy's y position to what we calculated ^
            #Change enemy direction
            enemyspeed *= -1#Change its speed to opposite direction
            
        if enemy.xcor() < -280:#if the enemy reaches the left boundary
            for e in enemies:
                #Moves all enemies down
                y = e.ycor()#Gets current y coordinate of enemy
                y -= 40#Decreases enemy y coordinate by 40 (drops the enemy down)
                e.sety(y)#Sets the enemy's y position to what we calculated ^
            #Change enemy direction
            enemyspeed *= -1#Change its speed to opposite direction

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))


        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    #if bulletstate == "fire":
    if bulletstate == "ready":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


            
delay = raw_input("Press enter to finish.")
