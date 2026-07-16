import pygame
import Color
from maze_representation import drawGrid, drawAuxiliaryLines
maze=[[-1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [-1, 1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1, 0, -1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [-1, 0, -1, 1, -1, 1, -1, 0, -1, 0, -1, 0, -1, 1, -1, 1, -1, 1, -1, 0, -1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], [-1, 0, -1, 1, -1, 0, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [-1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [-1, 1, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1, 1, -1, 1, -1, 0, -1, 0, -1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1], [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, -1, 0, -1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, -1, 1, -1, 1, -1, 0, -1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], [-1, 0, -1, 0, -1, 0, -1, 0, -1, 1, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, -1]]

#constants
height,width=600,600 # x,y //tamany de la pantalla
#gridNumber=10 #nombre de caselles per cada costat
windowsCaptionText="Test"  #Nom de finestres

#calculs d'altres constants
gridNumber=len(maze)
gridSize=height//gridNumber #tamany de cada casella a un tamany enter
height,width=gridSize*gridNumber, gridSize*gridNumber #ajusta el tamany quitant les vores




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
    
    screen.fill(Color.background) #posar color de fons

    drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
    
    drawAuxiliaryLines(screen,gridSize,gridNumber,width,height) #dibuixar graella de auxiliar

    pygame.display.update() #actualitzar per cada frame
    clock.tick(30) #ajustar a 30 FPS
pygame.quit()