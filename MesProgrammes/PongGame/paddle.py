import pygame 




class Paddle(pygame.sprite.Sprite):
    def __init__(self, opponent=1):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('ressources/PongPaddlesRed.png')
        self.rect = self.image.get_rect()                                       # rect permet de mettre l'image dans un carré et de la déplacer il faut la mettre
        self.rect.x = 50                                           # modifie le point de spawn du sprite(joueur sur l'axe x ) 
        self.rect.y = 300
        if opponent == True:
            self.imageopponent = pygame.image.load('ressources/PongPaddlesBlue.png')
            self.rectopponent = self.imageopponent.get_rect()                                       # rect permet de mettre l'image dans un carré et de la déplacer il faut la mettre
            self.rectopponent.x = 1015                                           # modifie le point de spawn du sprite(joueur sur l'axe x ) 
            self.rectopponent.y = 300



    def move_up(self):
        if self.rect.y >= 10:
            self.rect.y -= self.speed
    def move_down(self):
        if self.rect.y < (720-148):
            self.rect.y += self.speed

    def move_up_opponent(self):
        if self.rectopponent.y >= 10:
            self.rectopponent.y -= self.speed
    def move_down_opponent(self):
        if self.rectopponent.y < (720-148):
            self.rectopponent.y += self.speed
