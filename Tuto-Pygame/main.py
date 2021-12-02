import pygame
pygame.init()

# Créer une première classe qui va représenter notre joueur
class Player:
    def __init__(self):
        


# Générer la fenètre de notre jeu 
pygame.display.set_caption("Comet fall Game")       # Définis le titre et si on le souhaite une icone
screen = pygame.display.set_mode((1080, 720))                           # Définis la taille de la fenètre


# Importer de charger l'arrière plan du jeu
background = pygame.image.load('Tuto-Pygame/assets/bg.jpg')                    # Charge le background mais ne l'affiche pas encore


running = True

# Boucle tant que cette condition est vrai

while running:

    # Appliquer l'arrière plan à la fenètre
    screen.blit(background, (0, -200))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme cette fenètre
    for event in pygame.event.get():
        # verifier que l'event est fermeture de fenètre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")