import pygame, math, random

SCREENX = 1600
SCREENY = 900
DISPLAY = (SCREENX, SCREENY)
screen = pygame.display.set_mode(DISPLAY, True)
pygame.display.set_caption("Boids")

class Vehicle(pygame.sprite.Sprite):
    SIZEOFVEHICLE = 30
    def __init__(self, position, velocity, min_speed, max_speed, max_force):
        super().__init__()
        #pygame.transform.scale(self.image, (self.SIZEOFVEHICLE, self.SIZEOFVEHICLE))

        self.min_speed = min_speed
        self.max_speed = max_speed
        self.max_force = max_force

        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)

        self.acceleration = pygame.Vector2(random.random(), random.random())

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # Updating the different variables to make the objects move     
    def update(self) -> None:
        self.position += self.velocity
        self.velocity += self.acceleration
        self.rect.center = self.position
        self.velocity.scale_to_length(self.max_speed)
        self.rotate_image()

        self.acceleration *= 0
    
    def rotate_image(self) -> None:
        """
        Rotating the image after the direction it's going       
        """
 
        angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x))
        self.image = pygame.transform.rotate(self.originalImage, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    # Function for spawing the vehicles inside the screen if they go outside the border of the screen
    def no_edges(self) -> None:
        if self.position.x > SCREENX:
            self.position.x = 0

        elif self.position.x < 0:
            self.position.x = SCREENX
        
        elif self.position.y > SCREENY:
            self.position.y = 0
        
        elif self.position.y < 0:
            self.position.y = SCREENY

    