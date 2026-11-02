from pathlib import Path
import numpy as np
import config
import copy

from config import DATA_DIR, MAZE_DIR, RUN_DIR, runs_path, connection
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

def creatDB():
    connection.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        run_id INTEGER PRIMARY KEY AUTOINCREMENT,
        experiment_id TEXT,
        maze_id TEXT,
        solver_algorithm TEXT,
        is_solved INTEGER,
        execution_time REAL,
        vertices_explored INTEGER,
        movement_steps INTEGER,
        is_optimal INTEGER,
        memory_peak REAL,
        maze_category INTEGER,
        maze_size INTEGER,
        is_outlier TEXT
        )
    """)

def save_run_info(experiment_id, maze_id, solver_algorithm, is_solved,
                  execution_time, vertices_explored, movement_steps, is_optimal, memory_peak):
    connection.execute("""
        INSERT INTO runs (
            experiment_id,
            maze_id,
            solver_algorithm,
            is_solved,
            execution_time,
            vertices_explored,
            movement_steps,
            is_optimal,
            memory_peak,
            maze_category,
            maze_size,
            is_outlier
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (experiment_id, maze_id, solver_algorithm, is_solved, execution_time, vertices_explored, movement_steps, is_optimal, memory_peak, maze_id[1], maze_id[2], "U"))
    connection.commit()

def load_run_id(**conditions):
    if not conditions:
        rows = connection.execute(
            "SELECT run_id FROM runs"
        ).fetchall()
    else:
        where_clause = " AND ".join(f'"{key}" = ?' for key in conditions)
        sql = f"SELECT run_id FROM runs WHERE {where_clause}"
        rows = connection.execute(
            sql,
            tuple(str(value) for value in conditions.values())
        ).fetchall()
    return [row["run_id"] for row in rows]

def load_determined_run_info(run_id, *info_types):
        row = connection.execute(
            f"""
            SELECT {", ".join(info_types)}
            FROM runs
            WHERE run_id = ?
            """,
            (run_id,)
        ).fetchone()

        if row is None:
            raise ValueError(f"run_id {run_id} does not exist")

        result = list(row)

        if len(result) == 1:
            return result[0]
        return result

def print_run_info(run_id_list):
    for run_id in run_id_list:
        run_id = int(run_id)

        row = connection.execute("SELECT * FROM runs WHERE run_id = ?",(run_id,)).fetchone()

        if row is None: raise Exception(f"run_id {run_id} does not exist in runs.db")

        print(f'''    Run id: {row["run_id"]}
    Experiment id: {row["experiment_id"]}
    Maze id: {row["maze_id"]}''')

        print_maze_info(row["maze_id"])

        print(f'''    Solver algorithm: {row["solver_algorithm"]}
    Is solved: {row["is_solved"]}
    Execution time: {row["execution_time"]} ms
    Vertices explored: {row["vertices_explored"]}
    Movement steps: {row["movement_steps"]}
    Is optimal: {row["is_optimal"]}
    Memory peak: {row["memory_peak"]} MB
    Is outlier: {row["is_outlier"]}

    ''')

def divide_by_category(run_id_list,category,*info_types):
    maze_dict={}
    if not run_id_list:
        return maze_dict
    columns = [category, *info_types]
    columns_sql = ", ".join(f'"{column}"' for column in columns)
    rows = []

    batch_size = 900
    for start in range(0, len(run_id_list), batch_size):
        batch = run_id_list[start:start + batch_size]
        placeholders = ", ".join("?" for _ in batch)
        sql = f"""
            SELECT run_id, {columns_sql}
            FROM runs
            WHERE run_id IN ({placeholders})
        """
        rows.extend(
            connection.execute(sql, tuple(batch)).fetchall()
        )
    
    rows_by_id = {row["run_id"]: row for row in rows}

    for run_id in run_id_list:
        row = rows_by_id.get(int(run_id))

        category_info=row[category]
        info = [row[column] for column in info_types]

        if len(info)==1:
            info=info[0]
        if isinstance(info,list):
            result = [n for n in info]
        else:
            result=info
        
        if category=="maze_category":
            category_info=config.maze_category[str(category_info)][1]
        elif category=="maze_size":
            category_info=config.maze_size[category_info]
            
        maze_dict.setdefault(category_info, []).append(result)

    return maze_dict


def convert_to_txt():
    import csv
    rows = connection.execute("SELECT * FROM runs").fetchall()

    if rows is None: raise Exception("runs.db is empty")

    with open("output_runinfo.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "run_id",
            "experiment_id",
            "maze_id",
            "solver_algorithm",
            "is_solved",
            "execution_time",
            "vertices_explored",
            "movement_steps",
            "is_optimal",
            "memory_peak",
            "maze_category",
            "maze_size",
            "is_outlier"
            ])
        for row in rows:
            writer.writerow([
                row["run_id"],
                row["experiment_id"],
                row["maze_id"],
                row["solver_algorithm"],
                row["is_solved"],
                row["execution_time"],
                row["vertices_explored"],
                row["movement_steps"],
                row["is_optimal"],
                row["memory_peak"],
                str(row["maze_id"])[1],
                str(row["maze_id"])[2],
                row["is_outlier"]
                ])
