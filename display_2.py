import pygame
from display import Canvas

class Canvas_2(Canvas):
    width  = 900
    height = 670
    display = pygame.display.set_mode((width, height))

    def __init__(self, player):

        self.image = pygame.image.load('images/level2.png')
        self.time  = pygame.time.Clock()
        self.speed = player.xspeed
        self.fps   = 120

        self.x = 0
        self.y = 0

        self.left_limit  = 0
        self.right_limit = -5175

    def show(self, player):
        self.caption = pygame.display.set_caption('Mario Game - FPS: %d' % (self.time.get_fps()))
        self.display.blit(self.image, (self.x, self.y))

