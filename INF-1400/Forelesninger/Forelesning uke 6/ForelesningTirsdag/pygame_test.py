import pygame
# "pygame documentaion" to find the commands in pygame

# X and Y size for a window/display
X_SIZE =  1200
Y_SIZE = 900
BG_FILE = "mario.webp"
NAR_FILE = "naruto.webp"

# Need this to initialize pygame
pygame.init()

# Function to make the display/window for our pygame
screen = pygame.display.set_mode((X_SIZE, Y_SIZE), 0)
background = pygame.image.load(BG_FILE)
background = pygame.transform.scale(background, (X_SIZE, Y_SIZE))
background.convert()

naruto = pygame.image.load(NAR_FILE)
naruto = pygame.transform.scale(naruto, (150, 135))
naruto_center = naruto.get_width() / 2
naruto_center = naruto.get_height() / 2

#rect = naruto.get_rect()
#rect.center = 150/2, 135/2

class Naruto:
    def __init__(self, x, y, image, vel):
        self.x = x
        self.y = y
        self.image = image
        self.vel = vel


while True:
# Initializing an event
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

# Drawing "background" to the display
    screen.blit(background, (0, 0))


    keys = pygame.key.get_pressed()

    #if keys[pygame.K_LEFT] and x>0:
    #    x -= vel



    if event.type == pygame.MOUSEMOTION:
        naruto_center_x = pygame.mouse.get_pos()[0] - naruto.get_width() / 2
        naruto_center_y = pygame.mouse.get_pos()[1] - naruto.get_height()

        screen.blit(naruto, (naruto_center_x, naruto_center_y))
    
    #screen.blit(naruto, (X_SIZE/2, Y_SIZE/2))

# Updating whatever is on the display
    pygame.display.update()


print("\nExecution of pygame is finished, have a great day:D")

