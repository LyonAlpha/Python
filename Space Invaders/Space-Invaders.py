# Space Invaders
# Press Ctrl + F5 to Play
import turtle
import math
import platform
import turtle
import winsound


# Set up the screen






wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
winsound.PlaySound("powerup.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
wn.tracer(0)

# Register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose a number of enemies
number_of_enemies = 30
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0


for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = enemy_start_x + (50 * enemy_number)
	y = enemy_start_y 
	enemy.setposition(x, y)
	# Update the enemy number
	enemy_number += 1
	if enemy_number == 10: 
    	
		enemy_start_y -= 50
		enemy_number = 0

    	
enemyspeed = 0.08


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("cyan")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 2

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


# Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

	
	
def fire_bullet():
	# Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
            winsound.PlaySound("laser.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
			
			
            bulletstate = "fire"
			# Move the bullet to the just above the player
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

def play_sound(sound_file, time = 0):
    if platform.system == "Windows":
	    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    if time > 0:
    	turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))











# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

# Main game loop
while True:
	wn.update()
		
	
	for enemy in enemies:
		# Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		# Move the enemy back and down
		if enemy.xcor() > 280:
			# Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			# Change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			# Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			# Change enemy direction
			enemyspeed *= -1
			
		# Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
					winsound.PlaySound("explosion.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

			# Reset the bullet
					bullet.hideturtle()
					bulletstate = "ready"
					bullet.setposition(0, -400)
				    # Reset the enemy
					enemy.setposition(0, 10000)
					# Update the score
					score += 10
					scorestring = "Score: %s" %score
					score_pen.clear()
					score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
			
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break

		
	# Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	# Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"








# Create keyboard bindings
	wn.listen()
	wn.onkeypress(move_left, "Left")
	wn.onkeypress(move_right, "Right")
	wn.onkeypress(fire_bullet, "space")
	wn.onkeypress(move_left, "a")
	wn.onkeypress(move_right, "d")
	wn.onkey(quit, "q")
	# Add Global Variable Running To Using Def "Quit" to Quit the Program without the Canvas Error
	
	running = True

	# Main game loop
	while running:
			
		
		for enemy in enemies:
			# Move the enemy
			x = enemy.xcor()
			x += enemyspeed
			enemy.setx(x)

			# Move the enemy back and down
			if enemy.xcor() > 280:
				# Move all enemies down
				for e in enemies:
					y = e.ycor()
					y -= 40
					e.sety(y)
				# Change enemy direction
				enemyspeed *= -1
			
			if enemy.xcor() < -280:
				# Move all enemies down
				for e in enemies:
					y = e.ycor()
					y -= 40
					e.sety(y)
				# Change enemy direction
				enemyspeed *= -1
				
			# Check for a collision between the bullet and the enemy
			if isCollision(bullet, enemy):
						winsound.PlaySound("explosion.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

				# Reset the bullet
						bullet.hideturtle()
						bulletstate = "ready"
						bullet.setposition(0, -400)
						# Reset the enemy
						enemy.setposition(0, 10000)
						# Update the score
						score += 10
						scorestring = "Score: %s" %score
						score_pen.clear()
						score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
				
			if isCollision(player, enemy):
				player.hideturtle()
				enemy.hideturtle()
				print ("Game Over")
				break

			
		# Move the bullet
		if bulletstate == "fire":
			y = bullet.ycor()
			y += bulletspeed
			bullet.sety(y)
		
		# Check to see if the bullet has gone to the top
		if bullet.ycor() > 275:
			bullet.hideturtle()
			bulletstate = "ready"

		if score == 300:
			print("You Win")
			exit()
		
		wn.update()


		
		
		
	


