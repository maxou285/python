##########################################################################################
# Les import de librairies
##########################################################################################

import pygame                                                                               # Importe le module pygame de sorte que je puisse utiliser des fonctions de cette librairie 
import math


##########################################################################################
# Classe Ball
#   Classe qui gère la balle
#   Une balle est un Sprite, par conséquent celle classe hérite de la classe Sprite (sous librairie de pygame)
##########################################################################################

class Ball(pygame.sprite.Sprite):

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - image : image de la balle que l'on fabrique à partir du fichier
    # - mask : mask de la balle pour gestion précise de collision
    # - rect : dimensions et position du Paddle
    # - _zone : zone dans laquelle la balle peut bouger
    # - _background_color : couleur de fond
    # - _speed : vitesse de la balle. Si 0 la balle est sur le Paddle et se déplace avec le Paddle
    # - _direction : direction (x, y) de la balle teannt compte de la vitesse

    # Le constructeur
    def __init__(self, background_color, left_width = 0, right_width = 0, top_height = 0):
        # Appel du constructeur du parent
        super().__init__()

        self._screen = pygame.display.get_surface()                                         # La Surface dans laquelle on dessine

        self.image = pygame.image.load('resources/images/ball.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)                                    # Fabrication du masque à partir de l'image
        self.rect = self.image.get_rect()                                                   # Pour éviter de faire sans cesse appel à get_rect()

        self._background_color = background_color                                           # Utilisé pour effacer la précédente position du sprite

        # Définir la zone dans laquelle la balle peut évoluer
        screen_dimensions = pygame.display.get_surface().get_rect()
        self._zone = pygame.Rect(left_width + self.rect.width /2, top_height + self.rect.height / 2, 
                                 screen_dimensions.width - left_width - right_width - self.rect.width, screen_dimensions.height - top_height - self.rect.height)

        # Position de départ
        self.rect.center = self._zone.center                                                # Positionner la balle au centre de la zone

        # Vitesse et direction
        self._speed = 0
        self._direction = (0, 0)

    # Met à jour sa position (je surcharge la fonction update de la classe Sprite)
    def setPosition(self, position):
        # Vérifier que la position demandée est dans la zone
        if position[0] < self._zone.x:
            position[0] = self._zone.x
            self._direction[0] = -self._direction[0]
        elif position[0] > self._zone.x + self._zone.width:
            position[0] = self._zone.x + self._zone.width
            self._direction[0] = -self._direction[0]
        if position[1] < self._zone.y:
            position[1] = self._zone.y
            self._direction[1] = -self._direction[1]
        elif position[1] > self._zone.y + self._zone.height:
            self._speed = 0
        self.rect.center = position

    def setDirection(self, angle):
        self._direction = [self._speed * math.cos(math.radians(angle)), self._speed * -math.sin(math.radians(angle))] # Direction de la balle et vitesse sur chaque axe

    def setSpeed(self, speed):
        # Recalculer l'orientation pour tenir compte de la nouvelle vitesse
        
        # Pour rappel la vitesse correspond à la longeur du vecteur _direction
        # Il suffit donc de multiplier x et y par la variation entre la vitesse demandée et l'ancienne vitesse
        self._direction[0] *= (speed / self._speed)
        self._direction[1] *= (speed / self._speed)

        # Et enfin je mets à jour la proprité correspondant à vitesse de la balle
        self._speed = speed

    # Met à jour l'image
    def blit(self):
        # Met à jour l'image
        self._screen.blit(self.image, self.rect.topleft)                                    # Positionne la balle dans la fenêtre
