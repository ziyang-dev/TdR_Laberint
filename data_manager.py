from pathlib import Path
import numpy as np
import config
import csv

from config import DATA_DIR, MAZE_DIR, RUN_DIR, runs_path

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
    np.save(path, np.array(maze, dtype=np.uint8))

def load_maze(maze_id):
    path =  information_to_folder(maze_id_manager(maze_id)) / f"{maze_id}.npy"
    maze = np.load(path).tolist()
    return maze

def print_maze_info(maze_id):
    _, maze_category, maze_generate_algorithm, maze_size = maze_id_manager(maze_id)
    print(f'''    Maze type: {maze_category}
    Generator: {maze_generate_algorithm}
    Size: {maze_size}''')

def save_run_info(path,experiment_id, maze_id, solver_algorithm, is_solved,
                  execution_time, vertices_explored, path_length, is_optimal, memory_peak):
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    run_id=int(rows[-1]["run_id"])+1
    with open(path, "a", newline="", encoding="utf-8") as file:
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
            memory_peak
            ])

def load_run_info(path,key=False,value=False):
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        row_list=[]
        if value:
            for row in reader:
                if row[key] == value:
                    row_list.append(row)
        else:
            return reader
    return row_list

def print_run_info(row_list):
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
