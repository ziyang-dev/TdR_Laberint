import random
from generate.maze_generate import *

#crear una lista amb 2 direcció que són les de biaix direacional (nord-oest)
dirList=[(0,-1),(-1,0)] 

def algorithm_binary_tree(size):
    maze=generate_empty_cell_maze(size)  #generar un laberint cel·la vacis
    for y in range(size):  #per cada casella
        for x in range(size):
            random.shuffle(dirList) #reordenar la lista de direcció aleatoriament
            for dir in dirList:  #anar provant de la lista de driecció si son posibles les direccións
                d1,d2=dir
                if x+d1>=size or x+d1<0 or y+d2>=size or y+d2<0:  #evitar que vagi fora del laberint
                    pass
                else:
                    pos=x,y
                    change_wall(maze, pos, dir, 0)
                    break

    maze=cell_to_grid(maze) #pasar de cel·la a graella
    return maze 

def animation_binary_tree(size):
    maze=generate_empty_cell_maze(size)  #generar un laberint cel·la vacis
    new_maze=cell_to_grid(maze) #pasar de cel·la a graella
    yield new_maze
    for y in range(size):  #per cada casella
        for x in range(size):
            new_maze=cell_to_grid(maze) #pasar de cel·la a graella
            new_maze[y*2+1][x*2+1]=2
            yield new_maze
            random.shuffle(dirList) #reordenar la lista de direcció aleatoriament
            for dir in dirList:  #anar provant de la lista de driecció si son posibles les direccións
                d1,d2=dir
                if x+d1>=size or x+d1<0 or y+d2>=size or y+d2<0:  #evitar que vagi fora del laberint
                    pass
                else:
                    pos=x,y
                    change_wall(maze, pos, dir, 0)
                    break
    new_maze=cell_to_grid(maze) #pasar de cel·la a graella
    yield new_maze
