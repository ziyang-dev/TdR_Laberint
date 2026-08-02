import pygame
import config
import copy

from representation.maze_representation import drawGrid, drawAuxiliaryLines, add_list_to_maze
from representation.graph_representation import maze_to_tree_graph1, maze_to_tree_graph2


from generate.recursive_backtracker import algorithm_recursive_backtracker
from generate.prim_algorithm import algorithm_prim
from generate.binary_tree import algorithm_binary_tree
from generate.sidewinder import algorithm_sidewinder
from generate.recursive_division import algorithm_recursive_division
from generate.wilson_algorithm import algorithm_wilson

from research.DFS import algorithm_DFS

def animate_next():
    global maze
    try:
        maze=next(gen)
    except StopIteration:
        pass

gen=None
maze=algorithm_recursive_division(config.Maze_size.medium)
maze_copy=copy.deepcopy(maze)
maze=add_list_to_maze(maze, algorithm_DFS(maze,config.start_pos, config.exit_pos, config.direction), 3)



#calculs d'altres constants
gridNumber=len(maze)
gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores





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

