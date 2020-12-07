#python 3.8.6 64-bit
#pip install pygame
import pygame
import random
import math
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
playerImg = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/player_img.png')#64 pixel and png
playerX,playerY =370,480 #initial position 
playerX_change = 0

#Enemy
'''
#for single enemy
enemyImg = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/alien.png')#64 pixel and png
enemyX, enemyY =random.randint(0,735),random.randint(50,150) #random initial position of enemy
enemyX_change, enemyY_change = 0.6,25
'''
#multiple enemies
enemyImg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change =[]
no_of_enemy = 6
for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.6)
    enemyY_change.append(25)

#Bullet 
#states : ready - cannot see the bullet on the screen ; fire - bullet is currently moving
bulletImg = pygame.image.load('D:/GITHUB/GAMES/SpaceInvader/bullet.png')
bulletX,bulletY=0,480
bulletX_change, bulletY_change = 0,1
bullet_state = 'ready'

score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))#blit -- draw

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))#blit -- draw

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg,(x+16,y+10))#to fire bullet from center of rocket

def iscollision(enemyX,enemyY,bulletX,bulletY):#distance formula 
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False

#game loop - show game window until a close/quit event occurs
running = True
while running: #for anything that need to be persisited on the screen
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
            #print('A Keystoke is pressed')
            if event.key == pygame.K_LEFT:
                #print('Left Arrow Key Pressed')
                playerX_change = -0.3 #move to left
            if event.key == pygame.K_RIGHT:
                #print('Right Arrow Key Pressed')
                playerX_change = 0.3 #move to right
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':#multiple spacbar changes x coordinates and hence multiple bullets ; 
                                            #for 1 bullet at a time on screen i.e fire if no bullet on screen
                    bulletX = playerX #bullect after firing moving with rocket movement issue handled; \
                                        #first instance of position of rockect is the path to be followed by bullet till 0 coordinate
                                        #gets the current x coordinate of the space ship
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:#key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print('Keystoke Realeased')
                playerX_change = 0 #stop moving


    playerX += playerX_change 
    #stopping at borders of left and right
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    for i in range(no_of_enemy):#for multiple enemy
        enemyX[i] += enemyX_change[i] 
        #borders of left and right and move down 
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5 #left to right 
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5 #right to left
            enemyY[i]  += enemyY_change[i]

        #for collision
        collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            #reset bullet
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            print(score)
            enemyX[i], enemyY[i] =random.randint(0,735),random.randint(50,150) #random initial position of enemy

        enemy(enemyX[i],enemyY[i],i) 

    #Bullet Movement
    if bulletY <= 0: # bullet reset after touching 0 cordinate  and firing again
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    
    player(playerX,playerY) 
    

    pygame.display.update()#*game window needs to be updated always