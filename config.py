from pathlib import Path
class Color:  #color of maze
    background=         (245, 247, 250)     #black
    wall=               (24, 28, 36)        #white
    line=               (50, 220, 120)      #fluorescent green
    error=              (255, 0, 0)         #fluorescent red
    exit=               (255, 160, 170)     #light red
    star=               (140, 210, 255)     #light gleu


    gren=               (180, 245, 205)     #light green
    yellow=             (255, 230, 150)     #light yellow
    blue=               (40, 60, 95)        #deep blue
    purple=             (185, 130, 255)     #purple


maze_size_int={
    "extra_small":        5,
    "small":              10,
    "medium":             20,
    "large":              40,
    "extra_large":        80,
    "especial_large":     500
}

#research
direction=((1,0), (0,1), (-1,0), (0,-1))
start_pos=(1,1)
exit_pos=(-2,-2)

#data_manager
maze_category={
    "1": ["perfect","recursive_backtracker"],
    "2": ["perfect","prim_algorithm"],
    "3": ["perfect","binary_tree"],
    "4": ["perfect","sidewinder"],
    "5": ["perfect","recursive_division"],
    "6": ["perfect","wilson_algoritm" ],
    "7": ["braid","break_wall_method"],
    "8": ["braid","generate_wall_method"],
    "9": [False,"unsolvable"]
}

maze_size={
    "1": "extra_small",
    "2": "small",
    "3": "medium",
    "4": "large",
    "5": "extra_large",
    "6": "especial_large"
}


runs_label={
    "run_id": "ID de l'execució",
    "experiment_id": "ID de l'experiment",
    "maze_id": "ID del laberint",
    "solver_algorithm": "Algorisme de cerca",
    "is_solved": "És resolt?",
    "execution_time": "Temps d'execució",
    "vertices_explored": "Caselles explorades",
    "movement_steps": "Nombre de moviments",
    "is_optimal": "És òptim?",
    "memory_peak": "Pic de memòria",
    "maze_size": "Mida d'un costat del laberint"
}

runs_unit_label={
    "run_id": None,
    "experiment_id": None,
    "maze_id": None,
    "solver_algorithm": None,
    "is_solved": "bool",
    "execution_time": "ms",
    "vertices_explored": "casella/es",
    "movement_steps": "casella/es",
    "is_optimal": "bool",
    "memory_peak": "MiB",
    "maze_size": "caselles/es"
}

generator_algorithm_label={
    "recursive_backtracker": "Recursive Backtracker",
    "prim_algorithm": "Prim's algorithm",
    "binary_tree": "Binary Tree",
    "sidewinder": "Sidewinder",
    "recursive_division": "Recursive Division",
    "wilson_algoritm": "Wilson's algorithm",
    "break_wall_method": "Braid maze per destrucció de paret",
    "generate_wall_method": "Braid maze per generació de paret",
    "unsolvable": "Usolvable maze"
}

experiment_id="E0050000"

#path

DATA_DIR = Path("data_store")

MAZE_DIR = Path("maze")
RUN_DIR = Path("run")

runs_path="data_store/run/runs.csv"
error_info_runs_path="data_store/run/error_info_runs_path.txt"
runsSQL_path="data_store/run/runs.db"
chart_info_path="data_store/chart"

#main
windowsCaptionText="Debug"  #Nom de finestres
windows_size=1080 # tamany de la pantalla, quadrat

with_auxiliary_line=False

animation_type="click"  #["off","click","auto"]

ticks=30


import sqlite3

connection=sqlite3.connect(runsSQL_path)
connection.row_factory = sqlite3.Row

save_chart_info_and_image=True


#region         char dict

dict_chart_type = {
    "run_id": "Resultats",
    "maze_id": "Resultats",
    "3_sol": "Comparació",
    "box": "Distribució", 
    "heap": "Mapa de calor",
    "bar": "Anàlisi",
    "pie": "Distribució percentual del nombre de moviments de les solucions trobades",
    "ver_time": "Relació entre el nombre de les caselles explorades",
    "5_size": "Influència de la mida del laberint en"
}

dict_chart_type_types={
    "run_id": "info",
    "maze_id": "info",
    "3_sol": "info",
    "box": "info", 
    "heap": "info",
    "bar": "info",
    "pie": "no info",
    "ver_time": "no info",
    "5_size": "en"
}


dict_chart_info_de={
    "execution_time": " del temps d'execució",
    "vertices_explored": " de les caselles explorades",
    "movement_steps": " del nombre de moviments",
    "memory_peak": " del pic de memòria",
}

dict_chart_info_en={
    "execution_time": " en el temps d'execució",
    "vertices_explored": " en les caselles explorades",
    "movement_steps": " en el nombre de moviments",
    "memory_peak": " en el pic de memòria",
}

dict_chart_gen={
    1: " generat mitjançant Recursive Backtracker",
    2: " generat mitjançant l'algorisme de Prim",
    3: " generat mitjançant Binary Tree",
    4: " generat mitjançant Sidewinder",
    5: " generat mitjançant Recursive Division",
    6: " generat mitjançant l'algorisme de Wilson" ,
    7: " sobre braid maze generat mitjançant el metode per destrucció de paret",
    8: " sobre braid maze generat mitjançant el metode per generació de paret",
    9: " generat mitjançant usolvable maze"
}

dict_chart_sol={
    "DFS": " resol amb DFS",
    "BFS": " resol amb BFS",
    "A_star": " resol amb A*"
}

dict_chart_size={
    1: f" de mida {maze_size_int["extra_small"]*2+1} * {maze_size_int["extra_small"]*2+1}",
    2: f" de mida {maze_size_int["small"]*2+1} * {maze_size_int["small"]*2+1}",
    3: f" de mida {maze_size_int["medium"]*2+1} * {maze_size_int["medium"]*2+1}",
    4: f" de mida {maze_size_int["large"]*2+1} * {maze_size_int["large"]*2+1}",
    5: f" de mida {maze_size_int["extra_large"]*2+1} * {maze_size_int["extra_large"]*2+1}",
    6: f" de mida {maze_size_int["especial_large"]*2+1} * {maze_size_int["especial_large"]*2+1}"
}

#endregion

