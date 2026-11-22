def algorithm_DFS(maze,start_pos, exit_pos, direction):
    stack = [start_pos]
    maze[start_pos[1]][start_pos[0]] = -1
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    if start_pos==(exit_pos_x,exit_pos_y):
        return stack, maze
    append = stack.append
    pop = stack.pop
    while stack:
        x0, y0 = stack[-1]
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            if row[x]==0:
                row[x]=-1
                append((x,y))
                if x==exit_pos_x and y==exit_pos_y:
                    return stack, maze
                break
        else:
            pop()
    return stack, maze



def animation_DFS(maze,start_pos, exit_pos, direction):
    import copy, config
    stack = [start_pos]
    maze[start_pos[1]][start_pos[0]] = 2
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    if start_pos==(exit_pos_x,exit_pos_y):
        return
    append = stack.append
    pop = stack.pop
    explored_cell=1
    status="Cercant"
    while stack:
        x0, y0 = stack[-1]
        stack_copy=stack.copy()
        if len(stack_copy) > config.debug_stack_max_value+1:
            stack_display = ["..."] + stack_copy[-config.debug_stack_max_value:]
        else:
            stack_display = stack_copy
        debug_info = [
            ("Posició actual", str((x0,y0))),
            ("Nodes explorats", str(explored_cell)),
            ("Estat", status),
            ("Pila", stack_display)
            ]
        new_maze=copy.deepcopy(maze)
        for x1,y1 in stack:
            new_maze[y1][x1]=3
        new_maze[y0][x0]=5
        yield new_maze, debug_info
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            if row[x]==0:
                row[x]=2
                append((x,y))
                explored_cell+=1
                status="Cercant"
                if x == exit_pos_x and y == exit_pos_y:
                    final_maze = copy.deepcopy(maze)
                    for x1, y1 in stack:
                        final_maze[y1][x1] = 4
                    stack_copy=stack.copy()
                    if len(stack_copy) > config.debug_stack_max_value+1:
                        stack_display = ["..."] + stack_copy[-config.debug_stack_max_value:]
                    else:
                        stack_display = stack_copy
                    debug_info = [
                        ("Posició actual", "---"),
                        ("Nodes explorats", str(explored_cell)),
                        ("Estat", "Finalitzat"),
                        ("Pila", stack_display)
                        ]
                    yield final_maze, debug_info
                    return
                break
        else:
            pop()
            status="Retrocedint"
    new_maze = copy.deepcopy(maze)
    debug_info = [
        ("Posició actual", "---"),
        ("Nodes explorats", str(explored_cell)),
        ("Estat", "Sense solució"),
        ("Pila", stack)
        ]
    yield new_maze, debug_info
    return