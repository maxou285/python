
import pygame
from paddle import Paddle
from paddleopponent import PaddleOpponent
from ball import Ball
# Creer une seconde class qui va representer notre jeu
class Game:

    def __init__(self):
        # generer les raquettes
        self.paddle = Paddle()
        self.paddleopponent = PaddleOpponent()
        self.ball = Ball()
        self.pressed = {}
       

