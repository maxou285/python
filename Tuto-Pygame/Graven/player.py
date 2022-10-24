import pygame


# Créer une première classe qui va représenter notre joueur
class Player(pygame.sprite.Sprite):             # création du joueur qui hérite de la classe Sprite de pygame (pour etre pris en compte par pygame)
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 4
        self.image = pygame.image.load('Tuto-Pygame/assets/player.png')
        self.rect = self.image.get_rect()                                       # rect permet de mettre l'image dans un carré et de la déplacer il faut la mettre
        self.rect.x = 400                                           # modifie le point de spawn du sprite(joueur sur l'axe x ) 
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity