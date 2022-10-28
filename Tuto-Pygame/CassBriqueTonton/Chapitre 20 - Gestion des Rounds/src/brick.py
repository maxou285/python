##########################################################################################
# Les import de librairies
##########################################################################################

import pygame                                                                               # Importe le module pygame de sorte que je puisse utiliser des fonctions de cette librairie 
from src.const import *


##########################################################################################
# Classe Brick
#   Classe qui gère les briques
#   Une brique est un Sprite, par conséquent celle classe hérite de la classe Sprite (sous librairie de pygame)
##########################################################################################

class Brick(pygame.sprite.Sprite):

    # Propriétés :
    # - _color : 'blue', 'green', 'red', 'silver', 'yellow'
    # - image : image de la brique que l'on fabrique à partir du fichier
    # - mask : mask de la brique
    # - rect : taille
    # - _points : points associées à la brique
    # - _hits : nombre de fois qu'il faut toucher la brique pour la détruire

    # Le constructeur
    def __init__(self, color, round_no):
        # Appel du constructeur du parent
        super().__init__()

        self._color = color
        self.image = pygame.image.load('resources/images/brick_{}.png'.format(color)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)                                    # Fabrication du masque à partir de l'image
        self.rect = self.image.get_rect()

        # Rechercher les points à associer à la brique en fonction de la couleur
        colors = BRICKS_COLORS
        points = BRICKS_POINTS
        idx = colors.index(color)
        self._points = points[idx]

        # Nombre de hits pour la brique
        hits = BRICKS_HITS
        self._hits = hits[idx]

        # Si la couleur est 'silver' il faut multiplier par le numéro du round
        if color == 'silver':
            self._points *= round_no

    def update(self):
        screen = pygame.display.get_surface()                                               # screen contient un objet de type surface dans lequel je peux dessiner
        screen.blit(self.image, self.rect.topleft)                                          # Positionne la brique dans la fenêtre

