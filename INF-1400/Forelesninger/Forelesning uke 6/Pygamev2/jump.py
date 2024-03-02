import pygame, sys, random

pygame.init()

# INITIALIZE SCREEN
SCREENX = 1656
SCREENY = 940
DIS = (SCREENX, SCREENY)
screen = pygame.display.set_mode(DIS, True)
pygame.display.set_caption("Svein's travel to Senja")
framerate = 60
font = pygame.font.Font('freesansbold.ttf', 75)
score = 0
timer = pygame.time.Clock()

# BACKGROUND INFO
background = pygame.transform.scale(pygame.image.load("background.webp"), DIS)
x1_background = 0
x2_background =  1656
speed_background = -0.5
state_background = "onscreen"

# PLAYER INFO
image_player = pygame.transform.scale(pygame.image.load("player.webp"), (150, 275))
x_player = 300
y_player = 503
speed_player = 0

# BLOCKS 
