# step 1: first, we'll create an empty Pygame window (p 241)
#	this being the basic structure of a game written in Pygame: 
import pygame 

from settings import Settings 
from ship import Ship 
from alien import Alien
import game_functions as gf 
from pygame.sprite import Group 
from game_stats import GameStats 
from button import Button 

def run_game(): 
	# initialize game, settings, and screen obj 
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make the play button 
	play_button = Button(ai_settings, screen, "Let's Play")

	# Create an instance to store game statistics 
	stats = GameStats(ai_settings)

	# Make a ship, a group of bullets, and a group of aliens 
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group() 

	# Create the fleet of aliens 
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# start the main loop for the game 
	while True: 
		# watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)
		
		if stats.game_active: # aka game over option!
			ship.update() 
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game() 