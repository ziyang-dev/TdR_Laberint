import random
import config
import copy
from generate.maze_generate import *
from generate.recursive_backtracker import algorithm_recursive_backtracker
from research.A_star import algorithm_A_star
direction=config.direction

def braid_maze_break_wall_method(size):
    maze=algorithm_recursive_backtracker(size)
    size=size*2+1
    for y0 in range(1,size-1):
        for x0 in range(1,size-1):
            counter=0
            pos_list=[]
            for d1,d2 in direction:
                x,y=x0+d1,y0+d2
                if maze[y][x]==0:
                    counter+=1
                else:
                    pos_list.append((x,y))
                if counter==2:
                    break
            else:
                random.shuffle(pos_list)
                for x, y in pos_list:
                    if 0<x<size-1 and 0<y<size-1:
                        maze[y][x]=0
                        break
    return maze

def braid_maze_generate_wall_method(size):
    maze=generate_empty_cell_maze(size,-1)
    generate_maze_border(maze)
    maze=cell_to_grid(maze)
    size=size*2+1
    for y0 in range(2,size-2,2):
        for x0 in range(2,size-2,2):
            pos_list=[]
            for d1,d2 in direction:
                x,y=x0+d1,y0+d2
                if maze[y][x]==1:
                    break
                else:
                    pos_list.append((x,y))
            else:
                random.shuffle(pos_list)
                for pos in pos_list:
                    x,y=pos
                    is_able=True
                    for d1,d2 in ((y-y0,x-x0),(y0-y,x0-x)):
                        if not is_able:
                            break
                        new_x,new_y=x+d1,y+d2
                        counter=0
                        for new_d1,new_d2 in direction:
                            if maze[new_d2+new_y][new_d1+new_x]==1:
                                counter+=1
                                if counter==2:
                                    is_able=False
                                    break
                    if is_able:
                        maze[y][x]=1
                        break
    pos_list=[]
    for y0 in range(1,size-1):
        for x0 in range(1,size-1):
            if maze[y0][x0]==-1:
                pos_list.append((x0,y0))
    random.shuffle(pos_list)
    for pos in pos_list:
        x,y=pos
        is_able=True
        for d1,d2 in direction:
            if maze[y][x]==1:
                continue
            if not is_able:
                break
            new_x,new_y=x+d1,y+d2
            counter=0
            for new_d1,new_d2 in direction:
                try:
                    if maze[new_d2+new_y][new_d1+new_x]==1:
                        counter+=1
                        if counter==2:
                            is_able=False
                            break
                except IndexError:
                    pass
        if is_able:
            maze[y][x]=1
        else:
            maze[y][x]=0
    if not algorithm_A_star(copy.deepcopy(maze),config.start_pos,config.exit_pos,config.direction):
        return braid_maze_generate_wall_method(size//2)
    return maze