import pygame



class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        self.damage = 5
        self.image = pygame.image.load('Tuto-Pygame/assets/mummy.png')
        self.rect = self.image.get_rect()                                       # rect permet de mettre l'image dans un carré et de la déplacer il faut la mettre
        self.rect.x = 1000                                         # modifie le point de spawn du sprite(joueur sur l'axe x ) 
        self.rect.y = 535        
    
    def move(self):
        self.rect.x -= self.velocity