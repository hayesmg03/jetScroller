import random
import pygame as pg

class enemy:
    speed = 5
    sprite = None
    sprite_rect = None
    position = None

    def __init__(self) -> None:
        pass

enemy_list = []
spawn_delay = 400
spawn_time = 0