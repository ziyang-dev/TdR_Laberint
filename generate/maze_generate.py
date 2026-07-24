#definir classe cel·la o habitació
class cell:
    def __init__(self, initial_wall_state):
        #guardar les propietats de les quatres parets, per defecte tots parets
        self.up=initial_wall_state
        self.down=initial_wall_state
        self.left=initial_wall_state
        self.right=initial_wall_state
        #guardar com a variable si aquest cell és visitat (recursive_backtracker)
        self.visited=False

def change_wall(maze, pos, dir,type):  #donat una posició de una cel·la canvia al tipos type la paret a la direcció dir
    x,y=pos
    cell1,cell2=maze[y][x], maze[y+dir[1]][x+dir[0]]
    if dir==(0,-1):
        cell1.up=type
        cell2.down=type
    elif dir==(0,1):
        cell1.down=type
        cell2.up=type
    elif dir==(-1,0):
        cell1.left=type
        cell2.right=type
    elif dir==(1,0):
        cell1.right=type
        cell2.left=type
    else:
        raise Exception("change_wall, direction incorrect") #encara que semble un estupidex, m'ha estalvitat molt temps en debuging
    return maze

def generate_empty_cell_maze(size, initial_wall_state=1): #crear una llista de cel·la   guarda el valor de la part creada per defecte tancada
    cell_maze=[]
    for _ in range(size):
        cell_list=[]
        for _ in range(size):
            cell_list.append(cell(initial_wall_state)) #crear una cel·la per defecte
        cell_maze.append(cell_list)
    return cell_maze

def cell_to_grid(cell_maze):
    grid_maze=[]
    size=len(cell_maze)*2+1  #el tamany de la graella és el soble més 1 del tamnay de la cel·la
    for _ in range(size):  #crear una llista de caselles per defecte amb valor -1
        grid_list=[]
        for _ in range(size):
            grid_list.append(-1)
        grid_maze.append(grid_list)
    for y in range(len(cell_maze)):  #pasar de cel·la a graella
        for x in range(len(cell_maze)):
            cell=cell_maze[y][x]
            grid_x,grid_y=x*2+1,y*2+1 #renovar les lesposicións a posiciones reals de la graella
            grid_maze[grid_y][grid_x]=0  #posar camí a la casella central de la cel·la
            #posar les caselles del costat les propietats de les parets de les cel·les
            grid_maze[grid_y-1][grid_x]=cell.up
            grid_maze[grid_y+1][grid_x]=cell.down
            grid_maze[grid_y][grid_x-1]=cell.left
            grid_maze[grid_y][grid_x+1]=cell.right
    return grid_maze