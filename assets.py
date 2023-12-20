import pygame
pygame.init()
player = pygame.image.load('images/player.png')
angel = pygame.image.load('images/angel.png')

player_icon = pygame.image.load('images/playericon.png')
angel_icon = pygame.image.load('images/angelicon.png')

bg = pygame.image.load('images/background.png')
bg = pygame.transform.scale(bg, (800, 600))
# button_sound = pygame.mixer.Sound('sounds/button.mp3')

mirrorlook = pygame.image.load('images/mirrorlook.jpg')
mirrorlook = pygame.transform.scale(mirrorlook, (600, 600))

shelflook = pygame.image.load('images/shelf.png')
shelflook = pygame.transform.scale(shelflook, (800, 600))

menu = pygame.image.load('images/menu.png')
menu = pygame.transform.scale(menu, (800, 600))
window = pygame.Surface((800, 100))
window.fill('Black')




walk_left = [
    pygame.image.load('images/player_left/player_left1.png'),
    pygame.image.load('images/player_left/player_left2.png'),
    pygame.image.load('images/player_left/player_left3.png'),
    pygame.image.load('images/player_left/player_left2.png')
]

walk_right = [
    pygame.image.load('images/player_right/player_right1.png'),
    pygame.image.load('images/player_right/player_right2.png'),
    pygame.image.load('images/player_right/player_right3.png'),
    pygame.image.load('images/player_right/player_right2.png')
]

walk_up = [
    pygame.image.load('images/player_up/player_up1.png'),
    pygame.image.load('images/player_up/player_up2.png'),
    pygame.image.load('images/player_up/player_up1.png'),
    pygame.image.load('images/player_up/player_up3.png')
]

walk_down = [
    pygame.image.load('images/player_down/player_down1.png'),
    pygame.image.load('images/player_down/player_down2.png'),
    pygame.image.load('images/player_down/player_down1.png'),
    pygame.image.load('images/player_down/player_down3.png'),

]

