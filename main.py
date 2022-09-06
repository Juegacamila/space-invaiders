#import requeride library
import pygame
import random
import math
from pygame import mixer

#Inicialize pygame
pygame.init()

#Wido size
screen_width = 800
screen_height = 600

#Size variable
size = (screen_width, screen_height)

#Display the window
screen = pygame.display.set_mode (size)

#Backgroup image
background = pygame.image.load ("5603526_1876.jpg")

#background music
mixer.music.load("fondo.wav")
mixer.music.play( -1 )

# title
pygame.display.set_caption ("Space Invaders GA")


#Icon
icon = pygame.image.load ("alien.png")
pygame.display.set_icon(icon)

#Player
player_img = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480
player_change_x = 0

#Enemy 
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_chance = []
enemy_y_chance = []

#Number of enemies 
number_enemies = 10



#Create multiples enemies

for item  in range (number_enemies):
    enemy_img.append(pygame.image.load("ufo.png"))
    enemy_x.append(random.randint (0, 800))
    enemy_y.append(random. randint (50, 150))
    enemy_x_chance.append(0.2)
    enemy_y_chance.append(10)



#Bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_chance = 0
bullet_y_chance = 3
bullet_state = "ready"

#Score variable
score = 0

#Font variable
score_font = pygame.font.Font ("sawa.ttf", 32)

#Text position in the screen
text_x = 10
text_y = 10

#Game over font
go_font = pygame.font.Font("Stocky-lx5.ttf", 64 )
go_x = 200
go_y = 250

#Game over function
def game_over (x, y):
    go_text = go_font.render("Game over", True, (255, 255, 255))
    screen.blit ( go_text, (x, y) )


#Score function
def show_text (x, y):
    score_text = score_font.render ("SCORE: " + str( score ), True, (255, 255, 255))
    screen.blit( score_text, (x, y) )


#Playerr function
def player(x, y):
    screen.blit(player_img, (x,y))

#Enemy function
def enemy (x , y, item):
    screen.blit (enemy_img[item], (x,y))

#Bullet fuction
def fire (x , y):
    global bullet_state
    bullet_state = "fire"
    screen.blit (bullet_img,(x + 16 ,y + 10))

#collision function
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2 ) 

    if distance < 27:
        return True
    else:
        return False


#Game loop
running = True
while running:

    #player_x += 0.1
    #print(player_x)
    #player_y+=0.1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    #if keystoke is pressioned,
    #check wheter its right or left
        if event.type == pygame. KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -0.1
                print("LEFT")


            if event.key == pygame.K_RIGHT:
                player_change_x= 0.1

            if event.key == pygame.K_SPACE:

                #Bullet sound
                bullet_sound = mixer.Sound ("blaster-2-81267.wav")
                bullet_sound.play()


                if bullet_state =="ready":
                    bullet_x = player_x
                    fire(bullet_x, bullet_y)

        #Review if keystroke was realed
        if event.type == pygame. KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change_x = 0

        

    #Color RGB: Red - Green - Blue
    rgb = (0, 0, 0,)
    screen.fill( rgb )

    #show backgroup image
    screen.blit (background, (0, 0))

    #Increase or decrease the variable player_x
    player_x += player_change_x

    #Boundaries
    if player_x <= 0:
        player_x = 0
        
    elif player_x >= 736:
         player_x = 736

    #Enemy movements
    for item in range (number_enemies):

        #Game over zone
        if enemy_y [ item ] > 440:
            for j in range (number_enemies):
                enemy_y [ j ] = 2000
                
                #Call game_over function
                game_over (go_x, go_y)

                #Break de loop
                break



        enemy_x [item] += enemy_x_chance[item]

        if enemy_x[item] <= 0:
             enemy_x_chance[item] = 0.2
             enemy_y[item] += enemy_y_chance[item]

        elif enemy_x[item] >= 736:
            enemy_x_chance[item] = -0.2
            enemy_y[item] += enemy_y_chance[item]

        enemy (enemy_x[item],enemy_y[item], item)
        
        #Call the collision function
        collision = is_collision(enemy_x[item], enemy_y[item], bullet_x, bullet_y)
     
        if collision:

            #Explosion sound
            explosion_sound = mixer.Sound ("impact.wav")
            explosion_sound.play()

            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemy_x[item] = random.randint (0, 736)
            enemy_y[item] = random.randint (50, 150)

    #Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"


    if bullet_state == "fire":
        fire (bullet_x, bullet_y)
        bullet_y -= bullet_y_chance


    

    player( player_x,player_y )

    #Call the show_text function
    show_text(text_x, text_y)
    

    #Update the window 
    pygame.display.update()

    

