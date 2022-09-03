import pygame
from ball import Ball
from game import Game

pygame.init()





        


# Générer la fenètre de notre jeu 
pygame.display.set_caption("PongGame")       # Définis le titre et si on le souhaite une icone
screen = pygame.display.set_mode((1080, 720))                           # Définis la taille de la fenètre

ScreenStart = pygame.image.load('MesProgrammes/PongGame/ressources/PongScreenStart.png')
# Importer de charger l'arrière plan du jeu
background = pygame.image.load('MesProgrammes/PongGame/ressources/Galaxie1.jpeg')                    # Charge le background mais ne l'affiche pas encore
run = False
# Charger notre jeu

game = Game()



clock = pygame.time.Clock()
running = True

# Boucle tant que cette condition est vrai

while running:
        screen.blit(ScreenStart, (-100, -100))
        # Appliquer l'arrière plan à la fenètre
        screen.blit(background, (-100, -100))
    
        # appliquer l'image à mon joueur 
        screen.blit(game.paddle.image, game.paddle.rect)
        screen.blit(game.paddleopponent.image, game.paddleopponent.rect)
        screen.blit(game.ball.image, game.ball.rect)
        #screen.blit(game.spawn_monster().monster, game.spawn_monster().monster)
        game.ball.move()
        game.ball.collision(game.paddle)
        game.ball.collision(game.paddleopponent)
        # vérifier si le joueur souhaite aller à gauche ou à droite

        if game.pressed.get(pygame.K_a) and game.paddle.rect.x + game.paddle.rect.width < screen.get_width():                # détecte si le joueur presse la touche(flèche droit)
            game.paddle.move_up()                           # si c'est le cas actionner la méthode move_right qui le fais aller à droit
        elif game.pressed.get(pygame.K_q) and game.paddle.rect.x > 0:                # détecte si le joueur presse la touche(flèche droit)
                game.paddle.move_down()

        if game.pressed.get(pygame.K_p) and game.paddle.rect.x + game.paddle.rect.width < screen.get_width():                # détecte si le joueur presse la touche(flèche droit)
            game.paddleopponent.move_up()                           # si c'est le cas actionner la méthode move_right qui le fais aller à droit
        elif game.pressed.get(pygame.K_m) and game.paddle.rect.x > 0:                # détecte si le joueur presse la touche(flèche droit)
                game.paddleopponent.move_down() 

        #print(game.player.rect.x)
        clock.tick(60)              # Nombre de FPS
        # Test des scores //// /////// ///// //// ///// ////// ////// //// /////  //// //// ///// ///// ///// ////

        if game.ball.score_J1 == 1:
            Chiffre1 = pygame.image.load('MesProgrammes/PongGame/ressources/1Chiffre.png') 
            screen.blit(Chiffre1, (350, 20))
        if game.ball.score_J1 == 2:
            Chiffre2 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre2.png') 
            screen.blit(Chiffre2, (350, 20))
        if game.ball.score_J1 == 3:
            Chiffre3 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre3.png') 
            screen.blit(Chiffre3, (350, 20))
        if game.ball.score_J1 == 4:
            Chiffre4 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre4.png') 
            screen.blit(Chiffre4, (350, 20))
        if game.ball.score_J1 == 5:
            Chiffre5 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre5.png') 
            screen.blit(Chiffre5, (350, 20))
            print("Victoire du Joueur 1")

        
        if game.ball.score_J2 == 1:
            Chiffre1 = pygame.image.load('MesProgrammes/PongGame/ressources/1Chiffre.png') 
            screen.blit(Chiffre1, (520, 20))
        if game.ball.score_J2 == 2:
            Chiffre2 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre2.png') 
            screen.blit(Chiffre2, (520, 20))
        if game.ball.score_J2 == 3:
            Chiffre3 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre3.png') 
            screen.blit(Chiffre3, (520, 20))
        if game.ball.score_J2 == 4:
            Chiffre4 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre4.png') 
            screen.blit(Chiffre4, (520, 20))
        if game.ball.score_J2 == 5:
            Chiffre5 = pygame.image.load('MesProgrammes/PongGame/ressources/Chiffre5.png') 
            screen.blit(Chiffre5, (520, 20))
            print("Victoire du Joueur 2")
        
        
        
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

    
        
        
    