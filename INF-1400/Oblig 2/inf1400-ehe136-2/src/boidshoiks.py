from __future__ import annotations
import pygame, random, math
from Vehicle import Vehicle
from random import uniform

pygame.init()

SCREENX = 1600
SCREENY = 900

class Boid(Vehicle):
    MIN_SPEED = 1
    MAX_SPEED = 3
    MAX_FORCE = 0.3
    def __init__(self):
        # Creating a image of the boid in a light turqoise color
        self.image = pygame.Surface((self.SIZEOFVEHICLE, self.SIZEOFVEHICLE), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 255, 150),  [(30, 10), (0, 4), (0, 16)])
        self.originalImage = self.image


        # Setting the values for position and velocity of the boid
        self.position = pygame.Vector2(uniform(0, SCREENX), uniform(0, SCREENY))
        self.velocity = pygame.Vector2(uniform(-1, 1) * self.MAX_SPEED, uniform(-1, 1) * self.MAX_SPEED)
        super().__init__(self.position, self.velocity, self.MIN_SPEED, self.MAX_SPEED, self.MAX_FORCE)
    
    def cohesion(self, boids: list[Boid]) -> pygame.Vector2:
        """
        Cohesion: steering to move toward the average heading of local flockmates
        """
        
        perception = 200
        total = 0
        steering = pygame.Vector2()
        
        for otherboids in boids:
            distance = self.position.distance_to(otherboids.position)
            if otherboids != self and distance < perception:
                steering += otherboids.position
                total += 1    
        
        if total > 0:
            steering /= total
            steering -= self.position
            steering.scale_to_length(self.MAX_SPEED)
            steering -= self.velocity
            steering = self.forceLimit(steering)

        return steering
    
    
    def alignment(self, boids: list[Boid]) -> pygame.Vector2:
        """ 
        Alignment: steerting towards the average position of local flockmates
        """
        
        perception = 200
        total = 0
        steering = pygame.Vector2()

        for otherboids in boids:
            if otherboids != self and self.position.distance_to(otherboids.position) < perception:
                steering += otherboids.velocity
                total += 1
            
        
        if total > 0:
            steering /= total
            steering.scale_to_length(self.MAX_SPEED)
            steering -= self.velocity
            steering = self.forceLimit(steering)

        return steering
    

    def separation(self, boids: list[Boid]) -> pygame.Vector2:
        """
        Separation: steer to avoid crowding local flockmates
        """

        steering = pygame.Vector2()
        total = 0
        persepsjon = 50 
        for otherboid in boids:
            if otherboid != self and self.position.distance_to(otherboid.position) < persepsjon:
                differns = (self.position - otherboid.position)
                steering += differns
                total += 1
        
        if total > 0:
            steering /= total   
            steering.scale_to_length(self.MAX_SPEED)
            steering -= self.velocity
            steering = self.forceLimit(steering)
        
        return steering
    

    def avoid_hoiks(self, hoiks: list[Hoik]) -> None:
        """
        Avoid hoiks: avoiding colliding with the hoiks to not get eaten
        """
        steering = pygame.Vector2()
        total = 0
        persepsjon = 200
        for hoik in hoiks:
            if self.position.distance_to(hoik.position) < persepsjon:
                steering = -(hoik.position - self.position).normalize()
                total += 1
        
        self.acceleration += steering
    

    def avoid_obstacles(self, obstacles) -> pygame.Vector2:
        """
        Avoid obstacles: avoiding to collide with the obstacles
        """

        run = pygame.Vector2()
        perseption = 75
        for obs in obstacles:
            if self.position.distance_to(obs.position) < perseption:
                run = -(obs.position - self.position).normalize()
        self.acceleration += run
                

    def forceLimit(self, force) -> int:
        """
        Force limit: limiting the maximum force of the boid
        """

        if 0 < force.magnitude() > self.MAX_FORCE:
            force.scale_to_length(self.MAX_FORCE)
        return force
    

    def flock(self, boids: list[Boid]) -> None:
        """
        Flock: putting cohesion, alignment and separation to 
        """

        cohesion = self.cohesion(boids)
        alignment = self.alignment(boids)
        separation = self.separation(boids)

        self.acceleration += cohesion
        self.acceleration += alignment
        self.acceleration += separation

    def update(self):
        super().update()
    

class Hoik(Vehicle):
    SIZEOFHOIK = 50
    HOIK_MAX_SPEED = 4
    HOIK_MIN_SPEED = 0.2
    HOIK_FORCE = 0.1
    def __init__(self):
        self.image = pygame.Surface((self.SIZEOFVEHICLE, self.SIZEOFVEHICLE), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255, 0, 0),  [(30, 10), (0, 4), (0, 16)])
        self.originalImage = self.image

        self.position = pygame.Vector2(uniform(0, SCREENX), uniform(0, SCREENY))
        self.velocity = pygame.Vector2(uniform(-1, 1) * self.HOIK_MAX_SPEED, uniform(-1, 1) * self.HOIK_MAX_SPEED)        
        super().__init__(self.position, self.velocity, self.HOIK_MIN_SPEED, self.HOIK_MAX_SPEED, self.HOIK_FORCE)


    def hunting(self, boids: list[Boid]) -> pygame.Vector2:
        """
        Hunting: making the hoiks hunt the boids
        """

        hunt = pygame.Vector2()
        perception = 300
        total = 0
        for boid in boids:
            if self.position.distance_to(boid.position) < perception:
                hunt += boid.velocity
                total += 1
        
        if total > 0:
            hunt /= total
            hunt.scale_to_length(self.HOIK_MAX_SPEED)
            hunt -= self.velocity
            hunt = self.forceLimit(hunt)
        
        self.acceleration += hunt
    
    def collison(self, boids: list[Boid], movingboid):
        """
        Collision: if the hoik collide with the boid, the boid will "die" and be removed
        """

        for boid in boids:
            if self.rect.colliderect(boid.rect):
                movingboid.remove(boid)
    
    def forceLimit(self, force) -> int:
        """
        Force limit: limiting the macimum force of the hoik
        """

        if 0 < force.magnitude() < self.HOIK_FORCE:
            force.scale_to_length(self.HOIK_FORCE)
        return force

    def update(self):
        super().update()