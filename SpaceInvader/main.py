#python 3.8.6 64-bit
#pip install pygame
import pygame
import random

#*initialize the pygame
pygame.init()

#create screen of width, height; top left corner (0,0) 
screen = pygame.display.set_mode((800,600))

#background image
bg = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/back_image.png')#same as window size, 800,600


#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/si_icon.png')#32 pixel and png
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/player_img2.png')#64 pixel and png
playerX,playerY =370,480 #initial position 
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/alien.png')#64 pixel and png
enemyX, enemyY =random.randint(0,800),random.randint(50,150) #random initial position of enemy
enemyX_change, enemyY_change = 0.6,25

def player(x,y):
    screen.blit(playerImg,(x,y))#blit -- draw

def enemy(x,y):
    screen.blit(enemyImg,(x,y))#blit -- draw

#game loop - show game window until a close/quit event occurs
running = True
while running:
    #RGB - 0 to 255 
    screen.fill((0,0,0))#screen drawn first the img is kept on top else img wont be seen 
    
    #background image
    screen.blit(bg,(0,0))
    #playerX+=0.1#movement on x axis towards right 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN: #key pressed
            print('A Keystoke is pressed')
            if event.key == pygame.K_LEFT:
                print('Left Arrow Key Pressed')
                playerX_change = -0.3 #move to left
            if event.key == pygame.K_RIGHT:
                print('Right Arrow Key Pressed')
                playerX_change = 0.3 #move to right
        if event.type == pygame.KEYUP:#key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('Keystoke Realeased')
                playerX_change = 0 #stop moving


    playerX += playerX_change 
    #stopping at borders of left and right
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    enemyX += enemyX_change 
    #borders of left and right and move down 
    if enemyX <= 0:
        enemyX_change = 0.5 #left to right 
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.5 #right to left
        enemyY  += enemyY_change

    player(playerX,playerY) 
    enemy(enemyX,enemyY) 

    pygame.display.update()#*game window needs to be updated always