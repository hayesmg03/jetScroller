import os
import random
import pygame as pg
from bullet import *
from player import *
from enemy import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
data_dir = "images/"




def load_image(name, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert_alpha()
    return image, image.get_rect()



def update():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Jet")
    clock = pygame.time.Clock()
    running = True
    grungus = player()
    delta_time = 1
    grungus.sprite, sprite_rect = load_image("jet.png", 2)
    grungus.width, grungus.height = grungus.sprite.get_size()
    mouse_down = None
    #frames is not used
    frames = 0
    shot_time = 0
    spawn_time = 0
    




    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        frames += 1

        #gets current time in milliseconds
        curr_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False 

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("blue")

        # RENDER YOUR GAME HERE
        screen.blit(grungus.sprite, sprite_rect)




        mouse_pos = pygame.mouse.get_pos()

        # if a mouse button is held down and a certain amount of time has passed, add a new bullet object to bullet_list
        if mouse_down and (curr_time - shot_time >= fire_delay):
            bullet_list.append(bullet())
            bullet_list[-1].sprite, bullet_list[-1].sprite_rect = load_image("missile.png", 1.5)
            bullet_list[-1].sprite_rect.x, bullet_list[-1].sprite_rect.y = sprite_rect.x, sprite_rect.y
            shot_time = pygame.time.get_ticks()
            
        # for each bullet in bullet_list set its position to player's and blit. if the bullet reaches the edge of the screen, remove it from bullet_list
        for bullets in bullet_list:
            bullets.sprite_rect.x = (bullets.sprite_rect.x + bullets.speed)
            screen.blit(bullets.sprite, (bullets.sprite_rect.x + (grungus.width - 40), bullets.sprite_rect.y + 20))
            if bullets.sprite_rect.x >= SCREEN_WIDTH:
                bullet_list.remove(bullets)
            

        if curr_time - spawn_time >= spawn_delay:
            enemy_list.append(enemy())
            enemy_list[-1].sprite, enemy_list[-1].sprite_rect = load_image("druid.png", 2)
            enemy_list[-1].sprite_rect.x, enemy_list[-1].sprite_rect.y = (1280, random.randint(0, SCREEN_HEIGHT - 64))
            spawn_time = pygame.time.get_ticks()

        for enemies in enemy_list:
            enemies.sprite_rect.x = enemies.sprite_rect.x - enemies.speed
            screen.blit(enemies.sprite, enemies.sprite_rect)
            if enemies.sprite_rect.x < -100:
                enemy_list.remove(enemies)
            for bullets in bullet_list:
                if enemies.sprite_rect.colliderect(bullets.sprite_rect):
                    enemy_list.remove(enemies)
                    bullet_list.remove(bullets)


        #get_pressed(): returns boolean sequence representing state of currently pressed buttons as array
        keys = pygame.key.get_pressed()
        #checks for W, A, S, and D in keys array, increment or decrements the sprite_rect x or y. does nothing if edges of screen are reached.
        if keys[pygame.K_w] and sprite_rect.y > 0:
            sprite_rect.y -= grungus.speed * delta_time
        if keys[pygame.K_s] and sprite_rect.y < SCREEN_HEIGHT - grungus.height:
            sprite_rect.y += grungus.speed * delta_time
        if keys[pygame.K_a] and sprite_rect.x >= 0:
            sprite_rect.x -= grungus.speed * delta_time
        if keys[pygame.K_d] and sprite_rect.x < SCREEN_WIDTH - grungus.width:
            sprite_rect.x += grungus.speed * delta_time

        grungus.position = pygame.Vector2(sprite_rect.x, sprite_rect.y)


        print(bullet_list)

        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
