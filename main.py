#region imports
import pygame
import config
import copy
import numpy as np

from representation.maze_representation import drawGrid, drawAuxiliaryLines, add_list_to_maze
from representation.graph_representation import maze_to_tree_graph1, maze_to_tree_graph2


from generate.recursive_backtracker import algorithm_recursive_backtracker
from generate.prim_algorithm import algorithm_prim
from generate.binary_tree import algorithm_binary_tree
from generate.sidewinder import algorithm_sidewinder
from generate.recursive_division import algorithm_recursive_division
from generate.wilson_algorithm import algorithm_wilson

from generate.braid_maze import braid_maze_break_wall_method, braid_maze_generate_wall_method
from generate.unsolvablem_maze import unsolvablem_maze

from research.DFS import algorithm_DFS
from research.BFS import algorithm_BFS
from research.A_star import algorithm_A_star 

from data_manager import save_maze, load_maze, print_maze_info, load_run_id, print_run_info, save_run_info

from data_collector import collect_data, repeat_collection

from runs_info_safety import verify_runs_safety

#endregion

def animate_next():
    global maze
    try:
        maze=next(gen)
    except StopIteration:
        pass

gen=None

'''id_list=[]
star_id=1
end_id=100
for gen in [1]:
    for size in [1]:
        for id in range(star_id,end_id+1):
            id_list.append(f"M{gen}{size}{id:05d}")
del star_id,end_id,gen,size,id
'''

#for maze_id in id_list:
#    maze =algorithm_recursive_backtracker(config.Maze_size.small)
#    save_maze(maze,maze_id)
maze_id="M1100001"
maze, optimal_path_lenght = load_maze(maze_id)

#add_list_to_maze(maze, path, 3)
#gen=algorithm_A_star(maze,config.start_pos, config.exit_pos, config.direction)

#repeat_collection(id_list,"DFS",5)

#collect_data(maze_id, "BFS")

#print_run_info(load_run_id(vertices_explored=28,is_optimal=1))

print(verify_runs_safety())


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

