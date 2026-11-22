from collections import deque
def algorithm_BFS(maze,start_pos, exit_pos, direction):
    queue = [start_pos]
    parent = [-1]
    maze[start_pos[1]][start_pos[0]] = 1
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    if start_pos==(exit_pos_x,exit_pos_y):
        return queue, 0
    index = 0
    queue_len=1
    queue_append = queue.append
    parent_append = parent.append
    while index<queue_len:
        x0, y0 = queue[index]
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            if row[x]!=1:
                row[x]=1
                queue_append((x,y))
                parent_append(index)
                queue_len+=1
                if x==exit_pos_x and y==exit_pos_y:
                    stack=deque()
                    appendleft=stack.appendleft
                    i=queue_len-1
                    while i>=0:
                        appendleft(queue[i])
                        i=parent[i]
                    return list(stack), index+1
        index+=1
    return [], index


def animation_BFS(maze,start_pos, exit_pos, direction):
    import copy, config
    queue = [start_pos]
    parent = [-1]
    maze[start_pos[1]][start_pos[0]] = 2
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    if start_pos==(exit_pos_x,exit_pos_y):
        return
    index = 0
    queue_len=1
    queue_append = queue.append
    parent_append = parent.append
    while index<queue_len:
        x0, y0 = queue[index]
        new_maze=copy.deepcopy(maze)
        queue_copy=queue.copy()
        if len(queue_copy) > config.debug_stack_max_value+1:
            queue_display = ["..."] + queue_copy[-config.debug_stack_max_value:]
        else:
            queue_display = queue_copy
        parent_copy=parent.copy()
        if len(parent_copy) > config.debug_stack_max_value+1:
            parent_display = ["..."] + parent_copy[-config.debug_stack_max_value:]
        else:
            parent_display = parent_copy
        debug_info = [
            ("Posició actual", str((x0,y0))),
            ("Nodes explorats", str(index+1)),
            ("Estat", "Cercant"),
            ("Cua", queue_display),
            ("Índex de casella pare", parent_display),
            ("Índex actual", index),
            ("Camí", "---")
            ]
        for x1,y1 in queue[index::]:
            new_maze[y1][x1]=3
        new_maze[y0][x0]=5
        yield new_maze, debug_info
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            if row[x]!=1 and row[x]!=2:
                row[x]=2
                queue_append((x,y))
                parent_append(index)
                queue_len+=1
                if x==exit_pos_x and y==exit_pos_y:
                    stack=deque()
                    appendleft=stack.appendleft
                    i=queue_len-1
                    while i>=0:
                        appendleft(queue[i])
                        x1,y1 = queue[i]
                        new_maze[y1][x1]=4
                        stack_copy=list(stack)
                        if len(stack_copy) > config.debug_stack_max_value+1:
                            stack_display = stack_copy[:config.debug_stack_max_value] +["..."]
                        else:
                            stack_display = stack_copy
                        debug_info = [
                            ("Posició actual", str((x1,y1))),
                            ("Nodes explorats", str(index+1)),
                            ("Estat", "Reconstruint el camí"),
                            ("Cua", queue_display),
                            ("Índex de casella pare", parent_display),
                            ("Índex actual", i),
                            ("Camí", stack_display)
                            ]
                        yield new_maze, debug_info
                        i=parent[i]
                    debug_info = [
                        ("Posició actual", "---"),
                        ("Nodes explorats", str(index+1)),
                        ("Estat", "Finalitzat"),
                        ("Cua", queue_display),
                        ("Índex de casella pare", parent_display),
                        ("Índex actual", "---"),
                        ("Camí", stack_display)
                        ]
                    yield new_maze, debug_info
                    return
        index+=1
    debug_info = [
        ("Posició actual", "---"),
        ("Nodes explorats", str(index+1)),
        ("Estat", "Sense solució"),
        ("Cua", queue_display),
        ("Índex de casella pare", parent_display),
        ("Índex actual", index),
        ("Camí", "---")
        ]
    yield new_maze, debug_info
    return
