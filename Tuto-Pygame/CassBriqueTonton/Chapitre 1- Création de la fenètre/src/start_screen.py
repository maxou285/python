##########################################################################################
# Les import de librairies
##########################################################################################

import pygame
from src.const import *                                                                     # Importe les constantes


##########################################################################################
# Classe StartScreen
#   Cette classe affiche l'écran de démarrage
##########################################################################################

class StartScreen:

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - _font : police de caractères

    # Le constructeur
    def __init__(self):
        self._screen = pygame.display.get_surface()                                         # screen contient un objet de type surface dans lequel je peux dessiner

        # Charger la police de caractères
        self._font = pygame.font.Font('resources/fonts/optimus.otf', SIZE_FONT)

    # Fabrique l'image et la montre
    def show(self):
        # Dessiner notre image de départ
        self._screen.fill(BACKGROUND_COLOR)                                                 # Remplit la fenêtre avec une couleur de fond

        # Dimensions de la fenêtre
        screen_dimensions = self._screen.get_rect()

        # Afficher un message pour démarrer la partie
        text_image = self._font.render(SZ_PRESS_SPACE, True, (255, 255, 255))
        self._screen.blit(text_image, (screen_dimensions.width / 2 - text_image.get_rect().width / 2, screen_dimensions.height / 2 - text_image.get_rect().height * 3))
        text_image = self._font.render(SZ_OR, True, (255, 255, 255))
        self._screen.blit(text_image, (screen_dimensions.width / 2 - text_image.get_rect().width / 2, screen_dimensions.height / 2 - text_image.get_rect().height * 2))
        text_image = self._font.render(SZ_PRESS_MOUSE_BUTTON, True, (255, 255, 255))
        self._screen.blit(text_image, (screen_dimensions.width / 2 - text_image.get_rect().width / 2, screen_dimensions.height / 2 - text_image.get_rect().height))
        text_image = self._font.render(SZ_TO_START_GAME, True, (255, 255, 255))
        self._screen.blit(text_image, (screen_dimensions.width / 2 - text_image.get_rect().width / 2, screen_dimensions.height / 2 + 50))
        pygame.display.flip()                                                               # Actualise l'écran

        # Appelle la fontion main_loop() qui gère cet écran
        return self.main_loop()                                                             # Si cela retourne False alors on veut sortir de l'application

    # Boucle principale de l'écran de démarrage
    def main_loop(self):
        # Boucle d'attente d'un événement
        while True:                                                                         # La sortie de la boucle se fait par un return à l'intérieur de la boucle
            for event in pygame.event.get():                                                # Parcourir les évènements reçus par l'application
                if event.type == pygame.QUIT:                                               # A t'on reçu un évènement "QUIT" ?
                    return False                                                            # Oui : Valeur de sortie qui indiqu que l'on veut sortir de l'application
                elif event.type == pygame.MOUSEBUTTONUP:                                    # A t'on appuyé sur un bouton de la souris ?
                    return True                                                             # Oui : Indique que l'on veut passer à l'étape suivante
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:                                         # A ton appuyé sur la touche ESPACE ?
                        return True                                                         # Oui : Indique que l'on veut passer à l'étape suivante

