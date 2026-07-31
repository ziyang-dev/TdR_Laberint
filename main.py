import pygame
import Color
from maze_representation import drawGrid, drawAuxiliaryLines

from generate.recursive_backtracker import algorithm_recursive_backtracker
from generate.prim_algorithm import algorithm_prim
from generate.binary_tree import algorithm_binary_tree
from generate.sidewinder import algorithm_sidewinder
from generate.recursive_division import algorithm_recursive_division
from generate.wilson_algorithm import algorithm_wilson

from graph_representation import maze_to_tree_graph1, maze_to_tree_graph2


maze=algorithm_wilson(10)



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
            #if event.key == pygame.K_SPACE: #sicronizar animacion
            '''else:
                try:
                    maze=next(gen)
                except StopIteration:
                    pass'''

    screen.fill(Color.background) #posar color de fons

    drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
    
    #drawAuxiliaryLines(screen,gridSize,gridNumber,width,height) #dibuixar graella de auxiliar

    pygame.display.update() #actualitzar per cada frame
    clock.tick(240) #ajustar a 30 FPS
pygame.quit()

