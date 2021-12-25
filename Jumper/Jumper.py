import turtle
import random

# Line Below Represents Number of Enemies that Will Be On The Screen


number_of_enemies = 10

print("")
print("")
print("The Floor and Roof Are Lava")
print("Avoid The Red Line. The Top of the Screen, And The Red Enemies")
print("Be Careful, Sometimes The Gravity")
print("Press Q To Quit")
print("Press P To Pause")

wn = turtle.Screen()
wn.title("Jumper")
wn.bgcolor("blue")
wn.setup(height=600, width=800)
wn.tracer(0)

GROUND_LEVEL = -200
ROOF_LEVEL = 265

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        # Draw ground
        self.ht()
        self.speed(0)
        self.pensize(3)
        self.shape("square")
        self.color("white")
        self.penup()

        # Draw line
        self.pencolor("red")
        self.goto(-400, GROUND_LEVEL)
        self.pendown()
        self.goto(400, GROUND_LEVEL)
        self.penup()
        self.pencolor("red")
        self.goto(-400, ROOF_LEVEL)
        self.pendown()
        self.goto(400, ROOF_LEVEL)
        self.penup()

class Jumper(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("green")
        self.penup()
        self.height = 20
        self.width = 20
        self.dy = 0
        self.dx = 0
        self.state = "ready"
        self.goto(-350, 0)

class Enemy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.rt(90)
        self.shape("circle")
        self.color("red")
        self.penup()
        x = 365
        y = random.randint(-195, 245)
        self.goto(x, y)
        self.dx = random.uniform(0.05, 0.07)    

    def move(self):
        self.setx(self.xcor() - self.dx)


# Create Sprites

jumper = Jumper()
pen = Pen()


class Hidden_Missile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("classic")
        self.penup()
        self.speed(0)
        self.goto(0, 1000)
        self.dx = 0
        self.state = "ready"

    def fire(self):
        self.state = "firing"
        self.goto(jumper.xcor(), jumper.ycor())
        self.dx = 0.25

    def move(self):
        if self.state == "firing":
            self.setx(self.xcor() + self.dx)

        if self.xcor() > 400:
            self.state = "ready"
            self.sety(1000)

missile = Hidden_Missile()

# Create Multiple Enemies

enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

gravity = -0.0023456789

def jump():
    if jumper.state == "ready":
        jumper.dy = 0.5

def quit():
    global running
    running = False

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True




wn.listen()
wn.onkeypress(jump, "space")
wn.onkeypress(quit, "q")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(missile.fire, "f")

running = True

while running:
    if not is_paused:
        wn.update()

        missile.move()

        for enemy in enemies:

            enemy.move()

            if enemy.distance(jumper) < 20:
                jumper.ht()
                
                exit



            if enemy.xcor() < -365:
                enemy.setx(365)
                gravity = -0.001
                jumper.dy = 0

            if enemy.xcor() == 350:
                gravity = -0.0023456789
                jumper.dy = 0.5

            # Check For A Collision With The Arrow And The Missile

            if missile.distance(enemy) < 20:
                enemy.ht()
                missile.ht()
                enemy.goto(365, y)
                enemy.st()
                missile.dx = 0
                missile.goto(0, 1000)
                missile.state = "ready"
                missile.st()

        # Gravity
        jumper.dy += gravity 

        # Move the Jumper
        y = jumper.ycor()
        y += jumper.dy
        jumper.sety(y)

        if jumper.ycor() < GROUND_LEVEL + jumper.height / 2:
            jumper.sety(GROUND_LEVEL + jumper.height / 2)
            jumper.dy = 0

        if jumper.ycor() > 265:
            jumper.ht()
            print("Game Over")
            break 

        if jumper.ycor() == GROUND_LEVEL + jumper.height / 2:
            jumper.ht()
            print("Game Over")
            break

    else:
        wn.update()  