
from PIL import Image 
import pygame
from bullet import *
from player import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def can_shoot():
    if len(bullet_list) < 3:
        return True
    return False




def update():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    grungus = player()
    speed = 3
    delta_time = 1
    sprite_rect = grungus.sprite.get_rect()
    mouse_down = None
    frames = 0
    shot_time = 0
    



    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        frames += 1
        curr_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                print("\nmousedown\n")
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                print("\nmouseup\n")    

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE
        screen.blit(grungus.sprite, sprite_rect)




        mouse_pos = pygame.mouse.get_pos()
        if mouse_down and can_shoot() and (curr_time - shot_time >= fire_delay):
            bullet_list.append(bullet(grungus.position))
            shot_time = pygame.time.get_ticks()
            

        for bullets in bullet_list:
            bullets.position = (bullets.position[0] + bullets.speed, bullets.position[1])
            screen.blit(bullets.sprite, bullets.position)



        #get_pressed(): returns boolean sequence representing state of currently pressed buttons as array
        keys = pygame.key.get_pressed()
        #checks for W, A, S, and D in keys array, increment or decrements the sprite_rect x or y. does nothing if edges of scrren are reached.
        if keys[pygame.K_w] and sprite_rect.y > 0:
            sprite_rect.y -= speed * delta_time
        if keys[pygame.K_s]:
            sprite_rect.y += speed * delta_time
        if keys[pygame.K_a]:
            sprite_rect.x -= speed * delta_time
        if keys[pygame.K_d]:
            sprite_rect.x += speed * delta_time

        grungus.position = pygame.Vector2(sprite_rect.x, sprite_rect.y)

        # print(grungus.position)
        print(bullet_list)

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
