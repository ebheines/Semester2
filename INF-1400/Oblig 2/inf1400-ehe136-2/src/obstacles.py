import pygame, random, math

pygame.init()

SCREENX = 1600
SCREENY = 900

class Obstacles(pygame.sprite.Sprite):
    SIZEOFOBSTICLE = 10
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.SIZEOFOBSTICLE*2, self.SIZEOFOBSTICLE*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (self.SIZEOFOBSTICLE, self.SIZEOFOBSTICLE), self.SIZEOFOBSTICLE)

        self.position = pygame.Vector2(random.randint(0, SCREENX), random.randint(0, SCREENY))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    
    def update():
        pass