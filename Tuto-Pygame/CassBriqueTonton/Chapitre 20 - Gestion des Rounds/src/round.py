##########################################################################################
# Les import de librairies
##########################################################################################

import pygame
from src.const import *
from src.const_rounds import *                                                              # Les rounds
from src.brick import Brick


##########################################################################################
# Classe Round
##########################################################################################

class Round:

    # Propriétés :
    # - _round_no : numéro du round de 1 à 32
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - _name : nom du round
    # - _background : couleur du fond
    # - _edges : liste contenant les 3 bordures (gauche, droite, haut)
    # - _top_offset : offset depuis le haut de l'écran en pixel
    # - _bricks : briques du round (autres que gold)
    # - _bricks_gold : briques gold du round
    # - _map : la carte des briques sachant qu'on a au max 13 briques par ligne

    # Le constructeur
    def __init__(self, round_no, top_offset):      
        self._screen = pygame.display.get_surface()                                         # La Surface dans laquelle on dessine
        self._round_no = round_no                                                           # Numéro du round
        self._top_offset = top_offset

        self._edges = self.createEdges()                                                    # Création des bordures
        self._bricks = pygame.sprite.Group()                                                # Groupe de sprites correspondant aux briques non gold
        self._bricks_gold = pygame.sprite.Group()                                           # Groupe de sprites correspondant aux briques gold

        # Déclaration de propriétés
        self._name = ''                                                                     # Titre du round
        self._background = (0, 0, 0)                                                        # Couleur de fond du round
        self._map = None                                                                    # La map du round

    # Fabrique le round
    def update(self):
        # Construire le round

        # Titre de la fenêtre
        self._name = WINDOW_TITLE.format(self._round_no)
        pygame.display.set_caption(self._name)

        # Le background d'abord
        self.createBackground()

        # Dimensions de l'écran
        screen_dimensions = self._screen.get_rect()

        # Les bordures
        self._screen.blit(self._edges[0], (0, self._top_offset))
        self._screen.blit(self._edges[1], (screen_dimensions.width - self._edges[1].get_rect().width, self._top_offset))
        self._screen.blit(self._edges[2], (self._edges[0].get_rect().width, self._top_offset))

        # Disposer les briques
        self.createBricks()

    # Création du fond
    def createBackground(self):
        # Le fond de la fenêtre
        self._screen.fill(BACKGROUND_COLOR)                                                 # Remplit l'écran de noir

        # Le fond du niveau
        self._background = ROUNDS[self._round_no - 1][0]                                    # Couleur de fond du round
        screen_dimensions = self._screen.get_rect()                                         # Dimensions de l'écran
        self._screen.fill(self._background, (0, self._top_offset, screen_dimensions.width, screen_dimensions.height - self._top_offset)) # Fixe la couleur de fond de la zone de jeu

    # Crée les bordures gauche, droite et haut
    def createEdges(self):
        return ( pygame.image.load('resources/images/edge_left.png').convert_alpha(),
                 pygame.image.load('resources/images/edge_right.png').convert_alpha(),
                 pygame.image.load('resources/images/edge_top.png').convert_alpha())
        
    # Disposition des briques dans le Round
    def createBricks(self):
        # Vider le groupe de sprites
        pygame.sprite.Group.empty(self._bricks)
        pygame.sprite.Group.empty(self._bricks_gold)

        # Nombre de lignes
        self._map = ROUNDS[self._round_no - 1][1]                                               # La map du round
        nb_lines = len(self._map)

        # Offset depuis le haut de l'écran
        vertical_offset = self._top_offset + self._edges[2].get_rect().height                   # Hauteur de la barre du haut

        # Fabriquer le niveau
        for i in range(nb_lines):
            for j in range(13):
                if self._map[i][j] != None:
                    brick = Brick(self._map[i][j], 1)                                           # Création de la brique en indiquant qu'il s'agit du round 1
                    brick.rect.topleft = ((j + 0.5) * brick.rect.width, vertical_offset + i * brick.rect.height)
                    if self._map[i][j] == 'gold':
                        self._bricks_gold.add(brick)
                    else:
                        self._bricks.add(brick)

    def blitBricks(self):
        # Afficher les briques
        pygame.sprite.Group.update(self._bricks)
        pygame.sprite.Group.update(self._bricks_gold)
