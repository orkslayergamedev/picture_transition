# IMPORTS
import sys
import time
import pygame

# SCREEN, CLOCK
clock = pygame.time.Clock()
size = width, height = 500, 500
canvas = pygame.Surface(size)
screen = pygame.display.set_mode(size)

# IMAGES
pic1 = pygame.image.load("forest.jpg")
pic2 = pygame.image.load("beach.jpg")
pic1 = pygame.transform.scale(pic1, size)
pic2 = pygame.transform.scale(pic2, size)
pic1_alpha = 0

# STATE, TIME
ST_FADEIN = 0
ST_FADEOUT = 1
state = ST_FADEIN
last_state_change = time.time()
change = False

# SPEED
vel_change = 100

pygame.init()

while 1:
    ## Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Exit the main loop
            sys.exit()
        # Change when enter hit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            change = True

    ## Update the state
    dt = time.time() - last_state_change
    last_state_change = time.time()

    if change:
        # Increasing alpha until maximum
        if state == ST_FADEIN:
            pic1_alpha += dt * vel_change
            if pic1_alpha > 255:
                pic1_alpha = 255
                state = ST_FADEOUT
                change = False
        # Decreasing alpha until minimum
        else:
            pic1_alpha -= dt * vel_change
            if pic1_alpha < 0:
                pic1_alpha = 0
                state = ST_FADEIN
                change = False

    # Display the pictures
    pic1.set_alpha(pic1_alpha)
    canvas.blit(pic2, (0, 0))
    canvas.blit(pic1, (0, 0))

    # Update the screen
    clock.tick(60)
    screen.blit(canvas, (0, 0))
    pygame.display.flip()
