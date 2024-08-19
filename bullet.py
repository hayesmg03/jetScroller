import pygame




class bullet:
    speed = 20
    sprite_rect = None
    sprite = None
    

    def __init__(self) -> None:
        pass

        

    def __init__(self, position) -> None:
        self.position = position
        self.x = position[0]
        self.y = position[1]
    
    
        
bullet_list = []
fire_delay = 300



