import sys
import pygame
import numpy as np
from indices import arrangement
from pygame.locals import *
import indications

# CONSTANTS
screensize = width, height = 1000, 800

# colors
black = (0, 0, 0)
gray = (150, 150, 150)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# OUR GRID MAP:
cellMAP = np.random.randint(2, size=(10, 10))
# [[1 0 0 1 0 0]
#  [1 1 0 1 0 1]
#  [1 1 1 0 0 0]
#  [1 0 0 1 0 0]
#  [1 1 1 1 1 0]
#  [0 0 1 1 1 0]]

#create list to hold data rows and columns
col_list = []
row_list = []

#Get arrangement of squares
arrangement(col_list, row_list, cellMAP)

# VARS
VARS = {'board': pygame.display.set_mode(screensize), 'gridWH': 500,
        'grid_Origin': (250, 150), 'gridCells': cellMAP.shape[0], 'lineWidth': 2}

def main():

    pygame.init()
    pygame.display.set_caption('Nonogram')

    #main loop
    #will keep looping until pygame is closed
    #or when the key "Q" is pressed
    #according to checkEvents()
    while True:
        checkEvents()
        VARS['board'].fill(gray)
        drawSquareGrid(
            VARS['grid_Origin'], VARS['gridWH'], VARS['gridCells'])
        placeCells()
        indications.put_row_nums(row_list)
        indications.put_col_nums(col_list)
        pygame.display.update()


def drawSquareGrid(origin, gridWH, cells):

    x_cord, y_cord = origin

    #draw grid border
    #Top of grid
    pygame.draw.line(
        VARS['board'], white,
        (x_cord, y_cord),
        (gridWH + x_cord, y_cord), VARS['lineWidth'])

    #bottom of grid
    pygame.draw.line(
        VARS['board'], white,
        (x_cord, gridWH + y_cord),
        (gridWH + x_cord, gridWH + y_cord), VARS['lineWidth'])

    #left side of grid
    pygame.draw.line(
        VARS['board'], white,
        (x_cord, y_cord),
        (x_cord, gridWH + y_cord), VARS['lineWidth'])

    #right side of the grid
    pygame.draw.line(
        VARS['board'], white,
        (gridWH + x_cord, y_cord),
        (gridWH + x_cord, gridWH + y_cord), VARS['lineWidth'])

    #get cell size
    cellWH = gridWH / cells

    #adding divisors
    for i in range(cells):
        #vertical divisors
        pygame.draw.line(
            VARS['board'], white,
            (x_cord + (cellWH * i), y_cord),
            (x_cord + (cellWH * i), gridWH + y_cord), VARS['lineWidth'])

        #horizantal divisors
        pygame.draw.line(
            VARS['board'], white,
            (x_cord, y_cord + (cellWH * i)),
            (gridWH + x_cord, y_cord + (cellWH * i)), VARS['lineWidth']
        )


def drawSquareCell(x, y, x_dim, y_dim):
    color = blue
    pygame.draw.rect(
        VARS['board'],
        color,
        (x, y, x_dim, y_dim))

print(cellMAP.shape[0])
# print(cellMAP.shape[1])

#putting cells on board
def placeCells():
    #get cell dimensions
    cellBorder = 1.5
    celldimX = celldimY = (VARS['gridWH']/VARS['gridCells']) - (cellBorder*2)
    #inbedded loop to add each cell
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):

            # Is the grid cell tiled ?
            if cellMAP[column][row] == 1:

                drawSquareCell(
                    VARS['grid_Origin'][0] + (celldimY*row)
                    + cellBorder + (2*row*cellBorder) + VARS['lineWidth']/2,
                    VARS['grid_Origin'][1] + (celldimX*column)
                    + cellBorder + (2*column*cellBorder) + VARS['lineWidth']/2,
                    celldimX, celldimY)


def checkEvents():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()