# I am having a bit of trouble changing the background situation 
# this is to better troubleshoot this problem 
import sys, pygame 
pygame.init() 

size = width, height = 600, 400 
color = 100, 0, 0 
white = (255, 255, 255)

screen = pygame.display.set_mode(size)
#ship = pygame.image.load("./images/ship.png")
pygame.display.set_caption("background")

n = pygame.display.get_init()
print(n) # so it is working...
print(pygame.display.get_surface()) # yes, surface is set 
print(pygame.display.Info()) # more information 

x = 0 
y = 0 
while 1: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(color)
	#screen.blit(ship, (200, 200))

	pygame.display.flip()
# seems like I coded properly but something on my computer is the problem (aug 22)
# fuck...I was right...info found here: 
# https://github.com/pygame/pygame/issues/555 
# see! sometimes it's not my fault! 
# homebrew just did not have a compatible verison that ruined everything!!!! 
# but with the power of using google...and not giving up, I found the answer! hahahaha!