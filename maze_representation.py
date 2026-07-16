import pygame
import Color

def drawGrid(surface,maze,gridSize,gridNumber):
    for y in range(gridNumber): #dibuixar totes les caselles
        for x in range(gridNumber):
            n=maze[y][x]
            if n!=0:
                color=numberToColor(n)
                pygame.draw.rect(surface,color,(x*gridSize,y*gridSize,gridSize,gridSize))
    #sobremarcar les sortides
    pygame.draw.rect(surface,Color.star,(1*gridSize,0*gridSize,gridSize,gridSize))
    pygame.draw.rect(surface,Color.exit,((gridNumber-2)*gridSize,(gridNumber-1)*gridSize,gridSize,gridSize))

def drawAuxiliaryLines(surface,gridSize,gridNumber,width,height):
    for i in range(1,gridNumber): #dibuixar graella de auxiliar
        pygame.draw.line(surface, Color.line, (i*gridSize, 0), (i*gridSize, height), 1)
        pygame.draw.line(surface, Color.line, (0,i*gridSize), (width,i*gridSize), 1)


def numberToColor(n): #Donar a cada nombre un color
    match n:
        case -1:
            return Color.wall
        case 1:
            return Color.wall
        case _:
            return Color.error