import pygame
pygame.init()

# game dimensions
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('school project')

# screen width variables
screenWidth = 500
screenHeight = 500

# character dimensions
x = 50
y = 50
width = 40
height = 60
vel = 8

# jump variables
isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # game controls
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and x <= screenWidth - width: # right
        x += vel

    if key[pygame.K_LEFT] and x > vel : # left
        x -= vel
    if not (isJump):
        if key[pygame.K_UP] and y > vel: # up
            y -= vel
        if key[pygame.K_DOWN] and y <= screenHeight - height: # down
            y += vel
        if key[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()