import pygame




class bullet:
    speed = 5
    

    def __init__(self) -> None:
        self.sprite = pygame.image.load("images/bullet_bill.jpg").convert()
        self.sprite = pygame.transform.scale(self.sprite, (200, 100))

        

    def __init__(self, position) -> None:
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.sprite = pygame.image.load("images/bullet_bill.jpg").convert()
        self.sprite = pygame.transform.scale(self.sprite, (200, 100))
    
    
        
bullet_list = []
fire_delay = 300