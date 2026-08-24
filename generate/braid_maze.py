import random
import config
import copy
from generate.maze_generate import *
from generate.wilson_algorithm import algorithm_wilson
from research.A_star import algorithm_A_star
direction=config.direction

def braid_maze_break_wall_method(size):
    maze=algorithm_wilson(size)
    size=size*2+1
    for y0 in range(1,size-1,2):
        for x0 in range(1,size-1,2):
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

def will_dead_end(maze, x, y):  # Retorna True si convertir aquesta posició en paret pot generar un dead end
    counter=0
    for d1,d2 in direction:
        try:
            if maze[d2+y][d1+x]==1:
                counter+=1
                if counter==2:
                    return True
        except IndexError:
            pass
    return False
def braid_maze_generate_wall_method(size):
    maze=generate_empty_cell_maze(size,-1)  # -1 és usat com un variable extra, en aquest cas, un tipus de camí no visidada
    generate_maze_border(maze)
    maze=cell_to_grid(maze)  #treballem en una graella decaselles
    size=size*2+1
    for y0 in range(2,size-2,2):
        for x0 in range(2,size-2,2):
            pos_list=[]
            for d1,d2 in direction:  #mira si aquesta casella esta sola 
                x,y=x0+d1,y0+d2
                if maze[y][x]==1:
                    break
                else:
                    pos_list.append((x,y))
            else:  # si és que sí, li dona una paret si és possible
                random.shuffle(pos_list)
                for pos in pos_list:
                    x,y=pos
                    if not (will_dead_end(maze,x+y-y0,y+x-x0) or will_dead_end(maze,x+y0-y,y+x0-x)):
                        maze[y][x]=1
                        break
    pos_list=[]
    for y0 in range(1,size-1):  #apunta tots les caselles que no són parets i no visitades
        for x0 in range(1,size-1):
            if maze[y0][x0]==-1:
                pos_list.append((x0,y0))
    random.shuffle(pos_list)
    for pos in pos_list:  #per cada casella amb valor -1 prova de convertirlo en paret o camí
        x,y=pos
        is_able=True
        for d1,d2 in direction:
            if not is_able:
                break
            if will_dead_end(maze,x+d1,y+d2):
                is_able=False
                break
        if is_able:
            maze[y][x]=1
        else:
            maze[y][x]=0
    if not algorithm_A_star(copy.deepcopy(maze),config.start_pos,config.exit_pos,config.direction):
        return braid_maze_generate_wall_method(size//2)
    return maze