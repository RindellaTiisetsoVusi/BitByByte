import pygame, sys 
from pygame.locals import *
from pygame import mixer
import time
import random

#Initializing
pygame.init()

#Game Constraints
GREEN = [50,205,50]
DGREEN = [2,48,32]
PURPLE = [48,25,52]
WHITE = [255,255,255]
WHEAT = [245, 222, 179]
COGNANT = [131, 67, 51]
BLACK = [0,0,0]
RED = [255,0,0]
AMBER = [255, 195, 0]
width = 700
height = 600

#Screen Creation
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Ssssnake')
clock = pygame.time.Clock() 

#Loading Images
icon = pygame.image.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\snake.png')
fruit = pygame.image.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\plum.png')
background1 = pygame.image.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\background1.JPG')
background2 = pygame.image.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\background3.JPG')
background3 = pygame.image.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\background4.JPG')

#Scaling Images
snakePic = pygame.transform.scale(icon,(350,250)) 
fruitPic = pygame.transform.scale(fruit,(50,60))
background1 = pygame.transform.scale(background1,(200,200)) 
background2 = pygame.transform.scale(background2,(200,200))
background3 = pygame.transform.scale(background3,(200,200))
gameArea1 = pygame.transform.scale(background1,(700,600)) 
gameArea2 = pygame.transform.scale(background2,(700,600)) 
gameArea3 = pygame.transform.scale(background3,(700,600)) 

#Positioning
titlePos = (130,10) #(x,y)
gameTitlePos = (250,10)
instrPos = (10, 300)
bodyPos = (50,355)
snakePicPos = (250,50)
fruitPicPos = (150,200)
background1Pos = (20,380)
background2Pos = (250,380)
background3Pos = (480,380)
scorePos = (0,25)

#Setting Font
pygame.display.set_icon(icon)
titleFont = pygame.font.Font('freesansbold.ttf', 40)
bodyFont = pygame.font.Font('freesansbold.ttf', 18)
instrFont = pygame.font.Font('freesansbold.ttf', 15)

def GameOver(lost, color):
    screen.fill(DGREEN)
    msg = titleFont.render(lost, True, color )
    screen.blit(msg, [10,100])
    screen.blit(snakePic, [200,200])

def Score(points):
    score = bodyFont.render("Score: " + str(points), True, WHITE, BLACK)
    screen.blit(score, [0, 0])

def Snake(snakeBlock, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(screen, color, [x[0], x[1], snakeBlock, snakeBlock])

def StartMenu(): #Screen Splash
    mixer.music.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\snakeStart.mp3')
    mixer.music.play(1)

    message1 = titleFont.render("Welcome to Ssssnake", True, WHITE, DGREEN)
    message2 = instrFont.render("INSTRUCTIONS: Eat as many fruits as possible. Use keyboard arrows to move snake.", True, WHITE)
    message3 = bodyFont.render("CHOOSE GAME BACKGROUND TO START, Press 1,2, or 3 to choose", True, WHITE)
    
    screen.fill(DGREEN)
    screen.blit(message1, titlePos)
    screen.blit(message2, instrPos)
    screen.blit(snakePic, snakePicPos)
    screen.blit(fruitPic, fruitPicPos)
    screen.blit(message3, bodyPos)
    
    screen.blit(background1, background1Pos)
    screen.blit(background2, background2Pos)
    screen.blit(background3, background3Pos)

    start = True

    #Choose background
    while start:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    GameArena(gameArea1, WHEAT, GREEN)

                if event.key == pygame.K_2:
                    mixer.music.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\Wind.wav')
                    mixer.music.play(-1)
                    GameArena(gameArea2, COGNANT, PURPLE)

                if event.key == pygame.K_3:
                    mixer.music.load(r'C:\Users\user\Desktop\Python1\GameDev\Block3_4\Forest.wav')
                    mixer.music.play(-1)
                    GameArena(gameArea3, AMBER, RED)
                    

        pygame.display.update()

def GameArena(background, snakeTitleCol, foodCol):

    playing = True
    gameOver = False
    velocity = 40
    snakeBody = 10

    snakeX = width/2
    snakeY = height/2
 
    directionX = 0
    directionY = 0
 
    snakeArr = []
    snakeLength = 1
 
    foodX = round(random.randrange(0, width - snakeBody) / 10.0) * 10.0
    foodY = round(random.randrange(0, height - snakeBody) / 10.0) * 10.0
 
    while playing:
 
        while gameOver == True:
            GameOver("GAMEOVER!!! Press R Play Again", WHITE)
            Score(snakeLength - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        StartMenu()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keyPress = pygame.key.get_pressed()
        if keyPress[pygame.K_UP]:
            directionY = -snakeBody
            directionX = 0
        if keyPress[pygame.K_DOWN]:
            directionY = snakeBody
            directionX = 0
        if keyPress[pygame.K_LEFT]:
            directionX = -snakeBody
            directionY = 0
        if keyPress[pygame.K_RIGHT]:
            directionX = snakeBody
            directionY = 0  
 
        if snakeX >= width or snakeX < 0 or snakeY >= height or snakeY < 0:
            gameOver = True

        snakeX += directionX
        snakeY += directionY

        screen.blit(background, (0,0))
        title = titleFont.render("Ssssnake", True, snakeTitleCol) 
        screen.blit(title, gameTitlePos)

        pygame.draw.rect(screen, foodCol, [foodX, foodY, snakeBody, snakeBody])
        snake_Head = []
        snake_Head.append(snakeX)
        snake_Head.append(snakeY)
        snakeArr.append(snake_Head)

        if len(snakeArr) > snakeLength:
            del snakeArr[0]
 
        for x in snakeArr[:-1]:
            if x == snake_Head:
                gameOver = True
 
        Snake(snakeBody, snakeArr, snakeTitleCol)
        Score(snakeLength - 1)
 
        pygame.display.update()
 
        if snakeX == foodX and snakeY == foodY:
            foodX = round(random.randrange(0, width - snakeBody) / 10.0) * 10.0
            foodY = round(random.randrange(0, height - snakeBody) / 10.0) * 10.0
            snakeLength += 1
 
        clock.tick(velocity)

#Game
while True:
    StartMenu()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    



