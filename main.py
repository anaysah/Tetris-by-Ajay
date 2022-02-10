#IMPORTING ALL DEPENDENCIES----------------------------------------------------------------
import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP
from function import *
import os
import sys

"""
the main file is working properply with all required screens
working with all three screens now
"""

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

cell_size = 30
columes = 10
rows = 20
velocity = -2
change = 0
scoreBoard = 0
running = 2
filledBlocks = creatDic(rows)
random_block = rand_block()
avialabeColor = [(66,133,244),(219,68,55),(244,180,0),(15,157,88)]
blockColor = choice(avialabeColor)

#INITTILIZING PYGAME-----------------------------------------------------------------------
pygame.init()
width,height = columes*cell_size,rows*cell_size
win = pygame.display.set_mode((width,height))    # win.fill((0,0,0))
pygame.display.set_caption("TETRIS by Ajay")
icon_surface = resource_path(r"assests\tetrisLogo.ico")
icon_surface = pygame.image.load(icon_surface)
pygame.display.set_icon(icon_surface)

userevent = pygame.USEREVENT
pygame.time.set_timer(userevent, 500)

fontResource = resource_path(r"assests\SpaceMission-rgyw9.otf")
scoreFont = pygame.font.Font(fontResource, 32)
scoreText = scoreFont.render(f"S: {scoreBoard}", True,blockColor)
scoreRect = scoreText.get_rect()
scoreRect.topright = (295,5)

gameOverText = scoreFont.render("Game Over", True,blockColor)
gameOverRect = gameOverText.get_rect()
gameOverRect.center = (width//2,height//2)

imageResource = resource_path(r"assests\mainFrametetris.png")
mainImage = pygame.image.load(imageResource)
startButton = pygame.draw.rect(win, [255, 0, 0], (80,190,140,50),0)

while running!=5:
    rand_color = randint(0,len(avialabeColor)-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 5
        if event.type == pygame.MOUSEBUTTONDOWN and running==2:
            if startButton.collidepoint(event.pos):running=1
        elif event.type == pygame.KEYUP:
            if event.key==K_DOWN:
                pygame.time.set_timer(userevent, 500)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and a_direction(velocity, change-1, random_block,filledBlocks):
                change-=1
            elif event.key== K_RIGHT and a_direction(velocity, change+1, random_block,filledBlocks):
                change+=1
            elif event.key==K_DOWN:
                pygame.time.set_timer(userevent, 90)
            elif event.key==K_UP:
                random_block = rotate_block(random_block,filledBlocks,velocity,change)
            elif event.key==K_SPACE and running==0:
                running,scoreBoard=1,0
                filledBlocks = creatDic(rows)
        
        if event.type==userevent and running==1:
            if a_direction(velocity+1, change, random_block,filledBlocks):
                velocity+=1
            else:
                running = newBlock(random_block, filledBlocks,velocity,change,rand_color,scoreBoard)
                if running!=0:
                    [random_block,filledBlocks,velocity,change,scoreBoard] = running
                    running = 1
                    blockColor = choice(avialabeColor)


        pygame.event.clear()

    if running==1:
        win.fill((74, 21, 75))
        for r in random_block:
            pygame.draw.rect(win,blockColor,((r[0]+change)*cell_size,(r[1]+velocity)*cell_size,cell_size,cell_size),3)
            pygame.draw.rect(win,blockColor,((r[0]+change)*cell_size+5,(r[1]+velocity)*cell_size+5,20,20),0)

        for i in filledBlocks:
            for r in range(len(filledBlocks[i][0])):
                l = filledBlocks[i]
                pygame.draw.rect(win,avialabeColor[l[1][r]],(l[0][r]*cell_size,i*cell_size,cell_size,cell_size),3)
                pygame.draw.rect(win,avialabeColor[l[1][r]],(l[0][r]*cell_size,i*cell_size,20,20),0)

        scoreText = scoreFont.render(f"S: {scoreBoard}", True,blockColor)
        scoreRect = scoreText.get_rect()
        scoreRect.topright = (295,5)
        scoreText.set_alpha(200)
        win.blit(scoreText, scoreRect)
        
    
    elif running==0:
        win.fill((74, 21, 75))
        win.blit(gameOverText, gameOverRect)
        win.blit(scoreText, scoreRect)

    elif running==2:
        win.fill((74, 21, 75))
        startButton = pygame.draw.rect(win, [255, 0, 0], (80,190,140,50),0)
        win.blit(mainImage, (0,0))

    
    pygame.display.update()
