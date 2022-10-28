##########################################################################################
# Les import de librairies
##########################################################################################

import pygame                                                                               # Importe le module pygame de sorte que je puisse utiliser des fonctions de cette librairie 


##########################################################################################
# Classe Paddle
#   Classe qui gère la raquette avec laquelle on renvoie la balle vers le haut
#   Un Paddle est un Sprite, par conséquent celle classe hérite de la classe Sprite (sous librairie de pygame)
##########################################################################################

class Paddle(pygame.sprite.Sprite):

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - image : image de la brique que l'on fabrique à partir du fichier
    # - mask : mask du Paddle pour gestion précise de collision
    # - rect : dimensions et position du Paddle
    # - _zone : zone dans laquelle le Paddle peut bouger

    # Le constructeur
    def __init__(self, left_width = 0, right_width = 0, bottom_offset = 0):
        # Appel du constructeur du parent
        super().__init__()

        self._screen = pygame.display.get_surface()                                         # La Surface dans laquelle on dessine

        self.image = pygame.image.load('resources/images/paddle.png').convert_alpha()       # Charge l'image du Paddle
        self.mask = pygame.mask.from_surface(self.image)                                    # Fabrication du masque à partir de l'image
        self.rect = self.image.get_rect()                                                   # Pour éviter de faire sans cesse appel à get_rect()

        # Définir la zone dans laquelle le Paddle peut évoluer
        screen_dimensions = pygame.display.get_surface().get_rect()
        self._zone = pygame.Rect(left_width + self.rect.width / 2, screen_dimensions.height - bottom_offset, 
                                 screen_dimensions.width - left_width - right_width - self.rect.width, self.rect.height)

        # Position de départ
        self.rect.center = self._zone.center                                                # Positionner le Paddle au centre de la zone

    # Met à jour sa position
    def setPosition(self, x):
        if x < self._zone.x:
            self.rect.centerx = self._zone.x                                                # Positionne le Paddle à gauche
        elif x > self._zone.x + self._zone.width:
            self.rect.centerx = self._zone.x + self._zone.width                             # Positionne le Paddle à droite
        else:
            self.rect.centerx = x                                                           # Positionne là où est la souris sur l'axe des X

    # Met à jour l'image
    def blit(self):
        # Met à jour l'image
        self._screen.blit(self.image, self.rect.topleft)                                    # Positionne le Paddle dans la fenêtre
