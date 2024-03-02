import pygame, sys
pygame.init()

BG_FILE = "background.webp"
START_FILE = "space.png"


XS = 1656
XY = 940
DIS = (XS, XY)

# COLORS
red = (255, 0, 0)
white = (255, 255, 255)


screen = pygame.display.set_mode(DIS, True)
pygame.display.set_caption('Mosquito escape')
background = pygame.transform.scale(pygame.image.load(BG_FILE),DIS)
stsc = pygame.transform.scale(pygame.image.load(START_FILE), (XS/2, XY/2))
framerate = 60

gameover = pygame.transform.scale(pygame.image.load("gameover.webp"), (XS/2, XY/2))

font = pygame.font.Font('freesansbold.ttf', 50)
score = 0
timer = pygame.time.Clock()

# BALL PARA
ballimg = pygame.transform.scale(pygame.image.load("ball.webp"), (80, 80))
ballx = 300
bally = 615
ballspeed = 5
ballrad = 25
bxspeed = ballspeed
ballstate = "loaded"


# PLAYER PARA
playerimg = pygame.transform.scale(pygame.image.load("player.webp"), (150, 275))
playerx = 300
playery = 503
playerspeed = 0
player_isjump = False
jumpcount = 10 
jumpvel = 10
playerrect = playerimg.get_rect(topleft=(playerx, playery))

# MUSQUITO
musimg = pygame.transform.scale(pygame.image.load("musso.webp"), (200, 100))
musx = 1600
musy = 615
musspeed = -5
musstate = "loaded"

# SPIDER
spider = pygame.transform.scale(pygame.image.load("spider.webp"), (180, 240))
spiderx1 = 1656
spidery = 600
spiderspeed = -10
spiderstate1 = "offscreen"
spiderrect = spider.get_rect(topleft=(spiderx1, spidery))

# BACKGROUND
bg1x = 0
bg2x = 1656
bgspeed = -2
bgstate = "onscreen"




def player(playerrect):
    screen.blit(playerimg, playerrect)

def shot(ballx, bally):
    global ballstate
    ballstate = "fired"
    screen.blit(ballimg, (ballx, bally))

def enemy(musx, musy):
    global musstate
    musstate = "fired"
    screen.blit(musimg, (musx, musy))

def spidermove(spiderx, spidery):
    global spiderstate
    spiderstate = "onscreen"
    screen.blit(spider, (spiderx, spidery))

def moving_screen():
    global bgstate
    bgstate = "offscreen"
    screen.blit(background, (bg2x, 0))



# STARTSCREEN
starting = True
while starting: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:                
                print("\nThanks for playing")
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                starting = False
    screen.blit(background, (0,0))
    screen.blit(stsc, (380, 250))
    pygame.display.flip()


# GAME
running = True
while running:
    timer.tick(framerate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("\nThanks for playing")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                print("\nThanks for playing")
                pygame.quit()
                sys.exit()
            # MOVE RIGHT
            if event.key == pygame.K_RIGHT:
                playerspeed = 5
            # MOVE LEFT
            if event.key == pygame.K_LEFT:
                playerspeed = -5
            # SHOOTING
            if event.key == pygame.K_SPACE:
                if ballstate == "loaded":
                    ballx = playerrect.x + 50
                    # SHOT BULLET
                    shot(ballx, bally)
            if event.key == pygame.K_UP:
                player_isjump = True
        
            # KEY RELEASE
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerspeed = 0
    
    screen.blit(background, (bg1x,0))
    screen.blit(background, (bg2x, 0))

    playerrect.x += playerspeed

    if bgstate == "onscreen":
        bg1x += bgspeed
        bg2x += bgspeed
    
    if bg2x <= 1:
        bg1x = 0
        bg2x = 1656
        screen.blit(background, (bg1x, 0))
        screen.blit(background, (bg2x, 0))
        
    if spiderstate1 == "offscreen":
        spidermove(spiderx1, spidery)
        spiderx1 += spiderspeed

    if spiderx1 <= 0:
        spiderx1 = 1656
        spiderstate = "offscreen"
    

    if musstate == "loaded":
        enemy(musx, musy)
        musx += musspeed
        
    if playerrect.colliderect(spiderrect):
        print("COLLIDE")

    if playerx <= 50:
        playerx = 50
    elif playerx >= 800:
        playerx = 800
    
    # RELOAD
    if ballx >= 1655:
        ballx = 300
        ballstate = "loaded"
    
    if musx < 0:
        musx = 1600
        musstate = "loaded"

    if ballstate == "fired":
        shot(ballx, bally)
        ballx += ballspeed
        ballx += ballspeed
    
    if musstate == "fired":
        enemy(musx, musy)
        musx += musspeed
    
    if musx <= ballx:
        ballx = 300
        ballstate = "loaded"
        musx = 1600
        musstate = "loaded"
        score += 1
    
    if score >= 10:
        musspeed = -7
    
    if score >= 20:
        musspeed = -9
    
    if score >= 30:
        musspeed = -11
    
    if score >= 40:
        musspeed = -13
    
    if musx <= playerrect.x:
        running = False
    
    #if spiderx1 <= playerx and spidery :
    #    running = False
    #    print("\nSpider got you, GAME OVER")
    
    if (player_isjump):
        if jumpcount >= -10:
            playerrect.y -= (jumpcount * abs(jumpcount)) 
            jumpcount -= 1
        else:
            jumpcount = 10
            player_isjump = False
        


    # SCOREBOARD
    display_score = font.render("Score: " + str(score), True, white)
    screen.blit(display_score, (10, 10))

    player(playerrect)
    

    pygame.display.flip()
    

stop = True
while stop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("\nThanks for playing")
                pygame.quit()
                sys.exit()
    screen.blit(background,(0,0))
    screen.blit(gameover, (425, 200))
    pygame.display.flip()