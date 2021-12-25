# Press Ctrl F5 To Play

import turtle
import random
import winsound
import time


print("Press Q To Quit")
print("Press P To Pause")

# Set up screen
wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Side-Scrolling Shooter")
wn.tracer(0)

# Register shapes (images)
images = ["C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/player.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/enemy.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/boss.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/missile.gif",
          "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/red_star.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/white_star.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/yellow_star.gif"]
for image in images:
    wn.register_shape(image)




# Create classes
# Pen class for rendering Health Meters, Ammo Counter, and Score
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("green")
        self.width(2)
        self.speed(0)
        self.setheading(0)

    def health_meter(self):
        if player:
            self.goto(player.xcor() - 20, player.ycor() + 15)
            self.pendown()
            self.fd(40 * (player.health / player.max_health))
            self.penup()
            self.hideturtle()

        if enemies:
            self.goto(enemy.xcor() - 15, enemy.ycor() + 15)
            self.pendown()
            self.fd(30 * (enemy.health / enemy.max_health))
            self.penup()
            self.hideturtle()

    def ammo_counter(self):
        ammo = 0
        for missile in missiles:
            if missile.state == "ready":
                ammo += 1

            for x in range(ammo):
                self.goto(300 + 30 * x, 280)
                self.shape("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/missile.gif")
                self.stamp()

    def draw_score(self):
        self.goto(-80, 270)
        self.write(f"Score: {player.score}  Kills: {player.kills}", font=("Comic sans", 16, "normal"))


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/player.gif")
        self.penup()
        self.speed(0)
        self.goto(-350, 0)
        self.dy = 0
        self.dx = 0
        self.score = 0
        self.max_health = 20
        self.health = self.max_health
        self.kills = 0

    def up(self):
        self.dy = 1.25

    def down(self):
        self.dy = -1.25

    def move_left(self):
        self.dx = -1.25

    def move_right(self):
        self.dx = 1.25

    def move(self):
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)

    def stopx(self):
        self.dx = 0

    def stopy(self):
        self.dy = 0

    def rotate(self):
        player.lt(180)

        # Check for border collisions
        if self.ycor() > 280:
            self.sety(280)
            self.dy = 0

        elif self.ycor() < -280:
            self.sety(-280)
            self.dy = 0

        if self.xcor() < -380:
            self.setx(-380)
            self.dx = 0

        elif self.xcor() > -180:
            self.setx(-180)
            self.dx = 0


class Missile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/missile.gif")
        self.penup()
        self.speed(0)
        self.goto(0, 1000)
        self.dx = 0
        self.state = "ready"

    def fire(self):
        self.state = "firing"
        self.goto(player.xcor(), player.ycor())
        self.dx = 2.5

    def move(self):
        if self.state == "firing":
            self.setx(self.xcor() + self.dx)

        if self.xcor() > 400:
            self.state = "ready"
            self.sety(1000)


class Enemy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/enemy.gif")
        self.penup()
        self.speed(0)
        self.goto(random.randint(400, 480), random.randint(-280, 280))
        self.dx = random.randint(1, 3) / -3
        self.dy = 0
        self.max_health = 1
        self.health = self.max_health
        self.type = "enemy"

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # Border check
        if self.xcor() < -400:
            self.goto(random.randint(400, 480), random.randint(-280, 280))

        # Check for border collision
        if self.ycor() < -280:
            self.sety(-280)
            self.dy *= -1

        elif self.ycor() > 280:
            self.sety(280)
            self.dy *= -1

    # Spawn boss if conditions are met (see loop)
    def boss_spawn(self):
        self.shape("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/boss.gif")
        self.max_health = 1
            
        self.health = self.max_health

        if self.max_health == 0:
                print("You Win")
                exit()
        
        self.dy = random.randint(-5, 5) / 3


    # Respawn enemy if boss conditions are not met
    def enemy_respawn(self):
        self.dy = 0
        self.shape("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/enemy.gif")
        self.max_health = 1
        self.health = self.max_health

class Star(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        star_images = ["C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/yellow_star.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/red_star.gif", "C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/white_star.gif"]
        self.shape(random.choice(star_images))
        self.penup()
        self.speed(0)
        self.goto(random.randint(-400, 400), random.randint(-290, 290))
        self.dx = random.randint(1, 5) / -20

    def move(self):
        self.setx(self.xcor() + self.dx)

        # Border check
        if self.xcor() < -400:
            self.goto(random.randint(400, 480), random.randint(-290, 290))


# Create game objects
pen = Pen()
player = Player()
missiles = [Missile(), Missile(), Missile()]

enemies = []
for _ in range(5):
    enemies.append(Enemy())

stars = []
for _ in range(30):
    stars.append(Star())


# Check if missile is ready, then fire
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.fire()
            winsound.PlaySound("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/Missile.wav", winsound.SND_ASYNC)
            break


# Quit game function (q)
def quit_game():
    global running
    running = False

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

# Keyboard binding
wn.listen()
wn.onkeypress(quit_game, "q")
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.onkeypress(player.up, "w")
wn.onkeypress(player.down, "s")
wn.onkeypress(player.move_left, "a")
wn.onkeypress(player.move_right, "d")
wn.onkeypress(fire_missile, "space")
wn.onkeypress(fire_missile,"f")
wn.onkeypress(toggle_pause,"p")
wn.onkeyrelease(player.stopy, "Up")
wn.onkeyrelease(player.stopy, "Down")
wn.onkeyrelease(player.stopx, "Left")
wn.onkeyrelease(player.stopx, "Right")
wn.onkeyrelease(player.stopy, "w")
wn.onkeyrelease(player.stopy, "s")
wn.onkeyrelease(player.stopx, "a")
wn.onkeyrelease(player.stopx, "d")

# Main game loop
running = True

while running:
    if not is_paused:
        wn.update()
        pen.clear()

        # Update objects
        player.move()

        for missile in missiles:
            missile.move()

        for star in stars:
            star.move()

        for enemy in enemies:
            enemy.move()

            # Render health meters
            pen.health_meter()

            # Render the ammo counter
            pen.ammo_counter()

            # Check for collision
            for missile in missiles:
                if enemy.distance(missile) < 20:
                    winsound.PlaySound("C:/Users/Alpha/OneDrive/Desktop/Programs/Python Programs/Side Scrolling Shooter/explosion.wav", winsound.SND_ASYNC)
                    enemy.health -= 4
                    if enemy.health <= 0:
                        enemy.goto(random.randint(400, 480), random.randint(-280, 280))

                        player.kills += 1
                        if player.kills % 20 == 0:
                            enemy.boss_spawn()
                        else:
                            enemy.enemy_respawn() 

                    else:
                        enemy.setx(enemy.xcor() + 20)

                    # Reset missile
                    missile.dx = 0
                    missile.goto(0, 1000)
                    missile.state = "ready"

                    # Add to score
                    player.score += 10

            # Check for collision
            if enemy.distance(player) < 20:
                winsound.PlaySound("C:/Users/Alpha/OneDrive/Desktop/Python Programs/explosion.wav", winsound.SND_ASYNC)
                player.health -= random.randint(5, 10)
                enemy.health -= random.randint(5, 10)
                enemy.goto(random.randint(400, 480), random.randint(-280, 280))

                if player.health <= 0:
                    print("Game Over!")
                    exit()

                

        # Render the score
        pen.draw_score()

    else:
        wn.update()