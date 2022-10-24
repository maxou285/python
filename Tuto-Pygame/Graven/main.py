import keyword

import pygame
from game import Game


pygame.init()





        


# Générer la fenètre de notre jeu 
pygame.display.set_caption("Comet fall Game")       # Définis le titre et si on le souhaite une icone
screen = pygame.display.set_mode((1080, 720))                           # Définis la taille de la fenètre


# Importer de charger l'arrière plan du jeu
background = pygame.image.load('Tuto-Pygame/assets/bg.jpg')                    # Charge le background mais ne l'affiche pas encore

# Charger notre jeu
game = Game()




running = True

# Boucle tant que cette condition est vrai

while running:

    # Appliquer l'arrière plan à la fenètre
    screen.blit(background, (0, -200))


    # appliquer l'image à mon joueur 
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.spawn_monster().monster, game.spawn_monster().monster)
    
    # vérifier si le joueur souhaite aller à gauche ou à droite

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():                # détecte si le joueur presse la touche(flèche droit)
        game.player.move_right()                           # si c'est le cas actionner la méthode move_right qui le fais aller à droit
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:                # détecte si le joueur presse la touche(flèche droit)
            game.player.move_left() 

    print(game.player.rect.x)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme cette fenètre
    for event in pygame.event.get():
        # verifier que l'event est fermeture de fenètre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        
        # détecter si un joueur presse une touche du clavier
        elif event.type == pygame.KEYDOWN:
            # vérifier quelle touche a été utilisée
           game.pressed[event.key] = True                       # Grace à cela je remplis le dictionnaire dans game.presed avec les touches présses 
        elif event.type == pygame.KEYUP:                        # et cela remplis automatiquement le dictionnaire
            game.pressed[event.key] = False