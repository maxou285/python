import pygame
from player import Player
from monster import Monster
# Creer une seconde class qui va representer notre jeu
class Game:

    def __init__(self):
        # generer notre joueur
        self.player = Player()
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)

