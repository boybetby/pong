import pygame
import random
import time

pygame.init()

game_width = 720
game_height = 720

screen = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('Pong')

black = (0,0,0)
white = (255,255,255)
font = pygame.font.SysFont('sans',50)

game_level = 0

player1_bar = 310
player1_change = 0
score1 = 0

player2_bar = 310
player2_change = 0.3 
score2 = 0  

ball_speed = 0.1
ball_x = 310
ball_y = 360
ball_x_change = -ball_speed
ball_y_change = 0

running = True

level = True
 
while running :
    screen.fill(black)
    text1=font.render(str(score1),True,white)
    text2=font.render(str(score2),True,white)
    
    pygame.draw.rect(screen,white, (ball_x,ball_y,15,15))  
    
    #ball
    ball_x += ball_x_change
    ball_y += ball_y_change  
    
    #for Player 1  
    if ball_x<=10 and ball_y>=player1_bar and ball_y<=(player1_bar+100):
        if ball_y>=player1_bar and ball_y<player1_bar+49:
            rad = random.randint(1, 4)
            if (rad == 1):
                ball_y_change = -0.1
            elif (rad == 2):
                ball_y_change = -0.03
            elif (rad == 3):  
                ball_y_change = -0.06
            elif (rad == 4):
                ball_y_change = -0.01 
        if ball_y>=player1_bar+49.1 and ball_y<player1_bar+100:
            rad = random.randint(1, 4)
            if (rad == 1):
                ball_y_change = 0.1
            elif (rad == 2):
                ball_y_change = 0.03
            elif (rad == 3):
                ball_y_change = 0.06
            elif (rad == 4):
                ball_y_change = 0.01                   
        ball_x_change = ball_speed    
    if ball_x<=10 and (ball_y<player1_bar or ball_y>(player1_bar+100)):
        score2 += 1
        ball_x = 20
        ball_y = 340
        player1_bar = 310
        player2_bar = 310
        game_level += 1
        if (game_level%4==0): #tang_do_kho
            ball_speed += 0.05 
        time.sleep(0.7)

    #for Player 2  
    if ball_x>690 and ball_y>=player2_bar and ball_y<=(player2_bar+100):
        if ball_y>player1_bar and ball_y<player1_bar+49:
            rad = random.randint(1, 4)
            if (rad == 1):
                ball_y_change = 0.1
            elif (rad == 2):
                ball_y_change = 0.03
            elif (rad == 3):
                ball_y_change = 0.06
            elif (rad == 4):
                ball_y_change = 0.01 
        if ball_y>player1_bar+49.1 and ball_y<player1_bar+100:
            rad = random.randint(1, 4)
            if (rad == 1):
                ball_y_change = -0.1
            elif (rad == 2):
                ball_y_change = -0.03
            elif (rad == 3):
                ball_y_change = -0.06
            elif (rad == 4):
                ball_y_change = -0.01
        ball_x_change = -ball_speed 
    if ball_x>700 and (ball_y<player2_bar or ball_y>(player2_bar+100)):
        score1 += 1
        ball_x = 689
        ball_y = 340
        player1_bar = 310
        player2_bar = 310
        game_level += 1
        if(game_level%4==0): #tang_do_kho
            ball_speed += 0.05 
        time.sleep(0.7)
  
    #screen limit
    if ball_y<10 :
        rad = random.randint(1, 4)
        if (rad == 1):
            ball_y_change = 0.1
        elif (rad == 2):
            ball_y_change = 0.07
        elif (rad == 3):
            ball_y_change = 0.05
        elif (rad == 4):
            ball_y_change = 0.02    
    elif ball_y >710 :   
        rad = random.randint(1, 4)
        if (rad == 1):
            ball_y_change = -0.1
        elif (rad == 2):
            ball_y_change = -0.03
        elif (rad == 3):
            ball_y_change = -0.06
        elif (rad == 4):
            ball_y_change = -0.01      
    
    #AI
    player2_bar += player2_change
    if player2_bar<0 or player2_bar>=620:
       player2_change = -player2_change
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player1_bar>0 and player1_bar<620:
                    player1_bar += -40
            elif event.key == pygame.K_DOWN:
                if player1_bar>=0 and player1_bar<620:
                    player1_bar += 40
            elif event.key==pygame.K_KP_ENTER:    
                main()
            # elif event.key == pygame.K_LEFT: 
            # elif event.key == pygame.K_RIGHT:
               
    pygame.draw.rect(screen,white, (10,player1_bar,10,130))
    pygame.draw.rect(screen,white, (700,player2_bar,10,130))     
    
    screen.blit(text1,(180,60))
    screen.blit(text2,(540,60))  

    pygame.display.flip()
                
pygame.quit()    