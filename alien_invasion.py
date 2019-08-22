# step 1: first, we'll create an empty Pygame window (p 241)
#	this being the basic structure of a game written in Pygame: 
import pygame 

from settings import Settings 
from ship import Ship 
import game_functions as gf 

def run_game(): 
	# initialize game, settings, and screen obj 
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make a ship 
	ship = Ship(screen)

	# start the main loop for the game 
	while True: 
		# watch for keyboard and mouse events
		gf.check_events()
		
		# Redraw the screen during each pass through the loop 
		screen.fill(ai_settings.bg_color)
		pygame.display.update() # refresh the screen 
		ship.blitme()

		# Make the most recently drawn screen visible 
		pygame.display.flip()

run_game() 