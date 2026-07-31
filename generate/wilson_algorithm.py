import random
from generate.maze_generate import *

dirList=[(1,0),(-1,0),(0,1),(0,-1)]  #crear una lista amb 4 direcció


def algorithm_wilson(size):
    maze=generate_empty_cell_maze(size)  #generar un laberint cel·la vacis
    #buscar una cel·la a l'azar per comenzar, guardar la posició i visitarla
    unvisited_list=[]
    for y in range(size):
        for x in range(size):
            unvisited_list.append((x,y))
    pos=(random.choice(unvisited_list)) #init pos finalized
    initPos=pos
    maze[pos[1]][pos[0]].visited=True
    unvisited_list.remove(pos)
    pos_list_walk=[]  #crear una lista per guardar el stack
    while unvisited_list:  #repetir fins que no quedi cap casellela sense visitar
        if not pos_list_walk:
            pos=random.choice(unvisited_list)
            pos_list_walk.append(pos)
            continue  #este continue solo sirve para mellorar la animació, no serveix per res més
        dir=random.choice(dirList)
        if pos[0]+dir[0] < 0 or pos[0]+dir[0] >= size or pos[1]+dir[1] < 0 or pos[1]+dir[1] >= size:  #evitar que vagi fora del laberint
            continue
        pos=(pos[0]+dir[0],pos[1]+dir[1])

        if pos in pos_list_walk:
            last_index = len(pos_list_walk) - 1 - pos_list_walk[::-1].index(pos) #Encuentra el índice del último pos (buscando de derecha a izquierda)
            pos_list_walk = pos_list_walk[:last_index]  # Corta la lista hasta antes de ese índice
        
        pos_list_walk.append(pos)

        if maze[pos[1]][pos[0]].visited==True:  #si trova una cel·la visitada
            for pos1, pos2 in zip(pos_list_walk, pos_list_walk[1:]):
                n_dir=(pos2[0]-pos1[0],pos2[1]-pos1[1])
                maze=change_wall(maze,pos1,n_dir,0)
                maze[pos1[1]][pos1[0]].visited=True
                unvisited_list.remove(pos1)
            pos_list_walk.clear()
            

    maze=cell_to_grid(maze) #pasar de cel·la a graella
    return maze