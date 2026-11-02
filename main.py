import numpy as np
import psutil
import config

from data_collector import collect_data, repeat_collection
from chart_manager import chart_1gen3sol1size1info_box, chart_1gen1sol1size1info_runs, chart_1gen3sol5size1info, chart_1gen1sol1size1info_optim_pie

from runs_info_safety import verify_runs_safety, delete_Uinfo

from data_manager import creatDB, convert_to_txt, load_run_id, load_determined_run_info
creatDB()
'''
p=psutil.Process()

try:
    p.cpu_affinity([2])
    print(f"Connect Python whit {p.cpu_affinity()} cpu affinity")
except:
    raise Exception ("Can not conect de cpu affinity")



id_list=[]
star_id=1
end_id=100
for gen in [1,2,3,4,5,6,7,8,9]:
    for size in [1]:
        for id in range(star_id,end_id+1):
            id_list.append(f"M{gen}{size}{id:05d}")
del star_id,end_id,size,id, gen


#repeat_collection(id_list,"all",5)

print("collection done")

i=1
config.exprtiment_id=config.exprtiment_id[:4]+f"{i:04d}"

for _ in verify_runs_safety(auto_generate_maze=True):
    print(i)
    if i >=100:
        break
    i+=1
    config.exprtiment_id=config.exprtiment_id[:4]+f"{i:04d}"

print(delete_Uinfo())'''


#chart_1gen1sol1size1info_runs(load_run_id(maze_id="M6200045", solver_algorithm="DFS"),"execution_time")
#chart_1gen3sol5size1info(load_run_id(is_outlier="S"),"vertices_explored")
chart_1gen1sol1size1info_optim_pie(load_run_id(is_outlier="S", maze_category=5, solver_algorithm="DFS"))
#run_id,experiment_id,maze_id,solver_algorithm,is_solved,execution_time,vertices_explored,movement_steps,is_optimal,memory_peak,maze_category,maze_size,is_outlier
config.connection.close()