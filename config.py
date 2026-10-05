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
    "maze_size": "ERROR"
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

exprtiment_id="E000"

    #path

DATA_DIR = Path("data_store")

MAZE_DIR = Path("maze")
RUN_DIR = Path("run")

runs_path="data_store/run/runs.csv"
error_info_runs_path="data_store/run/error_info_runs_path.txt"

#main
windowsCaptionText="Debug"  #Nom de finestres
windows_size=600 # tamany de la pantalla, quadrat

with_auxiliary_line=True

animation_type="click"  #["off","click","auto"]

ticks=30
