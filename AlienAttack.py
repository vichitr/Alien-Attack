# Fun Game by Vichitr
# Developed in Python using pygame

# import the modules
import pygame,random,sys
from pygame.locals import *

# set the window size
WINDOWWIDTH = 900
WINDOWHEIGHT = 700

# set the colors
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0, 128,0)

# set the constant variables
FPS = 30
ALIENMINSPEED = 1
ALIENMAXSPEED = 4
ADDNEWALIENRATE = 10
ADDNEWALIEN1RATE = 20
ADDSUPERALIENRATE = 40
PLAYERMOVERATE = 5
ALIENSIZE = 50
BULLETSPEED = 4
NOSUPERBULLETS = 5
POWERUPRATE = 1000
POWERUPSIZE = 50
POWERUPSPEED = 4
ADDNEWLIFERATE = 3000
LIFESIZE = 50
PAUSE = False

def terminate():
	pygame.quit()
	sys.exit()
	
def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				return

# define a function to draw text on the screen
def drawText(text,font,surface, x, y):
	textobj= font.render(text, 1, TEXTCOLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

# set up pygame, the window and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Alien Attack')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None,48)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# set up images
playerImage1 = pygame.image.load('spaceship.png')
playerImage = pygame.transform.scale(playerImage1, (60,60))
playerRect = playerImage.get_rect()
alienImage = pygame.image.load('alien.png')
alien1Image = pygame.image.load('alien1.png')
superAlienImage = pygame.image.load('superalien.png')
lifeImage = pygame.image.load('life.png')
powerUpImage = pygame.image.load('powerup.png')
superBulletImage = pygame.image.load('superbullet.png')

# set up the background
background = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(background,(WINDOWWIDTH,WINDOWHEIGHT))
backgroundRect = backgroundImage.get_rect()

# show the start screen
drawText('Alien Attack',font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start!', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


highScore = 0
while True:
	# set up the start of the game
	aliens=[]
	aliens1=[]
	superAliens = []
	spaceshipBullets = []
	superBullets = []
	alienBullets = []
	superPower = []
	lifes = []
	score = 0
	levelUpScore = 1000
	level = 0
	LIFES = 3
	playerRect.topleft = (WINDOWWIDTH/2, WINDOWHEIGHT - 50)
	moveLeft = moveRight = moveUp = moveDown = False
	alienAddCounter = 0
	alien1AddCounter = 0
	superAlienAddCounter = 0
	superPowerCounter = 0
	newLifeCounter = 0
	pygame.mixer.music.play(-1,0.0)
	
	# update the background of the window
	windowSurface.blit(backgroundImage, backgroundRect)
	pygame.display.update()
	
	while True: # the game loop runs while the game part is playing
		
		# pause the game 
		while PAUSE == True: # wait till the player resumes the game
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == ord('p'):
						PAUSE = False
		
		# quit the game 
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
				
			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == ord('a'):
					moveRight = False
					moveLeft = True
				if event.key == K_RIGHT or event.key == ord('d'):
					moveLeft = False
					moveRight = True
				if event.key == K_UP or event.key == ord('w'):
					moveDown = False
					moveUp = True
				if event.key == K_DOWN or event.key == ord('s'):
					moveUp = False
					moveDown = True
				if event.key == K_SPACE:
					# create new bullets if space is pressed
					newSpaceshipBullet1 = pygame.Rect(playerRect.centerx-20, playerRect.centery+5, 3, 6)
					spaceshipBullets.append(newSpaceshipBullet1)
					newSpaceshipBullet2 = pygame.Rect(playerRect.centerx+15, playerRect.centery+5, 3, 6)
					spaceshipBullets.append(newSpaceshipBullet2)
				if event.key == K_LALT and NOSUPERBULLETS > 0:
					# use the super bullets when left alt is pressed
					newSuperBullet = {'rect': pygame.Rect(playerRect.centerx-12, playerRect.centery-50, 20, 50), 'surface': pygame.transform.scale(superBulletImage, (20,50))}
					superBullets.append(newSuperBullet)
					NOSUPERBULLETS -= 1
			
			if event.type == KEYUP:
				if event.key == K_ESCAPE: # exit the game
					terminate()
				if event.key == ord('p'): # pause the game
					PAUSE = True
					
				if event.key == K_LEFT or event.key == ord('a'):
					moveLeft = False
				if event.key == K_RIGHT or event.key == ord('d'):
					moveRight = False
				if event.key == K_UP or event.key == ord('w'):
					moveUp = False
				if event.key == K_DOWN or event.key == ord('s'):
					moveDown = False
					
			# move spaceship as mouse moves
			if event.type == MOUSEMOTION:
				playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
		
		# add aliens at the top of the screen
		alienAddCounter += 1
		if alienAddCounter == ADDNEWALIENRATE:
			alienAddCounter = 0
			newAlien = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - ALIENSIZE),0 - ALIENSIZE, ALIENSIZE, ALIENSIZE), 'speed': random.randint(ALIENMINSPEED,ALIENMAXSPEED),'surface': pygame.transform.scale(alienImage, (ALIENSIZE, ALIENSIZE))}
			aliens.append(newAlien)
		
		# add different type aliens 
		alien1AddCounter += 1
		if alien1AddCounter == ADDNEWALIEN1RATE:
			alien1AddCounter = 0
			newAlien1 = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - ALIENSIZE), 0 - ALIENSIZE, ALIENSIZE, ALIENSIZE), 'speed': random.randint(ALIENMINSPEED, ALIENMAXSPEED), 'surface': pygame.transform.scale(alien1Image,(ALIENSIZE, ALIENSIZE))}
			aliens1.append(newAlien1)
		
		# add super aliens 
		superAlienAddCounter += 1
		if superAlienAddCounter == ADDSUPERALIENRATE:
			superAlienAddCounter = 0
			newSuperAlien = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - ALIENSIZE), 0 - ALIENSIZE, ALIENSIZE, ALIENSIZE), 'speed': random.randint(ALIENMINSPEED, ALIENMAXSPEED), 'surface': pygame.transform.scale(superAlienImage, (ALIENSIZE, ALIENSIZE)), 'hit': 3}
			superAliens.append(newSuperAlien)
		
		# add powerups to increase no of super bullets
		superPowerCounter += 1
		if superPowerCounter == POWERUPRATE:
			superPowerCounter = 0
			newPower = {'rect': pygame.Rect(random.randint(0,WINDOWWIDTH - POWERUPSIZE), 0 - POWERUPSIZE, POWERUPSIZE, POWERUPSIZE), 'surface': pygame.transform.scale(powerUpImage, (POWERUPSIZE, POWERUPSIZE))}
			superPower.append(newPower)
		
		# add new powerup to increase the no of lifes
		newLifeCounter += 1
		if newLifeCounter == ADDNEWLIFERATE:
			newLifeCounter = 0
			newLife = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - LIFESIZE), 0 - LIFESIZE, LIFESIZE, LIFESIZE), 'surface': pygame.transform.scale(lifeImage, (LIFESIZE, LIFESIZE))}
			lifes.append(newLife)
		
		# move the spaceship around
		if moveLeft and playerRect.left > 0:
			playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
		if moveRight and playerRect.right < WINDOWWIDTH:
			playerRect.move_ip(PLAYERMOVERATE, 0)
		if moveUp and playerRect.top > 0:
			playerRect.move_ip(0, -1 * PLAYERMOVERATE)
		if moveDown and playerRect.bottom < WINDOWHEIGHT:
			playerRect.move_ip(0, PLAYERMOVERATE)
		
		# move the mouse cursor to match the player
		pygame.mouse.set_pos(playerRect.centerx,playerRect.centery)
		
		# move the aliens down
		for a in aliens:
			a['rect'].move_ip(0,a['speed'])
		
		for a1 in aliens1:
			a1['rect'].move_ip(0, a1['speed'])
		
		for sa in superAliens:
			sa['rect'].move_ip(0, sa['speed'])
		
		# move the powerups down
		for p in superPower[:]:
			p['rect'].move_ip(0, POWERUPSPEED)
		
		for l in lifes[:]:
			l['rect'].move_ip(0, POWERUPSPEED)
		
		# move the bullets up
		for b in spaceshipBullets:
			b.move_ip(0,-BULLETSPEED)
		
		for s in superBullets:
			s['rect'].move_ip(0,-BULLETSPEED)
		
		# delete bullets that have moved past the top
		for b in spaceshipBullets[:]:
			if b.top < 0:
				spaceshipBullets.remove(b)
		
		for s in superBullets[:]:
			if s['rect'].top <0:
				superBullets.remove(s)
		
		# delete aliens that have fallen past the bottom
		for a in aliens[:]:
			if a['rect'].top > WINDOWHEIGHT:
				aliens.remove(a)
		
		for a1 in aliens1[:]:
			if a1['rect'].top > WINDOWHEIGHT:
				aliens1.remove(a1)
		
		for sa in superAliens[:]:
			if sa['rect'].top > WINDOWHEIGHT:
				superAliens.remove(sa)
		
		# delete powerups that have fallen past the bottom 
		for l in lifes[:]:
			if l['rect'].top > WINDOWHEIGHT:
				lifes.remove(l)
		
		for p in superPower[:]:
			if p['rect'].top > WINDOWHEIGHT:
				superPower.remove(p)
		
		# draw the game world on the window
		windowSurface.blit(backgroundImage, backgroundRect)
		pygame.display.update()
		#windowSurface.fill(BACKGROUNDCOLOR)
		
		# draw the score, high score, Lifes and super bullets
		drawText('Score: %s' %(score), font, windowSurface, 10, 0)
		drawText('High Score: %s' %(highScore),font, windowSurface, 10,30)
		drawText('Super Bullets: %s' %(NOSUPERBULLETS),font, windowSurface, WINDOWWIDTH - 260, 30)
		drawText('Lifes: %s' %(LIFES), font, windowSurface, WINDOWWIDTH - 260, 0)
		
		# draw the spaceship
		windowSurface.blit(playerImage, playerRect)
		pygame.display.update()
		
		# draw the aliens
		for a in aliens:
			windowSurface.blit(a['surface'], a['rect'])
		
		for a1 in aliens1:
			windowSurface.blit(a1['surface'],a1['rect'])
		
		for sa in superAliens:
			windowSurface.blit(sa['surface'],sa['rect'])
		
		# draw the powerups
		for l in lifes:
			windowSurface.blit(l['surface'],l['rect'])
		
		# draw the bullets	
		for b in spaceshipBullets:
			pygame.draw.rect(windowSurface, BLUE, b, 0)
		
		for s in superBullets:
			windowSurface.blit(s['surface'], s['rect'])
		
		# draw the powerups
		for p in superPower:
			windowSurface.blit(p['surface'], p['rect'])
		
		# check if bullets have hit the aliens	
		for b in spaceshipBullets:
			for a in aliens:
				if b.colliderect(a['rect']):
					score += 10 # increase the score
					aliens.remove(a)
					spaceshipBullets.remove(b)
					break
		
		for b in spaceshipBullets:
			for a1 in aliens1:
				if b.colliderect(a1['rect']):
					score += 15 # increase the score
					aliens1.remove(a1)
					spaceshipBullets.remove(b)
					break
		
		for b in spaceshipBullets:
			for sa in superAliens:
				if b.colliderect(sa['rect']):
					sa['hit'] -= 1
					# check bullets have hit the super aliens 3 times
					if sa['hit'] > 0:
						spaceshipBullets.remove(b)
						break
					else:
						score += 30 # increase the score
						superAliens.remove(sa)
						spaceshipBullets.remove(b)
						break
		
		# if super bullets hit the aliens, increase more score
		for s in superBullets:
			for a in aliens:
				if s['rect'].colliderect(a['rect']):
					score += 20
					aliens.remove(a)
		
		for s in superBullets:
			for a1 in aliens1:
				if s['rect'].colliderect(a1['rect']):
					score += 30
					aliens1.remove(a1)
		
		for s in superBullets:
			for sa in superAliens:
				if s['rect'].colliderect(sa['rect']):
					score += 60
					superAliens.remove(sa)
		
		# if powerup is catched by spaceship
		for p in superPower:
			if playerRect.colliderect(p['rect']):
				if NOSUPERBULLETS < 9:
					NOSUPERBULLETS += 1
				superPower.remove(p)
		
		for l in lifes:
			if playerRect.colliderect(l['rect']):
				if LIFES < 3:
					LIFES += 1
				lifes.remove(l)
		
		# increase the difficulty if game proceeds
		if score >= levelUpScore:
			levelUpScore += 1000
			level += 1
			ALIENMINSPEED += 1
			ALIENMAXSPEED += 1
		
		# update the window
		pygame.display.update()
		
		# if aliens hit the spaceship decrease lifes
		for a in aliens:
			if playerRect.colliderect(a['rect']):
				aliens.remove(a)
				LIFES -= 1
		
		for a1 in aliens1:
			if playerRect.colliderect(a1['rect']):
				aliens1.remove(a1)
				LIFES -= 1
		
		for sa in superAliens:
			if playerRect.colliderect(sa['rect']):
				LIFES -= 1
				superAliens.remove(sa)

		# if lifes are zero, end the game
		if LIFES <= 0:
			if score > highScore:
				# set up high score
				highScore= score
			NOSUPERBULLETS = 5
			break
		
		mainClock.tick(FPS)
	
	# set the speed to the initial ones
	ALIENMINSPEED = 1
	ALIENMAXSPEED = 4
	
	# stop the game sound and play game over sound
	pygame.mixer.music.stop()
	gameOverSound.play()
	
	# show the 'Game Over' screen
	drawText('GAME OVER',font,windowSurface, (WINDOWWIDTH / 3),(WINDOWHEIGHT / 3))
	drawText('Press a key to play again.',font,windowSurface, (WINDOWWIDTH / 3) -80, (WINDOWHEIGHT / 3) + 50)
	pygame.display.update()
	waitForPlayerToPressKey()
	
	# stop the game over sound
	gameOverSound.stop()
