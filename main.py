import pygame
import config
from representation.maze_representation import drawGrid, drawAuxiliaryLines

from generate.recursive_backtracker import algorithm_recursive_backtracker
from generate.prim_algorithm import algorithm_prim
from generate.binary_tree import algorithm_binary_tree
from generate.sidewinder import algorithm_sidewinder
from generate.recursive_division import algorithm_recursive_division
from generate.wilson_algorithm import algorithm_wilson

from representation.graph_representation import maze_to_tree_graph1, maze_to_tree_graph2

gen=None
maze=algorithm_wilson(10)




#calculs d'altres constants
gridNumber=len(maze)
gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores


def animate_next():
    global maze
    try:
        maze=next(gen)
    except StopIteration:
        pass


#Pygame init
pygame.init()
screen = pygame.display.set_mode((config.windows_size,config.windows_size))
pygame.display.set_caption(config.windowsCaptionText)
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
            else:
                if config.animation_type=="click":
                    animate_next()

    if config.animation_type=="auto":
        animate_next()
    
    screen.fill(config.Color.background) #posar color de fons

    drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint

    if config.with_auxiliary_line:
        drawAuxiliaryLines(screen,gridSize,gridNumber,config.windows_size) #dibuixar graella de auxiliar

    pygame.display.update() #actualitzar per cada frame
    clock.tick(config.ticks) #ajustar a 30 FPS
pygame.quit()

