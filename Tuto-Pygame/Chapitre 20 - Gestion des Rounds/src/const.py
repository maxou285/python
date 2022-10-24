##########################################################################################
# Les constantes
#   Je déclare ici des constantes que je vais utiliser ensuite dans mon code
##########################################################################################

# casse-brique.py
TOP_OFFSET = 37                                                                             # A combien du haut de l'écran comenceront les rounds
SCREEN_SIZE = 600, 650 + TOP_OFFSET                                                         # Dimensions de la fenêtre en pixels: largeur, hauteur
WINDOW_TITLE = 'Casse-Briques - {}'                                                         # Titre de la fenêtre
BACKGROUND_COLOR = (0, 0, 0)                                                                # Couleur du fond de la fenêtre en (Red, Bue, Green) 
ROUND_START = 1                                                                             # Round de départ  

# start_screen.py
SIZE_FONT = 30                                                                              # Taille de la police de caractères
SZ_PRESS_SPACE = 'Appuyez sur ESPACE'
SZ_OR = 'ou'
SZ_PRESS_MOUSE_BUTTON = 'Cliquez la souris'
SZ_TO_START_GAME = 'pour démarrer la partie'
SZ_WINDOW_TITLE = 'Casse-Brique'

# final_screen.py
SZ_SCORE = 'SCORE : {0}'
SZ_WON = "JEU TERMINE"

# game.py
BOTTOM_OFFSET = 60                                                                          # A combien du haut de l'écran comenceront les rounds
FPS = 60                                                                                    # Nombre d'images par seconde (Frames Per Second)
BALL_SPEED = 8                                                                              # Vitesse de la balle en pixel
BALL_START_ANGLE = 73                                                                       # En degrés
NB_LIVES = 3                                                                                # Nombre de vies au départ
SPEED_HIT_INC = 8                                                                           # Tous les SPEED_HIT_INC la vitesse de la balle est incrémentée de 1
FONT_SIZE_MEDIUM = 30                                                                       # Taille utilisée pour l'afficahge du score
FONT_SIZE_SMALL = 10                                                                        # Taille utilisée pour l'affichage des infos
INFOS_PAUSE = 'P : Pause'                                                                   # Message à afficher pour mettre en 'Pause'
INFOS_SOUND = 'S : Son'                                                                     # Message à afficher pour mettre/enlever le son
INFOS_LIVES = 'U : Vies infinies'                                                           # Message à afficher pour activier/désactiver les vies infinies
SOUND_BRICK = 'resources/sounds/sound_hitbrick.wav'                                         # Son quand je touche une brique qui se détruit
SOUND_BRICK_LIVE = 'resources/sounds/sound_hitbrick.wav'                                    # Son quand je touche une brique qui reste vivante
SOUND_WALL = 'resources/sounds/sound_wall.wav'                                              # Son quand la balle touche un mur
SOUND_PADDLE = 'resources/sounds/sound_paddle.wav'                                          # Son quand la balle touche la raquette         
SOUND_OUT = 'resources/sounds/sound_outspeech.wav'                                          # Son quand la balle touche le bas de l'écran (donc je perds)
SOUND_GAMEOVER = 'resources/sounds/sound_gameover.wav'                                      # Son quand la partie est terminée
    
# bricks.py
BRICKS_COLORS = ['blue', 'cyan', 'gold', 'green', 'orange', 'pink', 'red', 'silver', 'white', 'yellow'] # Liste des couleurs de briques
BRICKS_POINTS = [100, 70, 0, 80, 60, 110, 90, 50, 50, 120]                                  # Points par brique
BRICKS_HITS = [1, 1, -1, 1, 1, 1, 1, 2, 1, 1]                                               # Nombre de fois qu'il faut toucher une brique pour la détruire
