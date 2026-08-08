import copy
import random
import config
from generate.wilson_algorithm import algorithm_wilson
from research.A_star import algorithm_A_star

def unsolvablem_maze(size):
    maze=algorithm_wilson(size)
    path=algorithm_A_star(copy.deepcopy(maze),config.start_pos,config.exit_pos,config.direction)
    x,y=1,1
    while x%2!=0 and y%2!=0:
        x,y=random.choice(path)
        print(1)
    maze[y][x]=-1
    return maze