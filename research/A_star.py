import heapq
from collections import deque
def algorithm_A_star(maze,start_pos, exit_pos, direction):
    size = len(maze)
    exit_pos_x = size + exit_pos[0]
    exit_pos_y = size + exit_pos[1]
    start_pos_x,start_pos_y= start_pos
    if start_pos_x==exit_pos_x and start_pos_y==exit_pos_y:
        return [start_pos]
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
            return list(stack)
        g+=1
        for dx,dy in direction:
            x=x0+dx
            y=y0+dy
            row=maze[y]
            casella=row[x]
            if -casella>g or casella==0:
                row[x]=-g
                counter+=1
                heapq_push(open_list,(int(abs(exit_pos_x-x)+abs(exit_pos_y-y)+g),counter,g,x,y,index))
    return[]