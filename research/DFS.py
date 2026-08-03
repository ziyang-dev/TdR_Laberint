def algorithm_DFS(maze,start_pos, exit_pos, direction):
    stack = [start_pos]
    maze[start_pos[1]][start_pos[0]] = 1
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    if start_pos==(exit_pos_x,exit_pos_y):
        return stack
    append = stack.append
    pop = stack.pop
    while stack:
        x0, y0 = stack[-1]
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            if row[x]!=1:
                row[x]=1
                append((x,y))
                if x==exit_pos_x and y==exit_pos_y:
                    return stack
                break
        else:
            pop()
    return stack

    '''maze1 = [row[:] for row in maze]
        for n in stack:
            maze1[n[1]][n[0]]=3
        yield maze1'''