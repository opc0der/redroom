import pygame
import sys
import time
from settings import *
from assets import *

pygame.init()
keys = pygame.key.get_pressed()

def animation():
    global animCount
    if animCount + 1 >= 20:
        animCount = 0
    if left:
        screen.blit(walk_left[animCount // 5], (x, y))
        animCount += 1
    elif right:
        screen.blit(walk_right[animCount // 5], (x, y))
        animCount += 1
    elif up:
        screen.blit(walk_up[animCount // 5], (x, y))
        animCount += 1
    elif down:
        screen.blit(walk_down[animCount // 5], (x, y))
        animCount += 1
    else:
        screen.blit(player, (x, y))

shelf_rect = pygame.Rect(600, 150, 100, 10)
player_rect = pygame.Rect(x, y, 128, 128)
mirror_rect = pygame.Rect(400, 50, 100, 20)

def movement():
    global x
    global y
    global left
    global right
    global up
    global down
    global animCount
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 50:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_d] and x < 620:
        x += speed
        left = False
        right = True
    elif keys[pygame.K_w] and y > 50:
        y -= speed
        up = True
        down = False
    elif keys[pygame.K_s] and y < 400:
        y += speed
        down = True
        up = False
    else:
        left = False
        right = False
        animCount = 0

current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene

font = pygame.font.Font('fonts/press_start.ttf', 20)

def text_objects(text, font):
    text_surface = font.render(text, True, 'White')
    return text_surface, text_surface.get_rect()

def message_display(text, x, y):
    text_surf, text_rect = text_objects(text, font)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)




def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                switch_scene(scene1())
        message_display("Нажмите, чтобы начать игру", 400, 550)
        pygame.display.update()
        time.sleep(0.5)

        screen.blit(menu, (0, 0))
        message_display('RED.ROOM/', 400, 200)
        pygame.display.update()
        time.sleep(0.5)




def scene1():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        movement()
        animation()
        shelf_rect = pygame.Rect(600, 150, 100, 10)
        player_rect = pygame.Rect(x, y, 128, 128)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        if player_rect.colliderect(shelf_rect):
            message_display("Открыть шкаф (E)", 600, 100)

        if player_rect.colliderect(mirror_rect):
            message_display('Посмотреть в зеркало (E)', 400, 50)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(shelf_rect):
                switch_scene(shelf())
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(mirror_rect):
                switch_scene(mirror())
                running = False

        pygame.display.update()


def shelf():
    running = True
    while running:
        clock.tick(30)
        screen.blit(shelflook, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                switch_scene(shelf1())
                running = False
        pygame.display.update()

def shelf1():
    running = True
    while running:
        clock.tick(30)
        screen.blit(shelflook, (0, 0))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Что за....', 400, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                switch_scene(shelf2())
                running = False
        pygame.display.update()

def shelf2():
    running = True
    while running:
        clock.tick(30)
        screen.blit(shelflook, (0, 0))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Почему здесь кровь?...', 400, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                switch_scene(shelf3())
                running = False
        pygame.display.update()

def shelf3():
    running = True
    while running:
        clock.tick(30)
        screen.blit(shelflook, (0, 0))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Где мои вещи?...', 400, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                switch_scene(scene2())
                running = False
        pygame.display.update()

def scene2():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        movement()
        animation()
        shelf_rect = pygame.Rect(600, 150, 100, 10)
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        if player_rect.colliderect(shelf_rect):
            message_display("Открыть шкаф (E)", 600, 100)

        if player_rect.colliderect(mirror_rect):
            message_display('Посмотреть в зеркало (E)', 400, 50)

        if player_rect.colliderect(angel_rect):
            message_display('Поговорить (E)', 600, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(shelf_rect):
                switch_scene(shelf())
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(mirror_rect):
                switch_scene(mirror())
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene3())

        pygame.display.update()


def scene3():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Ты еще кто?', 400, 550)
        movement()
        animation()
        shelf_rect = pygame.Rect(600, 150, 100, 10)
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene4())

        pygame.display.update()

def scene4():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Какого черта здесь происходит?...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene5())

        pygame.display.update()

def scene5():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(angel_icon, (20, 500))
        message_display('Я твоя единственная надежда...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene6())

        pygame.display.update()

def scene6():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(angel_icon, (20, 500))
        message_display('...которая избавит тебя от твоих грехов...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene7())

        pygame.display.update()

def scene7():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(angel_icon, (20, 500))
        message_display('...и поможет выбраться из этого мира', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene8())

        pygame.display.update()

def scene8():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Что ты несешь?!', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene9())

        pygame.display.update()


def scene9():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Я что кислоты объелся!?', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene10())

        pygame.display.update()

def scene10():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Почему я тебя вижу?', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene11())

        pygame.display.update()


def scene11():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Такого не может быть...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene12())

        pygame.display.update()

def scene12():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(player_icon, (20, 500))
        message_display('Ты явно моя галлюцинация...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene13())

        pygame.display.update()


def scene13():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(angel_icon, (20, 500))
        message_display('Ты можешь думать что угодно...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene14())

        pygame.display.update()


def scene14():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(angel_icon, (20, 500))
        message_display('Но со мной ты обретешь покой...', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene15())

        pygame.display.update()


def scene15():
    running = True
    while running:
        global player_rect
        global shelf_rect
        global x
        global y
        global font
        global event
        clock.tick(30)
        screen.blit(bg, (0, 0))
        screen.blit(angel, (550, 350))
        screen.blit(window, (0, 500))
        screen.blit(angel_icon, (20, 500))
        message_display('...навсегда', 400, 550)
        movement()
        animation()
        player_rect = pygame.Rect(x, y, 128, 128)
        angel_rect = pygame.Rect(550, 350, 200, 200)
        font = pygame.font.Font('fonts/press_start.ttf', 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and player_rect.colliderect(angel_rect):
                switch_scene(scene1())

        pygame.display.update()

def mirror():
    running = True
    while running:
        screen.fill('Black')
        screen.blit(mirrorlook, (100, 0))
        message_display('Закрыть (X)', 400, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                switch_scene(scene1())
                running = False
        pygame.display.update()


switch_scene(main_menu())
while current_scene is not None:
    current_scene()

