import time
import config
import copy
import tracemalloc

from research.DFS import algorithm_DFS
from research.BFS import algorithm_BFS
from research.A_star import algorithm_A_star 

from data_manager import load_maze, maze_id_manager, save_run_info

def collect_data(maze_id, search):
    maze, optimal_path_lenght= load_maze(maze_id)
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
    time.sleep(0.01)  #time for cool-down
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
                raise Exception("search_algorithm not found")

    is_solved="1" if path!=[] else "0"
    path_length = "---" if path==[] else len(path)-1
    is_optimal = "1" if optimal_path_lenght == len(path)-1 else "0"
    memory_peak = peak / (1024 * 1024)  #in MB
    save_run_info(config.exprtiment_id, maze_id, search, is_solved, execution_time, len_explored_node,
                  path_length, is_optimal, memory_peak)
    

def repeat_collection(id_list, search, times=1):  #els id tenen que ser del mateix category i size (encluint stard and end id)
    for _ in times:
        for maze_id in id_list:
            if search=="all":
                collect_data(maze_id,"DFS")
                collect_data(maze_id,"BFS")
                collect_data(maze_id,"A_star")
            else:
                collect_data(maze_id,search)