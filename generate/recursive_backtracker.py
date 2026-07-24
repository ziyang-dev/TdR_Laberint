import random
from generate.maze_generate import *

dirList=[(1,0),(-1,0),(0,1),(0,-1)]  #crear una lista amb 4 direcció

def algorithm_recursive_backtracker(size):
    maze=generate_empty_cell_maze(size)  #generar un laberint cel·la vacis
    #buscar una cel·la a l'azar per comenzar, guardar la posició i visitarla
    pos=(random.randint(0,size-1),random.randint(0,size-1))
    maze[pos[1]][pos[0]].visited=True
    pos_list=[pos]  #crear una lista per guardar el stack
    pos_init=pos
    while pos_list!=[]:  #repetir fins que no quedi cap casellela sense visitar
        random.shuffle(dirList) #reordenar la lista de direcció aleatoriament
        for dir in dirList:  #anar provant de la lista de driecció si son posibles les direccións
            x,y=pos
            d1,d2=dir
            if x+d1>=size or x+d1<0 or y+d2>=size or y+d2<0:  #evitar que vagi fora del laberint
                pass
            elif not maze[y+d2][x+d1].visited:  #si la cel·la no està visitada, visitala i tranca la paret entre mig
                maze=change_wall(maze, pos, dir, 0)
                pos=(x+d1,y+d2)
                pos_list.append(pos)
                maze[pos[1]][pos[0]].visited=True  #asistir que la cel·la està visitada
                break
        else:  #en cas no ha trobat cap direeció posible, retorna a la posició anterior.
            pos_list.pop()
            if pos_list!=[]:
                pos=pos_list[-1]

    maze=cell_to_grid(maze) #pasar de cel·la a graella
    maze[pos_init[1]*2+1][pos_init[0]*2+1]=2 #marcar el punt d'origen (no serveix per a res...)
    return maze