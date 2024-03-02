from __future__ import annotations
import pygame, random, math
from random import uniform

from boidshoiks import Boid, Hoik
from obstacles import Obstacles


pygame.init()

# Varibles for the screen
SCREENX = 1600
SCREENY = 900
DISPLAY = (SCREENX, SCREENY)

# Initializing the screen and caption
screen = pygame.display.set_mode(DISPLAY, True)
background = pygame.transform.scale(pygame.image.load("sky.webp"), DISPLAY)
pygame.display.set_caption("Boids")

# Making a sprite-group and list for the obstacles
obstacles = pygame.sprite.Group()
obs = []

# Adding the obstacles to the group and list
for _ in range(5):
    obs.append(Obstacles())
    obstacles.add(obs)

# Making a sprite-group and list for the boids
movingboid = pygame.sprite.Group()
boids = []

# Adding the boids to the group and list
for _ in range(100):
    boids.append(Boid())
    movingboid.add(boids)

# Making a sprite-group and list for the hoiks
movinghoik = pygame.sprite.Group()
hoiks = []

# Adding the hoiks to the group and list
for _ in range(3):
    hoiks.append(Hoik())
    movinghoik.add(hoiks)


running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("\nBoids ended, have a great day :D\n")
    
    
    movingboid.update()
    movingboid.draw(screen)

    movinghoik.update()
    movinghoik.draw(screen)

    obstacles.draw(screen)

    for boid in boids:
        boid.avoid_hoiks(obs)
        boid.no_edges()
        boid.avoid_hoiks(hoiks)
        boid.flock(boids)
    
    for hoink in hoiks:
        hoink.collison(boids, movingboid)
        hoink.no_edges()
        hoink.hunting(boids)

  
    pygame.display.flip()

