import random
from generate.maze_generate import *


def algorithm_sidewinder(size):
    maze=generate_empty_cell_maze(size)  #generar un laberint cel·la vacis
    for y in range(size):  #per cada casella
        pos_list=[]
        for x in range(size):
            
            if y==0:  #en la primera capa, sempre cap l'est
                if x<size-1:
                    change_wall(maze,(x,y), (1,0), 0)
                continue
            pos_list.append((x,y)) 
            if random.randint(1,100)<=10 or x==size-1:  #evitar que vagi fora del laberint i que sigui esgafat
                change_wall(maze, random.choice(pos_list), (0,-1), 0) #dels de la llista, agafar un in trencar una paret amun
                pos_list=[]
            else:
                change_wall(maze,(x,y), (1,0), 0)

    maze=cell_to_grid(maze) #pasar de cel·la a graella
    #maze[1][1]=2 #marcar el punt d'origen (no serveix per a res...)
    return maze 