import time
import config
import copy
import tracemalloc

from research.DFS import algorithm_DFS
from research.BFS import algorithm_BFS
from research.A_star import algorithm_A_star 

from data_manager import load_maze, maze_id_manager, save_run_info

def collect_data(maze_id, search, optimal_path_lenght):
    _, maze_category, maze_generate_algorithm, maze_size = maze_id_manager(maze_id)
    maze= load_maze(maze_id)
    match search:
        case "DFS":
            search_algorithm=algorithm_DFS
        case "BFS":    
            search_algorithm=algorithm_BFS 
        case "A_star":
            search_algorithm=algorithm_A_star
        case _:
            raise("search_algorithm not found")
    maze_copy=copy.deepcopy(maze)
    tracemalloc.start()
    start_time=time.perf_counter()
    path, list_explored_node = search_algorithm(maze_copy,config.start_pos, config.exit_pos, config.direction)
    end_time=time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time=(end_time-start_time)*1000  #in ms

    match search:
            case "DFS":
                counter=0
                for row in list_explored_node:
                    for tile in row:
                        if tile==-1: counter+=1
                len_explored_node=counter
                del counter
            case "BFS" | "A_star":
                len_explored_node=len(list_explored_node)
            case _:
                raise("search_algorithm not found")

    is_solved="True" if path!=[] else "False"
    path_length = "---" if path==[] else len(path)-1
    is_optimal = "True" if optimal_path_lenght == len(path)-1 else "False"
    memory_peak = peak / (1024 * 1024)  #in MB
    save_run_info(config.runs_path, config.exprtiment_id, maze_id, search, is_solved, execution_time, len_explored_node,
                  path_length, is_optimal, memory_peak)
    

def repeat_collection(start_id,end_id, search):  #els id tenen que ser del mateix category i size (encluint stard and end id)
    pre_id=start_id[0:3]
    for n in range(int(start_id[-5:]),int(end_id[-5:])+1):
        maze_id=pre_id+f"{n:05d}"
        maze= load_maze(maze_id)
        maze_copy=copy.deepcopy(maze)
        path, explored_node = algorithm_BFS(maze_copy,config.start_pos, config.exit_pos, config.direction)
        if search=="all":
            collect_data(maze_id,"DFS",len(path)-1)
            collect_data(maze_id,"BFS",len(path)-1)
            collect_data(maze_id,"A_star",len(path)-1)
        else:
            collect_data(maze_id,search,len(path)-1)