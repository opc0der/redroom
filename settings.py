import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('red.room/')
# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

clock = pygame.time.Clock()

speed = 8
x = 300
y = 100


left = False
right = False
up = False
down = False
animCount = 0