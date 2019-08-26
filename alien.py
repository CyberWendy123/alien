# via pg 267 - creating the alien class 
import pygame 
from pygame.sprite import Sprite 

class Alien(Sprite): 
	""" A class to present a single alien in the fleet. """ 
	def __init__(self, ai_settings, screen): 
		""" Initialize the alien and set its staring position """
		super(Alien, self).__init__() 
		self.screen = screen
		self.ai_settings = ai_settings 

		# Load the alien image and set its rect attribute 
		self.image = pygame.image.load("images/alien.png")
		self.image = pygame.transform.scale(self.image , (50, 30))
		self.rect = self.image.get_rect() 

		# Start each new alien near the top left on the screen 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height 

		# Store the alien's exact position 
		self.x = float(self.rect.x)

	def blitme(self): 
		""" Draw the alien at its current location. """
		self.screen.blit(self.image, self.rect)

	def update(self): 
		""" Move the alien right. """
		self.x += self.ai_settings.alien_speed_factor 
		self.rect.x = self.x  