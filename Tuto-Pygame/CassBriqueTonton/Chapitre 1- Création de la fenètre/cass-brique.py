##########################################################################################
# Les import de librairies
##########################################################################################

import pygame                                                                               # Importe le module pygame de sorte que je puisse utiliser des fonctions de cette librairie 
from src.const import *                                                                     # Importe les constantes
from src.start_screen import StartScreen
from src.game import Game


##########################################################################################
# Classe CasseBrique
#   Cette classe permettra de gérer les différentes phases du jeu
#   Pour le moment cette classe ne gère que la création de la fenêtre
##########################################################################################

class CasseBrique:

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - _stage : 1 = Start screen, 2 = Jeu
    # - _bPlay : False quand on ferme l'application
    # - _font : police de caractères
    # - _startScreen : l'écran de démarrage
    # - _game : le jeu en lui-même

    # Le constructeur
    def __init__(self):
        # Création d'une fenêtre
        pygame.display.set_mode(SCREEN_SIZE)                                                # Crée une fenêtre de taille SCREEN_SIZE
        pygame.display.set_caption(WINDOW_TITLE)                                            # Donne un titre à la fenêtre
        self._screen = pygame.display.get_surface()                                         # screen contient un objet de type surface dans lequel je peux dessiner

        # Fixer le fond
        self._screen.fill(BACKGROUND_COLOR)                                                 # Remplit la fenêtre avec une couleur de fond

        # Etape
        self._stage = 1                                                                     # 1 = Start Screen

        # Initialiser bPlay
        self._bPlay = True                                                                  # Passera à False quand on sortira

        # Charger les fontes
        self._font = pygame.font.Font('resources/fonts/optimus.otf', 30)                    # Taille = 30

        # Créer l'objet Ecran de démarrage (StartScreen)
        self._startScreen = StartScreen()

        # Créer l'objet Game qui correspond au jeu en lui-même
        self._game = Game()

    # Boucle principale de gestion du jeu
    def main_loop(self):
        while self._bPlay:                                                                  # Tant que l'on veut jouer on boucle sur la procédure indentée
            for event in pygame.event.get():                                                # Parcourir les évènements reçus par l'application
                if event.type == pygame.QUIT:                                               # A t'on reçu un évènement "QUIT" ?
                    self._bPlay = False                                                     # Oui donc on quitte l'application

            # Gestion de l'étape
            if self._stage == 1:
                self._bPlay = self._startScreen.show()                                      # Retourne False si on veut sortir de l'application
                if self._bPlay:
                    self._stage = 2                                                         # Si True alors on veut passer à l'étape suivante
            elif self._stage == 2:
                self._bPlay = self._game.show()                                             # Retourne False si on veut sortir de l'application
                if self._bPlay:
                    self._stage = 1                                                         # Si True alors on veut passer à l'étape suivante


##########################################################################################
# Programme principal
##########################################################################################

pygame.init()                                                                               # Initialise pygame : l'appel est obligatoire pour pouvoir utiliser pygame
pygame.font.init()                                                                          # Initialise le module font pour afficher du teste dans un objet Surface

if __name__ == "__main__":                                                                  # Le script est-il appelé depuis la ligne de commande ?
    mon_CasseBrique = CasseBrique()                                                         # Oui : je crée un objet CasseBrique
    mon_CasseBrique.main_loop()                                                             # Gestion du jeu

pygame.quit()                                                                               # Fait l'inverse de pygame.init() en permettant de sortir proprement de pygame

