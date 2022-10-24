Ceci est un petit récap des étapes de bases pour n'importe quel jeu pygame bien organisé

# 3 Fichiers

1. ***resources***
    1. images
    2. sounds
    3. fonts

2. ***src***
    game.py
    startscreen.py
    ...

3. ***nom_du_jeu.py***



## nom_du_jeu.py
Le fichier principal du jeu la que l'on va éxécuter le programme principal

# 1. Les imports de librairies
# 2. Classe NomDuJeu
    Cette classe permettra de gérer les différentes phases du jeu
    Pour le moment cette classe ne gère que la création de la fenêtre
1. 
    ***def __init__(self):***
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
2. 
    ***Boucle principale de gestion du jeu***
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

# 3. Programme Principal
pygame.init()                                                                           # Initialise pygame : l'appel est obligatoire pour pouvoir utiliser pygame
pygame.font.init()                                                                      # Initialise le module font pour afficher du teste dans un objet Surface

if __name__ == "__main__":                                                              # Le script est-il appelé depuis la ligne de commande ?
    mon_CasseBrique = CasseBrique()                                                     # Oui : je crée un objet CasseBrique
    mon_CasseBrique.main_loop()                                                         # Gestion du jeu

pygame.quit()                                                                           # Fait l'inverse de pygame.init() en permettant de sortir proprement





## src

# const.py
##########################################################################################
Les constantes
Je déclare ici des constantes que je vais utiliser ensuite dans mon code
##########################################################################################

    casse-brique.py
SCREEN_SIZE = 600, 650                                                                      # Dimensions de la fenêtre en pixels: largeur, hauteur
WINDOW_TITLE = 'Mon Casse-Briques'                                                          # Titre de la fenêtre
BACKGROUND_COLOR = (0, 0, 0)                                                                # Couleur du fond de la fenêtre en (Red, Bue, Green) 

    start_screen.py
SIZE_FONT = 30                                                                              # Taille de la police de caractères
SZ_PRESS_SPACE = 'Appuyez sur ESPACE'
SZ_OR = 'ou'
SZ_PRESS_MOUSE_BUTTON = 'Cliquez la souris'
SZ_TO_START_GAME = 'pour démarrer la partie'

    game.py
SIZE_FONT = 30                                                                              # Taille de la police de caractères
SZ_THE_GAME = 'Le JEU'




## game.py

##########################################################################################
1. Les import de librairies
##########################################################################################

import pygame
from src.const import *                                                                     # Importe les constantes


##########################################################################################
2. Classe Game
Cette classe s'occupe du jeu
##########################################################################################

class Game:

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - _font : police de caractères

    # Le constructeur
   ***def __init__(self):***
        self._screen = pygame.display.get_surface()                                         # screen contient un objet de type surface dans lequel je peux dessiner

        # Charger la police de caractères
        self._font = pygame.font.Font('resources/fonts/optimus.otf', SIZE_FONT)

    # Fabrique l'image et la montre
    def show(self):
        # Dessiner notre image de départ
        self._screen.fill(BACKGROUND_COLOR)                                                 # Remplit la fenêtre avec une couleur de fond

        # Dimensions de la fenêtre
        screen_dimensions = self._screen.get_rect()

        # Afficher le message 'Le JEU'
        text_image = self._font.render(SZ_THE_GAME, True, (255, 255, 255))
        self._screen.blit(text_image, (screen_dimensions.width / 2 - text_image.get_rect().width / 2, screen_dimensions.height / 2 - text_image.get_rect().height / 2))
        pygame.display.flip()                                                               # Actualise l'écran

        # Appelle la fontion main_loop() qui gère cet écran
        return self.main_loop()                                                             # Si cela retourne False alors on veut sortir de l'application

   ***Boucle principale du jeu***
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



```On suit ce schéma d'organisation pour tous les fichiers .py dans src```
EXEMPLE : FICHIER start_screen.py




##########################################################################################
# Les import de librairies
##########################################################################################

import pygame
from src.const import *                                                                     # Importe les constantes


##########################################################################################
# Classe StartScreen
Cette classe affiche l'écran de démarrage
##########################################################################################

class StartScreen:

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - _font : police de caractères

    # Le constructeur
   ***def __init__(self):***
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

   ***Boucle principale de l'écran de démarrage*** 
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

