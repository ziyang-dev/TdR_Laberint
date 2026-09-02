from pathlib import Path
class Color:
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


class Maze_size:
    small=              5
    medium=             25
    large=              50
    extra_large=        500

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
    "9": ["unsolvable",False]
}

maze_size={
    "1": "small",
    "2": "medium",
    "3": "large",
    "4": "extra_large"
}

exprtiment_id="E000"

DATA_DIR = Path("data_store")

MAZE_DIR = Path("maze")
RUN_DIR = Path("run")

runs_path="data_store/run/runs.csv"


#main
windowsCaptionText="Debug"  #Nom de finestres
windows_size=600 # tamany de la pantalla, quadrat

with_auxiliary_line=True

animation_type="off"  #["off","click","auto"]

ticks=30
