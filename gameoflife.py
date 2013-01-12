import pygame
from pygame.locals import *

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Conveys Game Of Life')

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
screen.fill(white)

clock = pygame.time.Clock()

# To initialise a two dimentional array
matrix = [[0 for i in xrange(20)] for i in xrange(20)]

pixel = pygame.PixelArray(screen)
#drawing the grid
for i in range(0,600,30):
   for j in range(0,600,30):
      pygame.draw.rect(screen, red, (i,j,30,30),1)


def birth(i,j):
   pygame.draw.rect(screen, black, (i*30,j*30,30,30))

def death(i,j):
   pygame.draw.rect(screen, white, (i*30,j*30,30,30))

def check(i,j):
   if pixel[i*30+15, j*30+15] == screen.map_rgb(black):
       return 1   
   if pixel[i*30+15, j*30+15] == screen.map_rgb(white):
       return 0
def initial():
    matrix[3][4] = 1
    matrix[4][4] = 1
    matrix[3][5] = 1
    matrix[6][4] = 1
    matrix[3][14] = 1
    matrix[13][4] = 1
    matrix[7][4] = 1
    matrix[8][6] = 1
    matrix[12][9]= 1
    matrix[7][8]=1
    matrix[3][17]=1
    matrix[12][16]=1
    matrix[7][8]=1
    matrix[7][9]=1
    matrix[8][8]=1
    matrix[8][9]=1
    matrix[16][16]=1

def initial2():
    matrix[2][8] = 1
    matrix[2][9] = 1
    matrix[3][8] = 1
    matrix[3][9] = 1
    matrix[6][8] = 1
    matrix[6][9] = 1
    matrix[6][10] = 1
    matrix[7][7] = 1
    matrix[7][11] = 1
    matrix[8][6] = 1
    matrix[8][12] = 1
    matrix[9][6] = 1
    matrix[9][12] = 1
    matrix[10][9] = 1
    matrix[11][7] = 1
    matrix[11][11] = 1
    matrix[12][8] = 1
    matrix[12][9] = 1
    matrix[12][10] = 1
    matrix[13][9] = 1
    matrix[16][7] = 1
    matrix[16][8] = 1
    matrix[16][9] = 1
    matrix[17][7] = 1
    matrix[17][8] = 1
    matrix[17][9] = 1
    
def updating(matr):
    for i in range(20):
         for j in range(20):
              status = matrix[i][j]
              if status == 1: 
                    birth(i,j)
              else: 
                    death(i,j)

def nextstage(m):
    for i in range(1,19):
         for j in range(1,19):
              count = m[i-1][j-1]+m[i][j-1]+m[i+1][j-1]+m[i+1][j]+m[i+1][j+1]+m[i][j+1]+m[i-1][j+1]+m[i-1][j]
              if m[i][j] == 1 and count <= 2:
                      m[i][j] = 0
              elif m[i][j] == 1 and(count == 2 or count == 3):
                      m[i][j] = 1
              elif m[i][j] == 1 and count > 3:
                      m[i][j] = 0
              elif m[i][j] == 0 and count == 3:
                      m[i][j] = 1 
   


initial2()

while True:
    updating(matrix)
    nextstage(matrix)
    pygame.display.update()
    clock.tick(1)
    

'''
initial2()
updating(matrix)
for i in range(0,600,30):
       for j in range(0,600,30):
           pygame.draw.rect(screen, red, (i,j,30,30),1)

pygame.display.update()
'''
raw_input('Press any key to quite')
