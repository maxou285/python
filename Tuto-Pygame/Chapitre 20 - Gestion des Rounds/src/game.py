##########################################################################################
# Les import de librairies
##########################################################################################

import pygame
import math
from src.const import *
from src.const_rounds import *
from src.round import Round
from src.paddle import Paddle
from src.ball import Ball


##########################################################################################
# Classe StartScreen
#   Cette classe affiche l'écran de démarrage
##########################################################################################

class Game:

    # Propriétés :
    # - _screen : contient un objet de type Surface permettant d'accéder à la fenêtre et de pouvoir dessiner dedans
    # - _top_offset : offset depuis le haut de l'écran en pixels
    # - _round : round en cours de jeu
    # - _paddle : le Paddle (la raquette qui renvoie la balle)
    # - _clock : l'heure pour la gestion de vitesse
    # - _ball : la balle
    # - _lives : nombre de vies (nombre de paddles)
    # - _lives_unlimited : True = vies inifinis, False = gestin d'un nombre de vies
    # - _paddle_life_image : image d'un petit paddle qui représente les vies restantes
    # - _points : points marqués
    # - _font_medium : police de caractère utilisée pour le score
    # - _font_small : police de caractère utilisée pour les infos
    # - _successive_hits : nombre successifs de fois que l'on touche une brique. Permet de gérer la vitesse de la balle tous les SPEED_HIT_INC
    # - _pause : si True on est en Pause, si False on n'est pas en Pause
    # - _sound : si True avec du son, si False sans son
    # - _sound_brick : son quand je touche une brique qui se détruit
    # - _sound_brick_live : son quand je touche une brique qui reste vivante
    # - _sound_wall : son quand la balle touche un mur
    # - _sound_paddle : son quand la balle touche la raquette
    # - _sound_out : son quand la balle touche le bas de l'écran (donc je perds)
    # - _sound_gameover : son quand la partie est terminée

    # Le constructeur
    def __init__(self, round_no = 1, top_offset = 0):
        self._screen = pygame.display.get_surface()                                         # screen contient un objet de type surface dans lequel je peux dessiner
        self._top_offset = top_offset

        # Créer le round
        self._round = Round(round_no, top_offset)
        self._round.update()

        # Créer le Paddle
        self._paddle = Paddle(self._round._edges[0].get_rect().width, self._round._edges[1].get_rect().width, BOTTOM_OFFSET)

        # Créer la balle
        self._ball = Ball(self._round._background, self._round._edges[0].get_rect().width, self._round._edges[1].get_rect().width, TOP_OFFSET + self._round._edges[2].get_rect().height)

        # Nombre de vies
        self._lives = NB_LIVES
        self._lives_unlimited = False
        self._paddle_life_image = pygame.image.load('resources/images/paddle_life.png').convert_alpha()

        # Si on joue au clavier en laissant appuyer cela prend en compte la touche plus d'une fois
        pygame.key.set_repeat(1) 

        # Initialiser les points
        self._points = 0

        # Nombre de hits successifs à 0
        self._successive_hits = 0

        # Charger les polices de caractères
        self._font_medium = pygame.font.Font('resources/fonts/optimus.otf', FONT_SIZE_MEDIUM)
        self._font_small = pygame.font.Font('resources/fonts/optimus.otf', FONT_SIZE_SMALL)

        # Charger les sons
        self._sound_brick = pygame.mixer.Sound(SOUND_BRICK)
        self._sound_brick_live = pygame.mixer.Sound(SOUND_BRICK_LIVE)
        self._sound_wall = pygame.mixer.Sound(SOUND_WALL)
        self._sound_paddle = pygame.mixer.Sound(SOUND_PADDLE)
        self._sound_out = pygame.mixer.Sound(SOUND_OUT)
        self._sound_gameover = pygame.mixer.Sound(SOUND_GAMEOVER)
        self._sound = True                                                                  # Avec du son par défaut

        # Pause : pas de Pause à la création
        self._pause = False

        # On initialise la montre
        self._clock = pygame.time.Clock()

    # Fabrique l'image 
    def update(self):
        # Initialiser le nombre de vies de cette nouvelle partie
        self._lives = NB_LIVES

        # Initialiser les points
        self._points = 0      

        # Vitesse de la balle et nombre de hits successifs
        self._ball._speed = 0
        self._successive_hits = 0

        # Update le round
        self._round._round_no = ROUND_START
        self._round.update()

        # Appelle la fontion main_loop() qui gère cet écran
        return self.main_loop()                                                             # Si cela retourne False alors on veut sortir de l'application

    # Boucle principale du jeu
    def main_loop(self):
        # Boucle d'attente d'un événement
        while True:                                                                         # La sortie de la boucle se fait par un return à l'intérieur de la boucle
            # Faire en sorte d'avoir un nombre stabilisé d'images par seconde quelque soit la plateforme sur laquel tourne le jeu
            self._clock.tick(FPS)

            if self._pause:                                                                 # Est-on en Pause ?
                for event in pygame.event.get():                                            # Parcourir les évènements reçus par l'application
                    # Gestion de la sortie de l'application
                    if event.type == pygame.QUIT:                                           # A t'on reçu un évènement "QUIT" ?
                        return False                                                        # Oui : Valeur de sortie qui indiqu que l'on veut sortir de l'application
                    # Gestion de la Pause
                    elif event.type == pygame.KEYUP:                                        # A t'on appuyé sur une touche ?
                        if event.key == pygame.K_p:                                         # Oui : est-ce la touche 'P' ?
                            self._pause = False                                             # On sort de la Pause
                        elif event.key == pygame.K_s:                                       # Est-ce la touche 'S' ?
                            self._sound = not self._sound                                   # Oui : J'enlève ou remets le son
                        elif event.key == pygame.K_u:                                       # Est-ce la touche 'U' ?
                            self._lives_unlimited = not self._lives_unlimited               # Oui : J'enlève ou remets les vies infinies
            else:
                # Nettoie 
                self.clean()

                # Gestion des mouvements du Paddle
                if not self.managePaddle():
                    return False

                # Gestion du déplacement de la balle
                self.manageBall()

                # Gestion des collisions de la balle
                self.manageCollision()

                # Si plus de vie alors on sort du jeu vers l'écran final
                if self._lives == 0:
                    return True

                # Afficher les vies, le paddle, les briques, la balle, les points, information sur Pause
                self.blitLives()                                                                # Affiche les vies restantes en bas de la fenêtre de jeu
                self._paddle.blit()                                                             # Afficher le Paddle à son nouvel emplacement
                self._round.blitBricks()                                                        # Afficher les briques qui restent
                self._ball.blit()                                                               # Positionne la balle dans la fenêtre
                self.blitPoints()                                                               # Affiche les points
                self.blitInfos()                                                                # Affiche informations

                # Gestion des rounds
                if not self.manageRound():                                                      # Retourne False si on doit sortir du jeu car nous avons terminé le tout dernier round et donc nous avons gagné
                    return True

                # Actualiser l'écran
                pygame.display.flip()

    # Met la couleur de fond du round à l'emplacement actuel du paddle et e la balle
    def clean(self):
        self._screen.fill(self._round._background, self._ball.rect)
        self._screen.fill(self._round._background, self._paddle.rect)

    def managePaddle(self):
        for event in pygame.event.get():                                                    # Parcourir les évènements reçus par l'application
            # Gestion de la sortie de l'application
            if event.type == pygame.QUIT:                                                   # A t'on reçu un évènement "QUIT" ?
                return False                                                                # Oui : Valeur de sortie qui indiqu que l'on veut sortir de l'application
            # Gestion du déplacement du Paddle
            elif event.type == pygame.MOUSEMOTION:                                          # A t'on déplacé la souris ?
                self._paddle.setPosition(pygame.mouse.get_pos()[0])
            elif event.type == pygame.KEYDOWN:                                              # A t'on une touche pressée ?
                if event.key == pygame.K_LEFT:                                              # Oui : est-ce la flêche gauche ?
                    self._paddle.setPosition(self._paddle.rect.centerx - 1)
                elif event.key == pygame.K_RIGHT:                                           # Est-ce la flêche droite ?
                    self._paddle.setPosition(self._paddle.rect.centerx + 1)
            # Gestion du lancement de la balle
            elif event.type == pygame.MOUSEBUTTONUP:                                        # A t'on appuyé sur un bouton de la souris ?
                if self._ball._speed == 0:                                                  # Oui : la vitesse de la balle est-elle à 0 ?
                    self._ball._speed = BALL_SPEED
                    self._ball.setDirection(BALL_START_ANGLE)                               # Fixe le vecteur direction en fonction d'nu angle et de la vitesse
            elif event.type == pygame.KEYUP:                                                # A t'on appuyé sur une touche ?
                if event.key == pygame.K_SPACE:                                             # Oui : est-ce la touche ESPACE ?
                    if self._ball._speed == 0:                                              # Oui : la vitesse de la balle est-elle à 0 ?
                        self._ball._speed = BALL_SPEED
                        self._ball.setDirection(BALL_START_ANGLE)                           # Fixe le vecteur direction en fonction d'nu angle et de la vitesse
                elif event.key == pygame.K_p:                                               # Oui : est-ce la touche 'P' ?
                    self._pause = True                                                      # Je mets en Pause
                elif event.key == pygame.K_s:                                               # Oui : est-ce la touche 'S' ?
                    self._sound = not self._sound                                           # J'enlève ou remets le son
                elif event.key == pygame.K_u:                                               # Oui : est-ce la touche 'U' ?
                    self._lives_unlimited = not self._lives_unlimited                       # J'enlève ou remets les vies infinies

        return True

    def manageBall(self):
        if self._ball._speed == 0:                                                          # La vitesse de la balle est-elle nulle ?
            self._ball.setPosition([self._paddle.rect.centerx, self._paddle.rect.y - self._ball.rect.height / 2]) # Oui donc la position de la balle est au milieu du Paddle
        else:
            self._ball.setPosition([self._ball.rect.centerx + self._ball._direction[0], self._ball.rect.centery + self._ball._direction[1]])

            # Si la vitesse de la balle est 0 alors cela signifie que l'on a touché le bas de l'écran et que par conséquent on perd une vie
            if self._ball._speed == 0: 
                if not self._lives_unlimited:                                               # Est-on en vies infinies ou pas ?
                    self._lives -= 1                                                        # Non donc j'enlève une vie
                self._successive_hits = 0                                                   # Réinitialiser le nombre de hits successifs
                if self._sound:
                    if self._lives > 0:
                        self._sound_out.play()                                              # Joue le son du contact entre la balle et le bas de la fenêtre
                    else:
                        self._sound_gameover.play()                                         # Joue le son de fin de partie

            # Jouer un son de contact entre la balle et un mur si on touche un mur
            if self._sound:
                if (self._ball.rect.centerx == self._ball._zone.x) or (self._ball.rect.centerx == self._ball._zone.x + self._ball._zone.width) or (self._ball.rect.centery == self._ball._zone.y):
                    self._sound_wall.play()                                                 # Joue le son du contact entre la balle et le bas de la fenêtre

    def manageCollision(self):
            # Collision de la balle avec le Paddle
            self.collideBallPaddle()

            # Collision de la balle avec les briques
            self.collideBallBrick()

    def collideBallPaddle(self):
        collision_point = pygame.sprite.collide_mask(self._paddle, self._ball)
        if collision_point != None:
            # Déterminer la partie du paddle qui est touchée 
            part = int(collision_point[0] // (self._paddle.rect.width / 6))
            if part == 6:                                                                   # Cas exceptionnel qui pourrait se produire
                part = 5
            # Angles
            angles = [140, 115, 100, 80, 65, 40]
            self._ball.setDirection(angles[part])

            # Jouer un son
            if self._sound:
                self._sound_paddle.play()                                                   # Joue le son du contact entre la balle et la raquette

    def collideBallBrick(self):
        # D'abord on teste la collision avec les briques indestructibles (gold)
        bricks_collided = pygame.sprite.spritecollide(self._ball, self._round._bricks_gold, False, pygame.sprite.collide_mask)
        if len(bricks_collided) > 0:
            self.manageCollidedBricks(bricks_collided)

        # Ensuite on teste avec les briques destructibles
        bricks_collided = pygame.sprite.spritecollide(self._ball, self._round._bricks, False, pygame.sprite.collide_mask)
        if len(bricks_collided) > 0:
            self.manageCollidedBricks(bricks_collided)

    def manageCollidedBricks(self, bricks_collided):
        # Déterminer de quelle brique la balle est le plus proche
        min_distance = 99999
        closed_brick = None
        for brick in bricks_collided:
            distance = math.sqrt((self._ball.rect.centerx - brick.rect.centerx) * (self._ball.rect.centerx - brick.rect.centerx) + (self._ball.rect.centery - brick.rect.centery) * (self._ball.rect.centery - brick.rect.centery))
            if distance < min_distance:
                min_distance = distance
                closed_brick = brick
        
        # Gérer la balle en fonction de la localisation de l'impact sur la brique
        # On regarde où est positionnée la balle par rapport à la brique
        if (self._ball.rect.centerx >= closed_brick.rect.left) and (self._ball.rect.centerx <= closed_brick.rect.right):
            # Au-dessus ou en-dessous
            if self._ball.rect.centery < closed_brick.rect.centery:
                # Au-dessus
                self._ball._direction[1] = -abs(self._ball._direction[1])               # La balle repart vers le haut
            else:
                # En-dessous
                self._ball._direction[1] = abs(self._ball._direction[1])                # La balle repart vers le haut
        else:
            # A droite ou à gauche
            if self._ball.rect.centerx < closed_brick.rect.centerx:
                # A gauche
                self._ball._direction[0] = -abs(self._ball._direction[0])               # La balle repart vers la gauche
            else:
                # A droite
                self._ball._direction[0] = abs(self._ball._direction[0])                # La balle repart vers la droite

        # La brique a été touchée, mettre à jour son compteur de touches
        # Je tiens compte du fait que si une brique a un nombre de touche < 0 alors elle est indestructible
        if closed_brick._hits > 0:
            closed_brick._hits -= 1

        # Si hits est à 0 il faut détruire la brique et comptabiliser les points
        if closed_brick._hits == 0:
            # Effacer l'endroit où il y a la brique
            self._screen.fill(self._round._background, closed_brick.rect)                   # Effacer la brique à son emplacement

            # Mettre à jour les points
            self._points += closed_brick._points

            # Retirer la brique
            self._round._bricks.remove(closed_brick)

            # On a détruit une brique donc je dois incrémenter le nombre hits successifs...
            self._successive_hits += 1
            # ...et mettre à jour la vitesse de la balle
            self._ball.setSpeed(BALL_SPEED + (self._successive_hits // SPEED_HIT_INC))      # Je pase par la fonction car je dois modifier le vecteur d'orientation

            # Jouer un son
            if self._sound:
                self._sound_brick.play()                                                    # Joue le son du contact entre la balle et une brique qui se détruit
        else:
            # Jouer un son
            if self._sound:
                self._sound_brick_live.play()                                               # Joue le son du contact entre la balle et une brique non encore détruite

    def manageRound(self):
        # S'il ne reste plus de brique dans le Round alors on passe au suivant
        if len(self._round._bricks) == 0:
            # Placer la balle en dehors de la scéne de sorte qu'on ne la voit pas
            self._ball.setPosition([-self._ball.rect.width, 0])
            self._ball._speed = 0                                                           # Stopper la vitesse de la balle
            self._successive_hits = 0                                                       # Réinitialiser le nombre de hits successifs
            if self._round._round_no < len(ROUNDS):
                self._round._round_no += 1                                                  # Y a t'il un autre round qui suit ?
                self._round.update()                                                        # Mettre à jour la zone de jeu
                return True
            else:
                # Nous avons atteint la fin du jeu
                return False
        else:
            return True

    def blitLives(self):
        # Uniquement s'il nous reste au moins une vie
        if self._lives > 0:
            # Afficher le nombre de vies restantes
            screen_dimensions = self._screen.get_rect()
            paddle_life_dimensions = self._paddle_life_image.get_rect()
            for i in range(self._lives - 1):
                self._screen.blit(self._paddle_life_image, (30 + i * (paddle_life_dimensions.width + 5), screen_dimensions.height - 20))
            
            # Effacer les emplacements où il y a pu y avoir des vies qui ont été perdues
            for i in range(NB_LIVES - self._lives):
                self._screen.fill(self._round._background, (30 + (NB_LIVES - 2 - i) * (paddle_life_dimensions.width + 5), screen_dimensions.height - 20, paddle_life_dimensions.width, paddle_life_dimensions.height))

    def blitPoints(self):
        # Le score en texte
        text_image = self._font_medium.render('{0}'.format(self._points), True, (255, 255, 255))

        # topleft où on écrit le texte
        topleft = ((self._screen.get_rect().width) / 2 - (text_image.get_rect().width / 2), 0)

        # Effacer la zone où on écrit le score sinon cela se superpose
        self._screen.fill(BACKGROUND_COLOR, (0, 0, self._screen.get_rect().width, self._top_offset))

        # Ecrire le texte
        self._screen.blit(text_image, topleft)

    def blitInfos(self):
        # Pause
        if self._pause:
            color = (255, 255, 255)
        else:
            color = (128, 128, 128)
        text_image = self._font_small.render(INFOS_PAUSE, True, color)
        self._screen.blit(text_image, (self._screen.get_rect().width - text_image.get_rect().width - 5, 1))

        # Son
        if self._sound:
            color = (255, 255, 255)
        else:
            color = (128, 128, 128)
        text_image = self._font_small.render(INFOS_SOUND, True, color)
        self._screen.blit(text_image, (self._screen.get_rect().width - text_image.get_rect().width - 5, 1 + text_image.get_rect().height - 2))

        # Vies infinies
        if self._lives_unlimited:
            color = (255, 255, 255)
        else:
            color = (128, 128, 128)
        text_image = self._font_small.render(INFOS_LIVES, True, color)
        self._screen.blit(text_image, (self._screen.get_rect().width - text_image.get_rect().width - 5, 1 + text_image.get_rect().height * 2 - 4))
