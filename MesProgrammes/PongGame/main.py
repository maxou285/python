
import pygame
from game import Game
from ball import Ball

pygame.init()





        





 
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 

 

# Générer la fenètre de notre jeu 
pygame.display.set_caption("PongGame")       # Définis le titre et si on le souhaite une icone
screen = pygame.display.set_mode((1080, 720))                           # Définis la taille de la fenètre

 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('ressources/freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('Choisis la balle pour cette partie', True, 00, 00)
text.set_colorkey([0, 0, 0])
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (400 // 2, 400 // 2)
 





StartButtonRect = pygame.Rect(170, 400, 700, 150)                                 
StartButtonSurface = pygame.Surface((StartButtonRect.width, StartButtonRect.height))

RightArrowButtonRect = pygame.Rect(720, 165, 100, 150)                                 
RightArrowButtonSurface = pygame.Surface((RightArrowButtonRect.width, RightArrowButtonRect.height))

LeftArrowButtonRect = pygame.Rect(275, 165, 100, 150)                                 
LeftArrowButtonSurface = pygame.Surface((LeftArrowButtonRect.width, LeftArrowButtonRect.height))


##### Choix de la balle pour la partie
    


BallSkinsList = ["ressources/pong_basketballStart.png", "ressources/Ball4copie.png","ressources/BallFootballStart.png","ressources/BallBeachVolley.png"]    
BallSkinIndex = 1

BallSkinsListGame = ["ressources/pong_basketball2.png", "ressources/Ball4.png","ressources/BallFootball.png","ressources/BallBeachVolley copie.png"]      





class DynamicText(object):
            def __init__(self, font, text, pos, autoreset=False):
                self.done = False
                self.font = font
                self.text = text
                self._gen = text_generator(self.text)
                self.pos = pos
                self.autoreset = autoreset
                self.update()
            
            def reset(self):
                self._gen = text_generator(self.text)
                self.done = False
                self.update()
                
            def update(self):
                if not self.done:
                    try: self.rendered = self.font.render(next(self._gen), True, (0, 128, 0))
                    except StopIteration: 
                        self.done = True
                        if self.autoreset: self.reset()

            def draw(self, screen):
                screen.blit(self.rendered, self.pos)
                    

####### PREMIERE BOUCLE WHILE POUR L'ECRAN DE DEMARAGE
game = Game()
wait_before_play = True
while wait_before_play == True:







    






    ## Afficher l'écran de démarage et le bouton start
    ScreenStart = pygame.image.load('ressources/bg.jpg')
    screen.blit(ScreenStart, (-100, -100))

    StartButton = pygame.image.load('ressources/button.png')
    screen.blit(StartButton, (180, 400))

    def SwitchBallStart():

        BallStart = pygame.image.load(BallSkinsList[BallSkinIndex])  
        BallStart.set_colorkey([0, 255, 0])
        screen.blit(BallStart, (500, 200))
    
    SwitchBallStart()

    """BasketBallStart = pygame.image.load('ressources/pong_basketball2.png') ##### 
    BasketBallStart.set_colorkey([0, 255, 0])
    screen.blit(BasketBallStart, (700, 200))"""

    ArrowStartRight = pygame.image.load('ressources/FlècheDroite2.png')
    ArrowStartRight.set_colorkey([0 , 255, 0])
    if BallSkinIndex < (len(BallSkinsList) - 1):
          screen.blit(ArrowStartRight, (720,165))

    ArrowStartLeft = pygame.image.load('ressources/FlècheGauche2.png')
    ArrowStartLeft.set_colorkey([0 , 255, 0])
    if BallSkinIndex > 0:
        screen.blit(ArrowStartLeft, (275,165))
    
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(text, (280, 80))



    
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() 
    for event in pygame.event.get():
        # DETECTION D'APPUIS SUR LE BOUTON START
        if ( event.type == pygame.MOUSEBUTTONUP ):
            mouse_position = pygame.mouse.get_pos()             # Location of the mouse-click

            if  StartButtonRect.collidepoint(mouse_position):
                    print("AHAHAHHAAAH")
                    wait_before_play = False
                
            if RightArrowButtonRect.collidepoint(mouse_position):
                    print("Droite")
                    print(BallSkinIndex)
                    if BallSkinIndex < (len(BallSkinsList) - 1):
                        BallSkinIndex += 1
                        
            if  LeftArrowButtonRect.collidepoint(mouse_position):
                    print("Gauche")
                    if  BallSkinIndex > 0:
                        BallSkinIndex -= 1
                  


        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
        
        # Draws the surface object to the screen.
        pygame.display.update()

    
   



    

    pygame.display.flip()

        # Si le joueur ferme cette fenètre
    '''for event in pygame.event.get():
            # verifier que l'event est fermeture de fenètre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
                quit()
            pygame.display.update()'''
# Importer de charger l'arrière plan du jeu
background = pygame.image.load('ressources/Galaxie1.jpeg')                    # Charge le background mais ne l'affiche pas encore
EndBackground = pygame.image.load('ressources/bg.jpg')
# Charger notre jeu
#### JE JEU COMMENCE REELLEMENT





clock = pygame.time.Clock()

###BOUCLE DU JEU PONG
# Boucle tant que cette condition est vrai
INFINITE_LOOP = True
while INFINITE_LOOP == True:
    
    def GameLoop():
        global Winner
        Winner = 0
        running = True
        game.ball.score_J1 = 0
        game.ball.score_J2 = 0
        while running:
                screen.blit(ScreenStart, (-100, -100))
                # Appliquer l'arrière plan à la fenètre
                screen.blit(background, (-100, -100))
            
                # appliquer l'image à mon joueur 
                screen.blit(game.paddle.image, game.paddle.rect)
                screen.blit(game.paddleopponent.imageopponent, game.paddleopponent.rectopponent)
            
            
            
                screen.blit(pygame.image.load(BallSkinsListGame[BallSkinIndex]), game.ball.rect)
                
                
                
                #screen.blit(game.spawn_monster().monster, game.spawn_monster().monster)
                game.ball.move()
                game.ball.collision(game.paddle, game.paddleopponent)
                
                # vérifier si le joueur souhaite aller à gauche ou à droite

                if game.pressed.get(pygame.K_a) and game.paddle.rect.x + game.paddle.rect.width < screen.get_width():                # détecte si le joueur presse la touche(flèche droit)
                    game.paddle.move_up()                           # si c'est le cas actionner la méthode move_right qui le fais aller à droit
                elif game.pressed.get(pygame.K_q) and game.paddle.rect.x > 0:                # détecte si le joueur presse la touche(flèche droit)
                        game.paddle.move_down()

                if game.pressed.get(pygame.K_p) and game.paddleopponent.rect.x + game.paddleopponent.rect.width < screen.get_width():                # détecte si le joueur presse la touche(flèche droit)
                    game.paddleopponent.move_up_opponent()                           # si c'est le cas actionner la méthode move_right qui le fais aller à droit
                elif game.pressed.get(pygame.K_m) and game.paddleopponent.rect.x > 0:                # détecte si le joueur presse la touche(flèche droit)
                        game.paddleopponent.move_down_opponent()
                

                #print(game.player.rect.x)
                clock.tick(60)              # Nombre de FPS
                # Test des scores //// /////// ///// //// ///// ////// ////// //// /////  //// //// ///// ///// ///// ////

                if game.ball.score_J1 == 0:
                    Chiffre0 = pygame.image.load('ressources/Chiffre0.png') 
                    screen.blit(Chiffre0, (350, 20))
                if game.ball.score_J1 == 1:
                    Chiffre1 = pygame.image.load('ressources/1Chiffre.png') 
                    screen.blit(Chiffre1, (350, 20))
                if game.ball.score_J1 == 2:
                    Chiffre2 = pygame.image.load('ressources/Chiffre2.png') 
                    screen.blit(Chiffre2, (350, 20))
                if game.ball.score_J1 == 3:
                    Chiffre3 = pygame.image.load('ressources/Chiffre3.png') 
                    screen.blit(Chiffre3, (350, 20))
                if game.ball.score_J1 == 4:
                    Chiffre4 = pygame.image.load('ressources/Chiffre4.png') 
                    screen.blit(Chiffre4, (350, 20))
                if game.ball.score_J1 == 5:
                    Chiffre5 = pygame.image.load('ressources/Chiffre5.png') 
                    screen.blit(Chiffre5, (350, 20))
                    print("Victoire du Joueur 1")
                    running = False
                    Winner = 1
                    GameEnd = True
                    wait_before_play = True

                if game.ball.score_J2 == 0:
                    Chiffre0 = pygame.image.load('ressources/Chiffre0.png') 
                    screen.blit(Chiffre0, (520, 20))
                if game.ball.score_J2 == 1:
                    Chiffre1 = pygame.image.load('ressources/1Chiffre.png') 
                    screen.blit(Chiffre1, (520, 20))
                if game.ball.score_J2 == 2:
                    Chiffre2 = pygame.image.load('ressources/Chiffre2.png') 
                    screen.blit(Chiffre2, (520, 20))
                if game.ball.score_J2 == 3:
                    Chiffre3 = pygame.image.load('ressources/Chiffre3.png') 
                    screen.blit(Chiffre3, (520, 20))
                if game.ball.score_J2 == 4:
                    Chiffre4 = pygame.image.load('ressources/Chiffre4.png') 
                    screen.blit(Chiffre4, (520, 20))
                if game.ball.score_J2 == 5:
                    Chiffre5 = pygame.image.load('ressources/Chiffre5.png') 
                    screen.blit(Chiffre5, (520, 20))
                    print("Victoire du Joueur 2")
                    running = False
                    Winner = 2
                    GameEnd = True
                    wait_before_play = True
                
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

    GameLoop()
        
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('ressources/freesansbold.ttf', 32)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('Une autre partie ? ', True, 00, 00)
    text.set_colorkey([0, 0, 0])
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (400 // 2, 400 // 2)
    ###############@
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 50)       # Debut
    
        # raise the USEREVENT every 1000ms
    pygame.time.set_timer(pygame.USEREVENT, 200)

        # generate a generator that scrolls through the letters
        # given a string foo, it will return
        # f
        # fo
        # foo
    def text_generator(text):
            tmp = ''
            for letter in text:
                tmp += letter
                # don't pause for spaces
                if letter != ' ':
                    yield tmp

        # a simple class that uses the generator
        # and can tell if it is done
    
    message = DynamicText(font, "Victoire du joueur " + str(Winner)+ " Félicitations", (310, 350), autoreset=True)
    
            
    ###############@

    wait_before_play = True
    while wait_before_play == True:
        
        ##############################################################################

        
        
        

        
        



        

        ################################################################################
        ## Afficher l'écran de démarage et le bouton start
        ScreenStart = pygame.image.load('ressources/bg.jpg')
        screen.blit(ScreenStart, (-100, -100))
        StartButton = pygame.image.load('ressources/button.png')
        screen.blit(StartButton, (180, 400))

        SwitchBallStart()

        ArrowStartRight = pygame.image.load('ressources/FlècheDroite2.png')
        ArrowStartRight.set_colorkey([0 , 255, 0])
        if BallSkinIndex < (len(BallSkinsList) - 1):
            screen.blit(ArrowStartRight, (720,165))

        ArrowStartLeft = pygame.image.load('ressources/FlècheGauche2.png')
        ArrowStartLeft.set_colorkey([0 , 255, 0])
        if BallSkinIndex > 0:
            screen.blit(ArrowStartLeft, (275,165))

        screen.blit(text, (410, 80))

        for event in pygame.event.get():
            
            
                
            if event.type == pygame.QUIT:
    
                # deactivates the pygame library
                pygame.quit()
    
                # quit the program.
                quit()
            # DETECTION D'APPUIS SUR LE BOUTON START
            if ( event.type == pygame.MOUSEBUTTONUP ):
                mouse_position = pygame.mouse.get_pos()             # Location of the mouse-click

                if  StartButtonRect.collidepoint(mouse_position):
                        print("AHAHAHHAAAH")
                        wait_before_play = False
                        
                    
                if RightArrowButtonRect.collidepoint(mouse_position):
                        print("Droite")
                        print(BallSkinIndex)
                        if BallSkinIndex < (len(BallSkinsList) - 1):
                            BallSkinIndex += 1
                            
                if  LeftArrowButtonRect.collidepoint(mouse_position):
                        print("Gauche")
                        if  BallSkinIndex > 0:
                            BallSkinIndex -= 1
                
            if event.type == pygame.USEREVENT: message.update()
        else:
                
                message.draw(screen)
                pygame.display.flip()
                clock.tick(60)
                
                
                
                continue

        '''if event.type == pygame.QUIT:
    
                # deactivates the pygame library
                pygame.quit()
    
                # quit the program.
                quit()
            
            # Draws the surface object to the screen.
        

        pygame.display.flip()
        pygame.display.update()
            # Si le joueur ferme cette fenètre
        for event in pygame.event.get():
                # verifier que l'event est fermeture de fenètre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                    quit()
                pygame.display.update()'''

    