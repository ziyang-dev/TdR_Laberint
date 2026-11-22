"""import numpy as np
import config
import psutil

from data_collector import collect_data, repeat_collection
from chart_manager import *

from runs_info_safety import verify_runs_safety, delete_Uinfo

from data_manager import creatDB, convert_to_txt, load_run_id, load_determined_run_info, save_maze
creatDB()

p=psutil.Process()

try:
    p.cpu_affinity([2])
    print(f"Connect Python whit {p.cpu_affinity()} cpu affinity")
except:
    raise Exception ("Can not conect de cpu affinity")
'''
for gen_list in [[1,2,3],[4,5,6],[7,8,9]]:
    id_list=[]
    star_id=1
    end_id=100
    for gen in gen_list:
        for size in [1,2,3,4,5]:
            for id in range(star_id,end_id+1):
                maze_id=f"M{gen}{size}{id:05d}"
                id_list.append(maze_id)
                #save_maze(braid_maze_generate_wall_method(20),maze_id)
                #print(f"saved maze: {maze_id}")

    del star_id,end_id,size,id, gen, maze_id

    repeat_collection(id_list,"all",5)

    print("collection done")

    i=1
    config.experiment_id=config.experiment_id[:4]+f"{i:04d}"

    for _ in verify_runs_safety(auto_generate_maze=True):
        print(i)
        if i >=100:
            break
        i+=1
        config.experiment_id=config.experiment_id[:4]+f"{i:04d}"

    print(delete_Uinfo())

    experiment_turn=int(config.experiment_id[2:4])+1
    config.experiment_id=config.experiment_id[:2]+f"{experiment_turn:02d}"+"0000"

print(f"Final experiment id: {config.experiment_id}")'''
from chart_manager import translate_title
#chart_1gen1sol1size1info_runs(load_run_id(maze_id="M6200045", solver_algorithm="DFS"),"execution_time")
chart_1gen1sol1size1info_maze(load_run_id(is_outlier="S", maze_category=1, maze_size=3, solver_algorithm="DFS"), "execution_time",lst=translate_title("box", size=3, gen=1, sol="DFS", info="execution_time"))
#chart_1gen1sol1size1info_optim_pie(load_run_id(is_outlier="S", maze_category=5, solver_algorithm="DFS"))
#run_id,experiment_id,maze_id,solver_algorithm,is_solved,execution_time,vertices_explored,movement_steps,is_optimal,memory_peak,maze_category,maze_size,is_outlier
config.connection.close()
"""

"""from representation.maze_representation import drawGrid, drawAuxiliaryLines, drawGraph, draw_exit
from representation.graph_representation import *
from data_manager import load_maze
import pygame
import config

maze=load_maze("M1100006")[0]

#print(maze)
gridNumber=len(maze)
gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores



pygame.init()
screen = pygame.display.set_mode((config.windows_size,config.windows_size))
pygame.display.set_caption(config.windowsCaptionText)
running = True
clock = pygame.time.Clock()


screen.fill(config.Color.background) #posar color de fons
if 0:
    maze_to_tree_graph3(maze)
elif 1:
    drawGrid(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
    #draw_exit(screen,gridSize,gridNumber)
else:
    drawGraph(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
    draw_exit(screen,gridSize,gridNumber, type="graph")
pygame.image.save(screen, "i05-02-03.png")

if False:
    drawAuxiliaryLines(screen,gridSize,gridNumber,config.windows_size) #dibuixar graella de auxiliar

pygame.display.update() #actualitzar per cada frame

while running:
    #Teclats per sortir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False

pygame.quit()"""


'''from generate.recursive_backtracker import animation_recursive_backtracker
from generate.prim_algorithm import animation_prim
from generate.binary_tree import animation_binary_tree
from generate.sidewinder import animation_sidewinder
from generate.recursive_division import animation_recursive_division
from generate.wilson_algorithm import animation_wilson
from generate.braid_maze import animation_braid_maze_break_wall_method, animation_braid_maze_generate_wall_method
from generate.unsolvablem_maze import animation_unsolvablem_maze

from research.DFS import animation_DFS
from research.BFS import animation_BFS
from research.A_star import animation_A_star

from data_manager import load_maze

from representation.maze_animation import animate_maze_generation, animate_maze_research
import config
#animate_maze_generation(animation_recursive_backtracker(config.maze_size_int["large"]), 61)
animate_maze_research(animation_A_star(load_maze("M6200003")[0],config.start_pos, config.exit_pos, config.direction), 67)'''