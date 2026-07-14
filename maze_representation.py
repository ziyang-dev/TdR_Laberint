import pygame
import color

def drawGrid(surface,n,x,y,gridSize):
    color=numberToColor(n)
    pygame.draw.rect(surface,color,(x*gridSize,y*gridSize,gridSize,gridSize))

def numberToColor(n): #Donar a cada nombre un color
    match n:
        case -3:
            return color.exit
        case -2:
            return color.star
        case -1:
            return color.wall
        case 1:
            return color.wall
        case _:
            return color.error