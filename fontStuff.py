import pygame
pygame.init()
pygame.font.init()
FPS = 1
clock = pygame.time.Clock()
M = input('Minute ')
TM = input('Minutes ')
H = input('Hours ')
RED = (179, 0, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((300, 300))

font = pygame.font.SysFont(None, 10)
text = font.render('test', True, RED)
    
running = True
while running:
    clock.tick(FPS)
    screen.blit(text, (150, 150))
    pygame.display.update()