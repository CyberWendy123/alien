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
	ship = Ship(ai_settings, screen)

	# start the main loop for the game 
	while True: 
		# watch for keyboard and mouse events
		gf.check_events(ship)
		ship.update() 
		gf.update_screen(ai_settings, screen, ship)

run_game() 