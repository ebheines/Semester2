import pygame
import os

import random

# Display parameters
XSCREEN = 1104 
YSCREEN = 626 
DIS_SIZE = (XSCREEN, YSCREEN)

# Files import
BG_FILE = "background.webp"
PLAYER_FILE = "player.webp"
MUSSO_FILE = "musso.webp"
GO_FILE = "gameover.webp"
START_FILE = "space.png"
BALL_FILE = "ball.webp"


# Let the games begin
pygame.init()

drawn = True
# DISPLAY
screen = pygame.display.set_mode(DIS_SIZE, True, 32)

# FONT
myfont = pygame.font.SysFont("monospace", 16)

background = pygame.image.load(BG_FILE)
background = pygame.transform.scale(background, (DIS_SIZE))
background.convert()

# PLAYER
player = pygame.image.load(PLAYER_FILE)
player = pygame.transform.scale(player, (100, 185))
#player.convert()

# MUSOO
musso = pygame.image.load(MUSSO_FILE)
musso = pygame.transform.scale(musso, (45, 90))
musso.convert()

# START/END
start = pygame.image.load(START_FILE)
start = pygame.transform.scale(start, (480, 360))
start.convert()

end = pygame.image.load(GO_FILE)
end = pygame.transform.scale(end, (300, 200))
end.convert()

# BALL
ball = pygame.transform.scale(pygame.image.load(BALL_FILE), (55, 55))

#ball = pygame.image.load(BALL_FILE)
#ball = pygame.transform.scale(ball, (55, 55))
#ball.convert()


class Draw:
    def __init__(self, x, y, img, xmax, xmin):
        self.x = x
        self.y = y
        self.img = img
        self.xmax = xmax
        self.xmin = xmin

    
    def move(self):
        pass
    
    def draw(self, x):
        self.move()
        screen.blit(self.img, (x, self.y))
    
    #def run(self):
    #    for event in pygame.event.get():
    #        if event.type == pygame.KEYDOWN:
    #            if event.key == pygame.K_RIGHT:
    #                self.speedx += 5
    #            if event.key == pygame.K_LEFT:
    #                self.speedx -= 5

class Player(Draw):
    def __init__(self, x, y, speed, xmax, xmin):
        super().__init__(x, y, player, xmax, xmin)
        self.speed = speed
        self.balls = []

    def move(self):
        self.x += self.speed
        if self.x < self.xmin:
            self.speed = 0
        if self.x > self.xmax:
            self.speed = 0
    
    def musso_moving(self, ymax, ymin, xmax, xmin):
        self.x += self.speed
        if self.y > ymax:
            self.speedy = -abs(self.speedy)
        if self.y < ymin:
            self.speedy = abs(self.speedy)
        if self.x > xmax:
            self.speedx = -abs(self.speedx)
        if self.x < xmin:
            self.speedx = abs(self.speedx)
    
    def shoot(self, shot):
        if shot == 1:
            ball = Ball(self.x, self.y)
            self.balls.append(ball)

class Ball(Player):
    def __init__(self, x, y):
        self.x = x + 100
        self.y = y + 50

    def draw_ball(self):
        screen.blit(ball, (self.x, self.y))
        
# START
#starts = Draw(402, 213, start, True)

# PLAYER
#players = Draw(300, 268, player, True)
x = 200
speed = 0
xmin = 75
xmax = 600
player = Player(x, 335, speed, xmax, xmin)


ballx = x
ball = Ball(ballx, 335)

shoot = 0

def draw_game():
    screen.blit(background, (0,0))
    player.draw(x)
    for ball in player.balls:
        ball.draw_ball()
    pygame.time.delay(30)
    pygame.display.update()


#for _ in range(1):
#    players.append(Player(100, 335, player, 10, 0, 950, 250, 245, 340))

test = False
while test == False:
    
    screen.blit(background, (0,0))
    screen.blit(start, (312, 133))

    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        test = True
    pygame.display.update()
# GAMEPLAY
crash = False
while not crash:
    #player.draw()
    #player1.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -4
            elif event.key == pygame.K_RIGHT:
                speed = 4
            elif event.key == pygame.K_SPACE:
                shoot = 1
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0
            elif event.key == pygame.K_SPACE:
                pass

# MOVE PLAYER
    x += speed
    if x <= xmin:
        speed = 0
    if x >= xmax:
        speed = 0

#SHOT
    player.shoot(shoot)
    

    #sball.draw(ballx)
            

    #speed = 200
    #screen.blit(player, (speed, 335))
#
    #if event.type == pygame.KEYDOWN:
    #    speed = 0
    #    if event.key == pygame.K_RIGHT:
    #        screen.blit(player, (speed + 10, 335))
    #    if event.key == pygame.K_LEFT:
    #        screen.blit(player, (speed - 10, 335))
    
        


    #draw_game()
    pygame.display.update()

print("\nGame has been ended, hope you enjoyed it! See u soon brother <3")


