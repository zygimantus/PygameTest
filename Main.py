from sys import exit

import pygame
from pygame.locals import *

import Constants

__author__ = 'Zygimantus'

screen = pygame.display.set_mode(Constants.SCREEN_SIZE, 0, 32)
pygame.display.set_caption(Constants.CAPTION)
pygame.init()

while True:
    event = pygame.event.wait()

    if event.type == QUIT:
        exit()