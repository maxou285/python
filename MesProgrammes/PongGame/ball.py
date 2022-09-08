import pygame

#from main import BallSkinIndex, BallSkinsList
from paddle import Paddle
import random




class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        self.image = pygame.image.load("ressources/BallRect.png")               # BallSkinsList[BallSkinIndex]      "ressources/pong_basketballStart.png"
        self.rect = self.image.get_rect()                                     
        self.init_ball_coords()
        self.image.set_colorkey([0, 255, 0])
        self.direction = "left"
        self.score_J1 = 0
        self.score_J2 = 0
        
    def move(self):
        # detect if players have scored"
        if (self.rect.x > (1080-43)):
            print("Joueur 1 a gagné")
            self.init_ball_coords()
            self.score_J1 += 1
            print(self.score_J1)
        elif (self.rect.x <= 0):
            print("Joueur 2 a gagné")
            self.init_ball_coords()
            self.score_J2 += 1
        # makes the ball bounce on Y axis
        if (self.rect.y > (720-43)) or (self.rect.y <= 0):
            self.speed_y = -self.speed_y
        # updates ball position on screen    
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
    def collision(self, paddle):
        if  pygame.Rect.colliderect(self.rect, paddle.rect) == True:
            self.speed_x = -self.speed_x
            if self.speed_x > 0:
                self.speed_x += 1
            else:
                self.speed_x -= 1
        
    def init_ball_coords(self):
        self.rect.x = (1080-43)/2
        self.rect.y = random.randint(0,720-43)
        self.speed_x = 0
        self.speed_y = 0
        while self.speed_x == 0:
            self.speed_x = random.randint(-3,3)*2
        while self.speed_y == 0:
            self.speed_y = random.randint(-3,3)*2
        
    #def Score_update(self):
        #background = pygame.image.load('ressources/Galaxie1.jpeg') 
       # screen.blit(background, (-100, -100))
