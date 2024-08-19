import pygame

class player:
    speed = 5
    sprite = None
    height = None
    width = None
    position = pygame.Vector2(0,0)

    def __init__(self) -> None:
        self.sprite = None
