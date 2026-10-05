#region imports
import config
import copy
import numpy as np
import psutil
import time

from representation.maze_animation import animate_maze_generation
from representation.graph_representation import maze_to_tree_graph1, maze_to_tree_graph2


from generate.recursive_backtracker import algorithm_recursive_backtracker, animation_recursive_backtracker
from generate.prim_algorithm import algorithm_prim, animation_prim
from generate.binary_tree import algorithm_binary_tree, animation_binary_tree
from generate.sidewinder import algorithm_sidewinder, animation_sidewinder
from generate.recursive_division import algorithm_recursive_division, animation_recursive_division
from generate.wilson_algorithm import algorithm_wilson, animation_wilson

from generate.braid_maze import braid_maze_break_wall_method, braid_maze_generate_wall_method, animation_braid_maze_break_wall_method, animation_braid_maze_generate_wall_method
from generate.unsolvablem_maze import unsolvablem_maze, animation_unsolvablem_maze

from research.DFS import algorithm_DFS
from research.BFS import algorithm_BFS
from research.A_star import algorithm_A_star 

from data_manager import save_maze, load_maze, print_maze_info, load_run_id, print_run_info, save_run_info

from data_collector import collect_data, repeat_collection

from runs_info_safety import verify_runs_safety

#endregion

'''p=psutil.Process()

try:
    p.cpu_affinity([2])
    print(f"Connect Python whit {p.cpu_affinity()} cpu affinity")
except:
    raise Exception ("Can not conect de cpu affinity")'''



'''id_list=[]
star_id=1
end_id=10
for gen in [1]:
    for size in [1,2,3,4,5]:
        for id in range(star_id,end_id+1):
            id_list.append(f"M{gen}{size}{id:05d}")
del star_id,end_id,gen,size,id
'''

'''for maze_id in id_list:
    maze =algorithm_recursive_backtracker(config.maze_size_int[config.maze_size[str(maze_id[2])]])
    save_maze(maze,maze_id)'''
#maze_id="M1300001"
#maze, optimal_path_lenght = load_maze(maze_id)

gen=animation_unsolvablem_maze(config.maze_size_int["extra_small"])
animate_maze_generation(gen)

#add_list_to_maze(maze, path, 3)

'''repeat_collection(id_list,"DFS",5)
repeat_collection(id_list,"BFS",5)
repeat_collection(id_list,"A_star",5)'''

#collect_data(maze_id, "BFS")

#print_run_info(load_run_id(maze_id="M1100057"))
'''i=0
for _ in verify_runs_safety(auto_generate_maze=True):
    i+=1
    if i >=500:
        raise Exception ("Repeat 500 times verity_runs_safety")
    time.sleep(3)
    if i%10==0:
        time.sleep(10)'''

#print(load_run_id(maze_id="M1100083"))
