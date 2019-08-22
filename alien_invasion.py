# step 1: first, we'll create an empty Pygame window (p 241)
#	this being the basic structure of a game written in Pygame: 
import sys 
import pygame 

def run_game(): 
	# initialize game and create a screen obj 
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Alien Invasion")

	# Set the background color (step 2)
	bg_color = (230, 230, 230)

	# start the main loop for the game 
	while True: 
		# watch for keyboard and mouse evenets 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()
		
		# Redraw the screen during each pass through the loop 
		screen.fill(bg_color)

		# Make the most recently drawn screen visible 
		pygame.display.flip()

run_game() 