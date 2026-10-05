import random
from generate.maze_generate import *

def generate_wall(maze, x, y, len, dir):  #generar un mur amb un furat en de la posició x,y a direccio dir de tamany len
    if dir=="v":
        safe_number=random.randint(y,y+len-1)
        for y in range(y,y+len):
            if y==safe_number:
                continue
            change_wall(maze,(x,y), (1,0),1)
        pos=(x,safe_number)
    else:
        safe_number=random.randint(x,x+len-1)
        for x in range(x,x+len):
            if x==safe_number:
                continue
            change_wall(maze,(x,y), (0,1),1)
        pos=(safe_number,y)
    return pos
        

def algorithm_recursive_division(size):
    maze=generate_empty_cell_maze(size,0)  #generar un laberint cel·la vacis
    generate_maze_border(maze)
    region_list=[]  #llista amb llistes de [x,y,dis_x,dis_y,dir]
    region_list.append([0,0,size-1,size-1,random.choice(["v","h"])])  # aquí la dis_x y dis_y no són els nombres de caselles sinó el màxim de murs
    while region_list:
        x,y,dis_x,dis_y,dir=region_list[-1]
        region_list.pop()
        if dis_x==0 or dis_y==0:  #si només quda una casella continnua el while
            continue
        if dis_x>dis_y:  #canvair direcció anterior a un direcció nou
            dir="v"
        elif dis_x<dis_y:
            dir="h"
        else:
            dir="h" if dir=="v" else "v"
        if dir=="v":
            n=random.randint(1,dis_x)
            #n=dis_x//2+1
            generate_wall(maze,x+n-1,y,dis_y+1,dir)
            region_list.append([x,y,n-1,dis_y,dir])
            region_list.append([x+n,y,dis_x-n,dis_y,dir])
        else:
            n=random.randint(1,dis_y)
            #n=dis_y//2+1
            generate_wall(maze,x,y+n-1,dis_x+1,dir)
            region_list.append([x,y,dis_x,n-1,dir])
            region_list.append([x,y+n,dis_x,dis_y-n,dir])

    maze=cell_to_grid(maze) #pasar de cel·la a graella
    return maze

def animation_recursive_division(size):
    maze=generate_empty_cell_maze(size,0)  #generar un laberint cel·la vacis
    generate_maze_border(maze)
    region_list=[]  #llista amb llistes de [x,y,dis_x,dis_y,dir]
    region_list.append([0,0,size-1,size-1,random.choice(["v","h"])])  # aquí la dis_x y dis_y no són els nombres de caselles sinó el màxim de murs
    new_maze=cell_to_grid(maze) #pasar de cel·la a graella
    yield new_maze
    while region_list:
        x,y,dis_x,dis_y,dir=region_list[-1]
        region_list.pop()
        if dis_x==0 or dis_y==0:  #si només quda una casella continnua el while
            continue
        if dis_x>dis_y:  #canvair direcció anterior a un direcció nou
            dir="v"
        elif dis_x<dis_y:
            dir="h"
        else:
            dir="h" if dir=="v" else "v"
        if dir=="v":
            n=random.randint(1,dis_x)
            #n=dis_x//2+1
            pos=generate_wall(maze,x+n-1,y,dis_y+1,dir)
            pos_list=[(x+n-1,ny) for ny in range(y,y+dis_y+1)] 
            region_list.append([x,y,n-1,dis_y,dir])
            region_list.append([x+n,y,dis_x-n,dis_y,dir])

            new_maze=cell_to_grid(maze) #pasar de cel·la a graella
            if pos_list!=[]:
                new_maze[pos_list[0][1]*2+1][pos_list[0][0]*2+2]=2
            for i in range(1,len(pos_list)):
                dy,dx=(pos_list[i-1][1]-pos_list[i][1]),(pos_list[i-1][0]-pos_list[i][0])
                new_maze[pos_list[i][1]*2+1+dy][pos_list[i][0]*2+2+dx]=2
                new_maze[pos_list[i][1]*2+1][pos_list[i][0]*2+2]=2
            new_maze[pos[1]*2+1][pos[0]*2+2]=0
            yield new_maze
        else:
            n=random.randint(1,dis_y)
            #n=dis_y//2+1
            pos=generate_wall(maze,x,y+n-1,dis_x+1,dir)
            pos_list=[(nx,y+n-1) for nx in range(x,x+dis_x+1)] 
            region_list.append([x,y,dis_x,n-1,dir])
            region_list.append([x,y+n,dis_x,dis_y-n,dir])

            new_maze=cell_to_grid(maze) #pasar de cel·la a graella
            if pos_list!=[]:
                new_maze[pos_list[0][1]*2+2][pos_list[0][0]*2+1]=2
            for i in range(1,len(pos_list)):
                dy,dx=(pos_list[i-1][1]-pos_list[i][1]),(pos_list[i-1][0]-pos_list[i][0])
                new_maze[pos_list[i][1]*2+2+dy][pos_list[i][0]*2+1+dx]=2
                new_maze[pos_list[i][1]*2+2][pos_list[i][0]*2+1]=2
            new_maze[pos[1]*2+2][pos[0]*2+1]=0
            yield new_maze
    new_maze=cell_to_grid(maze) #pasar de cel·la a graella
    yield new_maze