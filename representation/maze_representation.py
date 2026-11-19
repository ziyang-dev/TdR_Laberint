import pygame
import config

def drawGrid(surface,maze,gridSize,gridNumber):
    for y in range(gridNumber): #dibuixar totes les caselles
        for x in range(gridNumber):
            n=maze[y][x]
            if n!=0:
                color=numberToColor(n)
                pygame.draw.rect(surface,color,(x*gridSize,y*gridSize,gridSize,gridSize))

def drawGraph(surface,maze,gridSize,gridNumber):
    for y in range(gridNumber): #dibuixar totes les caselles
        for x in range(gridNumber):
            n=maze[y][x]
            if n==0:
                color=numberToColor(2)
                pygame.draw.circle(
                    surface, 
                    color, 
                    (x*gridSize+gridSize//2,y*gridSize+gridSize//2), 
                    gridSize//4, 
                    #width=1 if gridSize//40<1 else gridSize//20
                )
                line_size=1 if gridSize//40<1 else gridSize//10
                if y!=gridNumber-1:
                    if maze[y+1][x]==0:
                        pygame.draw.rect(surface,color,(x*gridSize+gridSize//2-line_size/2,y*gridSize+gridSize//2,line_size,gridSize))
                if x!=gridNumber-1:
                    if maze[y][x+1]==0:
                        pygame.draw.rect(surface,color,(x*gridSize+gridSize//2,y*gridSize+gridSize/2-line_size/2,gridSize, line_size))
                                
def draw_exit(surface, gridSize, gridNumber):
    #sobremarcar les sortides
    if gridSize>=4:
        pygame.draw.rect(surface,config.Color.background,(1*gridSize,0*gridSize,gridSize,gridSize*0.75))
        pygame.draw.rect(surface,config.Color.background,((gridNumber-2)*gridSize,(gridNumber-0.7)*gridSize,gridSize,gridSize*0.75))
    pygame.draw.rect(surface,config.Color.star,(1*gridSize,1*gridSize,gridSize,gridSize))
    pygame.draw.rect(surface,config.Color.exit,((gridNumber-2)*gridSize,(gridNumber-2)*gridSize,gridSize,gridSize))

def drawAuxiliaryLines(surface,gridSize,gridNumber,windows_size):
    for i in range(1,gridNumber): #dibuixar graella de auxiliar
        pygame.draw.line(surface, config.Color.line, (i*gridSize, 0), (i*gridSize, windows_size), 1)
        pygame.draw.line(surface, config.Color.line, (0,i*gridSize), (windows_size,i*gridSize), 1)


def numberToColor(n): #Donar a cada nombre un color
    match n:
        case -1:
            return config.Color.error
        case 1:
            return config.Color.wall
        case 2:
            return config.Color.blue
        case 3:
            return config.Color.yellow
        case 4:
            return config.Color.gren
        case 5:
            return config.Color.purple
        case _:
            raise Exception("maze_representation error, can determinat n") 

def add_list_to_maze(maze,list,type):
    for pos in list:
        maze[pos[1]][pos[0]]=type
