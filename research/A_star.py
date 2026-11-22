import heapq
from collections import deque
def algorithm_A_star(maze,start_pos, exit_pos, direction):
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    start_pos_x,start_pos_y= start_pos
    if start_pos_x==exit_pos_x and start_pos_y==exit_pos_y:
        return [start_pos], []
    open_list=[(abs(exit_pos_x-start_pos_x)+abs(exit_pos_y-start_pos_y), 0, 0, start_pos_x, start_pos_y,-1)]
    closed_list=[]
    parent=[]
    heapq_push = heapq.heappush
    heapq_pop = heapq.heappop
    closed_list_append=closed_list.append
    parent_append=parent.append
    counter=0
    while open_list:
        f, _, g, x0, y0, index = heapq_pop(open_list)
        row=maze[y0]
        if row[x0]==1:
            continue
        row[x0]=1
        closed_list_append((x0,y0))
        parent_append(index)
        index=len(closed_list) - 1
        if x0 == exit_pos_x and y0 == exit_pos_y:
            stack=deque()
            appendleft=stack.appendleft
            while index>=0:
                appendleft(closed_list[index])
                index=parent[index]
            return list(stack), closed_list
        g+=1
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            casella=row[x]
            if -casella>g or casella==0:
                row[x]=-g
                counter+=1
                heapq_push(open_list,(abs(exit_pos_x-x)+abs(exit_pos_y-y)+g,counter,g,x,y,index))
    return[], closed_list


def animation_A_star(maze,start_pos, exit_pos, direction):
    import copy, config
    new_maze=copy.deepcopy(maze)
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    start_pos_x,start_pos_y= start_pos
    if start_pos_x==exit_pos_x and start_pos_y==exit_pos_y:
        return
    open_list=[(abs(exit_pos_x-start_pos_x)+abs(exit_pos_y-start_pos_y), 0, 0, start_pos_x, start_pos_y,-1)]
    closed_list=[]
    parent=[]
    heapq_push = heapq.heappush
    heapq_pop = heapq.heappop
    closed_list_append=closed_list.append
    parent_append=parent.append
    counter=0
    while open_list:
        f, _, g, x0, y0, index = heapq_pop(open_list)
        olist_copy=copy.deepcopy(open_list)
        if len(olist_copy) > config.debug_stack_max_value+1:
            olist_display = []
            for f_c, _, g_c, x0_c, y0_c, index_c in olist_copy[:config.debug_stack_max_value]:
                olist_display.append(f"[{f_c}, {g_c}, ({x0_c},{y0_c}), {index_c}]")
            olist_display = olist_display + ["..."]
        else:
            olist_display = []
            for f_c, _, g_c, x0_c, y0_c, index_c in olist_copy:
                olist_display.append(f"[{f_c}, {g_c}, ({x0_c},{y0_c}), {index_c}]")
        clist_copy=closed_list.copy()
        if len(clist_copy) > config.debug_stack_max_value+1:
            clist_display = ["..."] + clist_copy[-config.debug_stack_max_value:]
        else:
            clist_display = clist_copy
        parent_copy=parent.copy()
        if len(parent_copy) > config.debug_stack_max_value+1:
            parent_display = ["..."] + parent_copy[-config.debug_stack_max_value:]
        else:
            parent_display = parent_copy
        debug_info = [
            ("Posició actual", str((x0,y0))),
            ("Costos de la posició actual", f" g: {g}, h: {f-g}, f: {f}"),
            ("Nodes explorats", str(len(closed_list))),
            ("Estat", "Cercant"),
            ("Open List [f, g, (pos), índex pare]", olist_display),
            ("Closed List", clist_display),
            ("Índex de casella pare", parent_display),
            ("Camí", "---")
            ]
        new_maze[y0][x0]=5
        yield new_maze, debug_info
        row=maze[y0]
        if row[x0]==1:
            new_maze[y0][x0]=2
            continue
        row[x0]=1
        closed_list_append((x0,y0))
        new_maze[y0][x0]=2
        parent_append(index)
        index=len(closed_list) - 1
        if x0 == exit_pos_x and y0 == exit_pos_y:
            stack=deque()
            appendleft=stack.appendleft
            while index>=0:
                x1,y1=closed_list[index]
                appendleft((x1,y1))
                index=parent[index]
                new_maze[y1][x1]=4
                stack_copy=list(stack)
                if len(stack_copy) > config.debug_stack_max_value+1:
                    stack_display = stack_copy[:config.debug_stack_max_value] +["..."]
                else:
                    stack_display = stack_copy
                debug_info = [
                    ("Posició actual", str((x1,y1))),
                    ("Costos de la posició actual", "---"),
                    ("Nodes explorats", str(len(closed_list))),
                    ("Estat", "Reconstruint el camí"),
                    ("Closed List", clist_display),
                    ("Índex de casella pare", parent_display),
                    ("Camí", stack_display)
                    ]
                yield new_maze, debug_info
            debug_info = [
                ("Posició actual", "---"),
                ("Costos de la posició actual", "---"),
                ("Nodes explorats", str(len(closed_list))),
                ("Estat", "Finalitzat"),
                ("Closed List", clist_display),
                ("Índex de casella pare", parent_display),
                ("Camí", stack_display)
                ]
            yield new_maze, debug_info
            return
        g+=1
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            casella=row[x]
            if -casella>g or casella==0:
                row[x]=-g
                counter+=1
                heapq_push(open_list,(abs(exit_pos_x-x)+abs(exit_pos_y-y)+g,counter,g,x,y,index))
                new_maze[y][x]=3
    debug_info = [
        ("Posició actual", "---"),
        ("Costos de la posició actual", "---"),
        ("Nodes explorats", str(len(closed_list))),
        ("Estat", "Sense solució"),
        ("Open List [f, g, (pos), índex pare]", olist_display),
        ("Closed List", clist_display),
        ("Índex de casella pare", parent_display),
        ("Camí", "---")
        ]
    yield new_maze, debug_info
    return