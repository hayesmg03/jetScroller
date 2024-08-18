import pygame

class player:
    def __init__(self) -> None:
        self.sprite = pygame.image.load("images/tank_main_character.png").convert()
        self.height = None
        self.width = None
        self.position = None
        self.x = None
        self.y = None
