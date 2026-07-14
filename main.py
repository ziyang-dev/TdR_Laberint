import pygame
import color
from maze_representation import drawGrid
maze=[[-1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [-1, 1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1, 0, -1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [-1, 0, -1, 1, -1, 1, -1, 0, -1, 0, -1, 0, -1, 1, -1, 1, -1, 1, -1, 0, -1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], [-1, 0, -1, 1, -1, 0, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [-1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [-1, 1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 0, -1, 0, -1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1], [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, -1, 0, -1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, -1, 1, -1, 1, -1, 0, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], [-1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1]]

#constants
height,width=600,600 # x,y //tamany de la pantalla
#gridNumber=10 #nombre de caselles per cada costat
gridNumber=len(maze)
gridSize=height//gridNumber #tamany de cada casella a un tamany enter
height,width=gridSize*gridNumber, gridSize*gridNumber #ajusta el tamany quitant les vores
windowsCaptionText="Test"  #Nom de finestres




#Pygame init
pygame.init()
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption(windowsCaptionText)
running = True
clock = pygame.time.Clock()

while running:
    #Teclats per sortir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
    
    screen.fill(color.background) #posar color de fons

    for y in range(gridNumber): #dibuixar totes les caselles
        for x in range(gridNumber):
            n=maze[y][x]
            if n!=0:
                drawGrid(screen,n, x, y,gridSize)
    
    #sobremarcar les sortides
    drawGrid(screen,-2,1,0,gridSize)
    drawGrid(screen,-3,gridNumber-2,gridNumber-1,gridSize)

    for i in range(1,gridNumber): #dibuixar graella de auxiliar
        pygame.draw.line(screen, color.line, (i*gridSize, 0), (i*gridSize, height), 1)
        pygame.draw.line(screen, color.line, (0,i*gridSize), (width,i*gridSize), 1)

    pygame.display.update() #actualitzar per cada frame
    clock.tick(30) #ajustar a 30 FPS
pygame.quit()