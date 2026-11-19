"""import numpy as np
import config

from data_collector import collect_data, repeat_collection
from chart_manager import *

from runs_info_safety import verify_runs_safety, delete_Uinfo
from generate.recursive_backtracker import algorithm_recursive_backtracker
from generate.braid_maze import braid_maze_generate_wall_method

from data_manager import creatDB, convert_to_txt, load_run_id, load_determined_run_info, save_maze
creatDB()
'''
p=psutil.Process()

try:
    p.cpu_affinity([2])
    print(f"Connect Python whit {p.cpu_affinity()} cpu affinity")
except:
    raise Exception ("Can not conect de cpu affinity")'''



id_list=[]
star_id=1
end_id=100
for gen in [8]:
    for size in [3]:
        for id in range(star_id,end_id+1):
            maze_id=f"M{gen}{size}{id:05d}"
            id_list.append(maze_id)
            save_maze(braid_maze_generate_wall_method(20),maze_id)
            print(f"saved maze: {maze_id}")

del star_id,end_id,size,id, gen, maze_id



repeat_collection(id_list,"all",5)

print("collection done")

i=1
config.exprtiment_id=config.exprtiment_id[:4]+f"{i:04d}"

for _ in verify_runs_safety(auto_generate_maze=True):
    print(i)
    if i >=100:
        break
    i+=1
    config.exprtiment_id=config.exprtiment_id[:4]+f"{i:04d}"

print(delete_Uinfo())



#chart_1gen1sol1size1info_runs(load_run_id(maze_id="M6200045", solver_algorithm="DFS"),"execution_time")
                                                                 # Generate_algorithm-relver_algorithm-size-info_type-char-tipe*id
#chart_1gen1sol1size1info_optim_pie(load_run_id(is_outlier="S"), title="RecursiveBactraker-all-3-execution_time-info_maze")
#chart_1gen1sol1size1info_optim_pie(load_run_id(is_outlier="S", maze_category=5, solver_algorithm="DFS"))
#run_id,experiment_id,maze_id,solver_algorithm,is_solved,execution_time,vertices_explored,movement_steps,is_optimal,memory_peak,maze_category,maze_size,is_outlier
config.connection.close()
"""

from representation.maze_representation import drawGrid, drawAuxiliaryLines, drawGraph
from data_manager import load_maze
import pygame
import config

maze=[
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1]
    ]

gridNumber=len(maze)
gridSize=config.windows_size//gridNumber #tamany de cada casella a un tamany enter
config.windows_size=gridSize*gridNumber #ajusta el tamany quitant les vores



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

    
    screen.fill(config.Color.background) #posar color de fons

    drawGraph(screen,maze,gridSize,gridNumber) #llamar a la funció per pintar el laberint
    #pygame.image.save(screen, "nombre_archivo.png")

    if True:
        drawAuxiliaryLines(screen,gridSize,gridNumber,config.windows_size) #dibuixar graella de auxiliar

    pygame.display.update() #actualitzar per cada frame
    clock.tick(1) #ajustar a 30 FPS
pygame.quit()
