from pathlib import Path
import numpy as np
import config
import copy
import csv

from config import DATA_DIR, MAZE_DIR, RUN_DIR, runs_path
from research.BFS import algorithm_BFS

#import sys
#sys.stdout = open("output.txt", "w", encoding="utf-8")



def information_to_folder(args):
    items = [x for x in args if x is not False]
    items.insert(0,DATA_DIR)
    return Path(*items)

def maze_id_manager(maze_id):
    if len(maze_id)!=8 or maze_id[0]!="M":
        raise ValueError ("Unknown maze_id detected")
    maze_category, maze_generate_algorithm = config.maze_category[maze_id[1]]
    maze_size = config.maze_size[maze_id[2]]
    return MAZE_DIR, maze_category, maze_generate_algorithm, maze_size

def save_maze(maze, maze_id):
    folder = information_to_folder(maze_id_manager(maze_id))
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{maze_id}.npy"
    if path.exists():
        raise FileExistsError(f"Maze ID '{maze_id}' already exists.")
    optimal_path, _=algorithm_BFS(copy.deepcopy(maze),config.start_pos,config.exit_pos,config.direction)
    optimal_path_lenght=len(optimal_path)-1
    data={"maze":np.array(maze,dtype=np.uint8),"optimal_path_lenght":optimal_path_lenght}
    np.save(path, data)

def load_maze(maze_id):
    path =  information_to_folder(maze_id_manager(maze_id)) / f"{maze_id}.npy"
    data = np.load(path, allow_pickle=True).item()
    maze = data["maze"].tolist()
    optimal_path_lenght = data["optimal_path_lenght"]
    return maze, optimal_path_lenght

def print_maze_info(maze_id):
    _, maze_category, maze_generate_algorithm, maze_size = maze_id_manager(maze_id)
    print(f'''    Maze type: {maze_category}
    Generator: {maze_generate_algorithm}
    Size: {maze_size}''')

def save_run_info(experiment_id, maze_id, solver_algorithm, is_solved,
                  execution_time, vertices_explored, path_length, is_optimal, memory_peak):
    with open(runs_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    run_id=int(rows[-1]["run_id"])+1
    with open(runs_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            run_id,
            experiment_id,
            maze_id,
            solver_algorithm,
            is_solved,
            execution_time,
            vertices_explored,
            path_length,
            is_optimal,
            memory_peak,
            "U"
            ])


def load_run_id(**conditions):
    with open(runs_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        return [
            int(row["run_id"])
            for row in reader
            if all(row[key] == str(value)
                   for key, value in conditions.items())
        ]

def load_determined_run_info(run_id, *info_types):
    with open(runs_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows=list(reader)
        if run_id!=int(rows[run_id]["run_id"]):
            print(run_id,rows[run_id]["run_id"])
            raise Exception ("run_id is not the same at runs.csv")
        result=[]
        for info_type in info_types:
            result.append(rows[run_id][info_type])
        if len(result)==1:
            result=result[0]
        return result

def print_run_info(run_id_list):
    row_list=[]
    with open(runs_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows=list(reader)
            for run_id in run_id_list:
                run_id=int(run_id)
                if run_id!=int(rows[run_id]["run_id"]):
                    print(run_id,rows[run_id]["run_id"])
                    raise Exception ("run_id is not the same at runs.csv")
                row_list.append(rows[run_id])
    for row in row_list:
        print(f'''    Run id: {row["run_id"]}
    Experiment id: {row["experiment_id"]}
    Maze id: {row["maze_id"]}''')
        print_maze_info(row["maze_id"])
        print(f'''    Solver algorithm: {row["solver_algorithm"]}
    Is solved: {row["is_solved"]}
    Execution time: {row["execution_time"]} ms
    Vertices explored: {row["vertices_explored"]}
    Path length: {row["path_length"]}
    Is optimal: {row["is_optimal"]}
    Memory peak: {row["memory_peak"]} MB
    ''')
