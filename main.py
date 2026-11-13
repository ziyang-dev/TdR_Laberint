import numpy as np
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