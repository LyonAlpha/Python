pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

stop_animation = False



import turtle
import math
import random

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH + 220, SCREEN_HEIGHT + 20, startx=-0.5, starty=0)
wn.title("Space Arena")
wn.bgcolor("black")

canvas = wn.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

if stop_animation == True:
    wn.tracer(0)

else:
    pass
    
score = 0

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.state = "splash"

    def start_level(self):
        sprites.clear()

        # Add Enemy Missiles

        for enemy_missile in enemy_missiles:
            sprites.append(enemy_missile)


        # Add Player
        sprites.append(player)

        # Add Missile
        for missile in missiles:
            sprites.append(missile)

        # Add Enemies
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.uniform(-0.3, 0.3)
            dy = random.uniform(-0.3, -0.3)
            sprites.append(Enemy(x, y, "square", "red"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

        # Add Powerups

        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.uniform(-0.3, 0.3)
            dy = random.uniform(-0.3, -0.3)
            sprites.append(Powerup(x, y, "circle", "blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def render_border(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        pen.penup()
        
        left = -self.width/2.0 - x_offset
        right = self.width/2.0 - x_offset
        top = self.height/2.0 - y_offset
        bottom = -self.height/2.0 -y_offset
        
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    def render_info(self, pen, score, active_enemies = 0):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()

        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)

        pen.penup()
        pen.color("white")
        character_pen.scale = 1.0
        character_pen.draw_string(pen, "SPACE ARENA", 400, 270)
        character_pen.draw_string(pen, "SCORE- {}".format(score), 400, 240)
        character_pen.draw_string(pen, "ENEMIES- {}".format(active_enemies), 400, 210)
        character_pen.draw_string(pen, "LIVES- {}".format(player.lives), 400, 180)
        character_pen.draw_string(pen, "LEVEL- {}".format(game.level), 400, 150)
        
    
    def start(self):
        self.state = "playing"




class CharacterPen():
    def __init__(self, color, scale = 1.0):
        self.color = color
        self.scale = scale
        self.color = "white"
        
        self.characters = {}
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))

        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))   
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))   
        
        self.characters["-"] = ((-3, 0), (3, 0)) 
        
    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color)
        
        # Center text
        x -= 15 * self.scale * ((len(str)-1) / 2)
        for character in str:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

        
    def draw_character(self, pen, character, x, y):
        scale = self.scale
        
        if character in "abcdefghijklmnopqrstuvwxyz":
            scale *= 0.8
        
        character = character.upper()
        
        # Check if the character is in the dictionary
        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.penup()

# Splash Screen



character_pen = CharacterPen("white", 3.0)
character_pen.color = "red"
character_pen.draw_string(pen, "SPACE ARENA", 0, 160)

character_pen.scale = 1.0
character_pen.draw_string(pen, "By LyonAlpha", 0, 100)

# Draw (Main) Splash Screen



pen.color("white")
pen.shape("triangle")
pen.goto(-150, 20)
pen.stamp()
character_pen.color = "white"
character_pen.draw_string(pen, "Player", -150, -20)

pen.color("red")
pen.shape("square")
pen.goto(-14, 20)
pen.stamp()
character_pen.color = "red"
character_pen.draw_string(pen, "Enemy", -12, -20)

pen.shape("circle")
pen.color("blue")
pen.goto(125, 20)
pen.stamp()
character_pen.color = "blue"
character_pen.draw_string(pen, "Powerup", 125, -20)

pen.pencolor("white")
character_pen.color = "red"
character_pen.draw_string(pen, "Up Arrow   -", -100, -60)
character_pen.draw_string(pen, "Accelerate", 100, -60)

character_pen.draw_string(pen, "Down Arrow  - ", -100, -100)
character_pen.draw_string(pen, "Decelerate", 100, -100)

character_pen.draw_string(pen, "Left Arrow  - ", -100, -140)
character_pen.draw_string(pen, "Rotate Left", 100, -140)

character_pen.draw_string(pen, "Right Arrow - ", -100, -180)
character_pen.draw_string(pen, "Rotate Right", 100, -180)

character_pen.draw_string(pen, "Space      -", -100, -220)
character_pen.draw_string(pen, "Fire", 100, -220)

character_pen.scale = 1.0
character_pen.draw_string(pen, "Press Q to Quit", 0, -280)
character_pen.draw_string(pen, "Press S to Start", 0, -310)

wn.tracer(0)

class Sprite():
    # Constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.0025
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20
        self.state = "active"
        self.radar = 200
        self.max_dx = 0.5
        self.max_dy = 0.5

    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy
        
        other.dx = temp_dx
        other.dy = temp_dy


    def update(self):
        self.heading += self.da
        self.heading %= 360
        
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
        self.x += self.dx
        self.y += self.dy
        
        self.border_check()
        
    def border_check(self):
        if self.x > game.width/2.0 - 10:
            self.x = game.width/2.0 - 10
            self.dx *= -1
            
        elif self.x < -game.width/2.0 + 10:
            self.x = -game.width/2.0 + 10
            self.dx *= -1

        if self.y > game.height/2.0 - 10:
            self.y = game.height/2.0 - 10
            self.dy *= -1
            
        elif self.y < -game.height/2.0 + 10:
            self.y = -game.height/2.0 + 10
            self.dy *= -1            
        
    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
        
            self.render_health_meter(pen, x_offset, y_offset)
        
    def render_health_meter(self, pen, x_offset, y_offset):
        # Draw health meter
        pen.goto(self.x -x_offset - 10, self.y -y_offset + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)
        
        if self.health/self.max_health < 0.3:
            pen.color("red")
        elif self.health/self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20.0 * (self.health/self.max_health))
        
        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health-self.health)/self.max_health))
        
        pen.penup()
        
class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0

    def rotate_left(self):
        self.da = 5

    def rotate_right(self):
        self.da = -5

    def stop_rotate(self):
        self.da = 0

    def accelerate(self):
        self.thrust += self.acceleration

    def decelerate(self):
        self.thrust = 0

    def antiaccelerate(self):
        self.thrust -= self.acceleration

    def antidecelerate(self):
        self.thrust = 0

    def fire(self):
        num_of_missiles = 0
        for missile in missiles:
            if missile.state == "ready":
                num_of_missiles += 1
                
    def fire(self):
        num_of_missiles = 0
        for missile in missiles:
            if missile.state == "ready":
                num_of_missiles += 1
        
        # 1 missile ready
        if num_of_missiles == 1:
            for missile in missiles:
                if missile.state == "ready":
                    missile.fire(self.x, self.y, self.heading, self.dx, self. dy)
            
        # 2 missiles ready
        if num_of_missiles == 2:
            directions = [-5, 5]
            for missile in missiles:
                if missile.state == "ready":
                    missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self. dy)
                    
        # 3 missiles ready        
        if num_of_missiles == 3:
            directions = [0, -5, 5]
            for missile in missiles:
                if missile.state == "ready":
                    missile.fire(self.x, self.y, self.heading +directions.pop(), self.dx, self. dy)

    def stop(self):
        self.dx = 0
        self.dy = 0



    def update(self):
    
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            
            self.x += self.dx
            self.y += self.dy
            
            self.border_check()
            
            # Check Health

            if self.health <= 0:
                print("Player Disintegrated")
                exit()

    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.max_health
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1


    def render(self, pen, x_offset, y_offset):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        pen.shapesize(1.0, 1.0, None)

        self.render_health_meter(pen, x_offset, y_offset)

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.fuel_level = 6
        self.fuel = self.fuel_level
        self.thrust = 0.08

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()

            self.heading += self.da
            self.heading %= 360
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            
            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.fuel_level
        self.dx = 0
        self.dy = 0
        self.state = "ready"
        

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            pen.shapesize(1.0, 1.0, None)


class EnemyMissile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.fuel_level = 6
        self.fuel = self.fuel_level
        self.thrust = 0.08

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()

            self.heading += self.da
            self.heading %= 360
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            
            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.fuel_level
        self.dx = 0
        self.dy = 0
        self.state = "ready"
        

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            pen.shapesize(1.0, 1.0, None)


class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = 20
        self.health = self.max_health
        self.type = random.choice(["hunter", "mine", "surveillance"])

        if self.type == "hunter":
            self.color = "red"
            self.shape = "square"

        elif self.type == "mine":
            self.color = "orange"
            self.shape = "square"

        elif self.type == "surveillance":
            self.color = "pink"
            self.shape = "square"

        # Set Max Speed

        if self.dx > self.max_dx:
            self.dx = self.max_dx

        elif self.dx < -self.max_dx:
            self.dx = -self.max_dx

        if self.dy > self.max_dy:
            self.dy = self.max_dy

        elif self.dy < -self.max_dy:
            self.dy = -self.max_dy

    def update(self):
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            
            self.x += self.dx
            self.y += self.dy
            
            self.border_check()
            
            # Check Health

            if self.health <= 0:
                self.reset()

            # Code For Different Types
            if self.type == "hunter":
                if self.x < player.x:
                    self.dx += 0.005
                
                else:
                    self.dx -= 0.005

                if self.y < player.y:
                    self.dy += 0.005

                else:
                    self.dy -= 0.005

            
            elif self.type == "mine":
                self.dx = 0
                self.dy = 0

            elif self.type == "surveillance":
                if self.x < player.x:
                    self.dx -= 0.005
                
                else:
                    self.dx += 0.005

                if self.y < player.y:
                    self.dy -= 0.005

                else:
                    self.dy += 0.005

    def reset(self):
        self.state = "inactive"
        
class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, pen, sprites):



        # Draw Radar Circle
        pen.color("white")
        pen.setheading(90)
        pen.goto(self.x + self.width / 2.0, self.y)
        pen.pendown()
        pen.circle(self.width / 2.0)
        pen.penup()

        # Draw Sprites
        for sprite in sprites:
            if sprite.state == "active":
                radar_x = self.x + (sprite.x - player.x) * (self.width/game.width)
                radar_y = self.y + (sprite.y - player.y) * (self.height/game.height)
                pen.goto(radar_x, radar_y)
                pen.color(sprite.color)
                pen.shape(sprite.shape)
                pen.shapesize(0.1, 0.1, None)
                pen.setheading(sprite.heading)

                # Make Sure Sprite Is Close To The Player
                distance = ((player.x-sprite.x)**2 + (player.y-sprite.y)**2)**0. 
                if distance < player.radar:

                    pen.stamp()

# Create game object
game = Game(700, 500)

# Create radar Object

radar = Radar(400, -200, 200, 200)

# Create player sprite
player = Player(0, 0, "triangle", "white")

# Create camera "Object"?

camera = Camera(player.x, player.y)

# Create missile object

missiles = []
for _ in range(3):
    missiles.append(Missile(0, 100, "circle", "cyan"))

enemy_missiles = []
for _ in range(1):
    enemy_missiles.append(EnemyMissile(0, 100, "circle", "red"))

# Sprites list
sprites = []

# Setup the level

game.start_level()

# Create Quit and Pause Function

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
    


# Create Keyboard Bindings

wn.listen()
wn.onkeypress(quit, "q")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")
wn.onkeyrelease(player.stop_rotate, "Left")
wn.onkeyrelease(player.stop_rotate, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")
wn.onkeypress(player.antiaccelerate, "Down")
wn.onkeyrelease(player.antidecelerate, "Down")
wn.onkeypress(player.rotate_left, "a")
wn.onkeypress(player.rotate_right, "d")
wn.onkeyrelease(player.stop_rotate, "a")
wn.onkeyrelease(player.stop_rotate, "d")
wn.onkeypress(player.accelerate, "w")
wn.onkeyrelease(player.decelerate, "w")
wn.onkeypress(player.antiaccelerate, "s")
wn.onkeyrelease(player.antidecelerate, "s")
wn.onkeypress(player.fire, "space")
wn.onkeypress(game.start, "s")
wn.onkeypress(game.start, "S")

# For Beta Testing ONLY

wn.onkeypress(player.stop, "z")


# Main Loop

running = True

while running:
    if not is_paused:
        if game.level < 10:

            # Splash
            if game.state == "splash":
                wn.update()

            elif game.state == "playing":

                # Clear screen
                pen.clear()
                
                # Do game stuff
                
                # Update sprites
                for sprite in sprites:
                    sprite.update()       

                # Fire Enemy Missiles
                for enemy_missile in enemy_missiles:
                    if enemy_missile.state == "ready":
                        # Fire The Missiles
                        # Find All Enemies
                        enemies = []
                        for sprite in sprites:
                            if isinstance(sprite, Enemy):
                                enemies.append(sprite)
                                
                        enemy = random.choice(enemies)
                                
                        # Set Heading
                        heading = math.atan2(player.y-enemy.y, player.x-enemy.x)
                        heading = heading * (180/pi)
                        enemy_missile.fire(enemy.x, enemy.y, heading, enemy.dx, enemy.dy)
                        # print(enemy_missile.heading)
                    

                # Check for collisions
                for sprite in sprites:
                    if isinstance(sprite, Enemy)  and sprite.state == "active":
                        if player.is_collision(sprite):
                            sprite.health -= 10
                            player.health -= 10
                            player.bounce(sprite)


                        for missile in missiles:
                            if missile.state == "active" and missile.is_collision(sprite):
                                sprite.health -= 10
                                score += 10
                                missile.reset()
                            
                    if isinstance(sprite, Powerup):
                        if player.is_collision(sprite):
                            sprite.x = 100
                            sprite.y = 100
                            if player.health < player.max_health:
                                player.health += 10

                            
                            
                        for missile in missiles:
                            if missile.state == "active" and missile.is_collision(sprite):
                                sprite.x = 100
                                sprite.y = -100
                                missile.reset()

                    # Enemy Missile Collision With The Player
                    if isinstance(sprite, EnemyMissile):
                        if sprite.state == "active" and sprite.is_collision(player):
                            sprite.reset()
                            player.health -= 10                    

                # Render sprites
                for sprite in sprites:
                    sprite.render(pen, camera.x - 100, camera.y)
                
                game.render_border(pen, camera.x - 100, camera.y)

                # Check For End Of Level
                end_of_level = True

                for sprite in sprites:

                    # Look For An Active Enemy

                    if isinstance(sprite, Enemy) and sprite.state == "active":
                        end_of_level = False

                if end_of_level:
                    game.level += 1
                    game.start_level()

                
                # Update The Camera

                camera.update(player.x , player.y)

                # Draw Text
                game.render_info(pen, 0, 0)

                # Render The Radar

                radar.render(pen, sprites)

                # Update the screen
                
                wn.update()
        else:
            print("You Win")
            exit()

    else:
        wn.update()