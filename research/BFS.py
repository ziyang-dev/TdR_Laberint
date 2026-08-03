from collections import deque
def algorithm_BFS(maze,start_pos, exit_pos, direction):
    queue = [start_pos]
    parent = [-1]
    maze[start_pos[1]][start_pos[0]] = 1
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    if start_pos==(exit_pos_x,exit_pos_y):
        return queue
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
                    index=queue_len-1
                    while index>=0:
                        appendleft(queue[index])
                        index=parent[index]
                    return list(stack)
        index+=1
    return []