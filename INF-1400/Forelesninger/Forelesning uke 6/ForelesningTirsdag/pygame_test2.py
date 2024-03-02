import pygame
import random

SX = 1200
SY = 900

NAR_FILE = "naruto.webp"
BACK_FILE = "mario.webp"
PANDA_FILE = "panda.webp"

pygame.init()

screen = pygame.display.set_mode((SX,SY), 0)
background = pygame.image.load(BACK_FILE)
background = pygame.transform.scale(background, (SX, SY))

naruto = pygame.image.load(NAR_FILE)
naruto = pygame.transform.scale(naruto, (150, 135))
panda = pygame.image.load(PANDA_FILE)
panda = pygame.transform.scale(panda, (200, 200))

class Drawable:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def move(self):
         pass

    def draw(self):
        self.move()
        screen.blit(self.img, (self.x, self.y))

class Naruto(Drawable):
    def __init__(self, x, y, img, speed):
        super().__init__(x, y, img)
        self.speed = speed

    def move(self):
        self.x += self.speed
        if self.x < 0:
            self.speed = abs(self.speed)
        if self.x > SX:
            self.speed = -abs(self.speed) 

class Panda(Drawable):
    def __init__(self, x, y, speed):
        super().__init__(x, y, panda)
        self.speed_x = speed[0]
        self.speed_y = speed[1]
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 0:
            self.speed_x = abs(self.speed_x)
        if self.y < 0:
            self.speed_y = abs(self.speed_y)
        if self.x > SX-150:
            self.speed_x = -abs(self.speed_x)
        if self.y > SY-150:
            self.speed_y = -abs(self.speed_y)

#panda1 = Panda(SX/2, 650, (2, 2))

#naruto1 = Naruto(200, 650, naruto, 2)
#naruto2 = Naruto(300, 650, naruto, 3)

pandas = []
narutos = []

for _ in range(10):
    x_pos = random.randint(0, SX)
    y_pos = random.randint(0, SY)
    speed_x = random.randint(1, 4)
    speed_y = random.randint(1, 4)
    pandas.append(Panda(x_pos, y_pos, (speed_x, speed_y)))

for _ in range(10):
    x_pos = random.randint(0, SX)
    y_pos = random.randint(0, SY)
    speed = random.randint(20, 30)
    narutos.append(Naruto(x_pos, y_pos, naruto, speed))



while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
        
    screen.blit(background, (0,0))

    for panda in pandas:
        panda.draw()

    for naruto in narutos:
        naruto.draw()

    #panda1.draw()

    #naruto1.draw()
    #naruto2.draw()

    pygame.display.update()

print("\nExecution of pygame is finished, have a great day:D")
