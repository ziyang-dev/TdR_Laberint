'''import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout


def maze_to_tree_graph(maze):  #donat una maze, es representa com un graf de arbre
    G=nx.Graph()
    size=len(maze)//2
    G.add_edge("Start",(0,0))
    G.add_edge("End",(size-1,size-1))
    for y in range(size):
        grid_y=y*2+1
        for x in range(size):
            grid_x=x*2+1
            if x!=0 and maze[grid_y][grid_x-1]==0:
                G.add_edge((x,y),(x-1,y))
            if y!=0 and maze[grid_y-1][grid_x]==0:
                            G.add_edge((x,y),(x,y-1))
    pos = graphviz_layout(G, prog="dot")
    pos = graphviz_layout(G, prog="dot", root="Start")

    nx.draw(G, pos, with_labels=True)

    print(G.number_of_nodes(), G.number_of_edges())

    plt.show(block=False)
    plt.pause(0.001)

    '''
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def maze_to_tree_graph(maze):
    G = nx.Graph()

    size = len(maze) // 2

    # 建图
    G.add_edge("Start", (0, 0))
    G.add_edge((size - 1, size - 1), "End")

    for y in range(size):
        grid_y = y * 2 + 1

        for x in range(size):
            grid_x = x * 2 + 1

            if x != 0 and maze[grid_y][grid_x - 1] == 0:
                G.add_edge((x, y), (x - 1, y))

            if y != 0 and maze[grid_y - 1][grid_x] == 0:
                G.add_edge((x, y), (x, y - 1))

    # ---------- BFS ----------
    depth = {"Start": 0}
    queue = deque(["Start"])

    while queue:
        node = queue.popleft()

        for nxt in G.neighbors(node):
            if nxt not in depth:
                depth[nxt] = depth[node] + 1
                queue.append(nxt)

    # ---------- 每层有哪些节点 ----------
    levels = {}

    for node, d in depth.items():
        levels.setdefault(d, []).append(node)

    # ---------- 自动计算坐标 ----------
    pos = {}

    vertical_gap = 2.5
    horizontal_gap = 2.0

    max_width = max(len(v) for v in levels.values())

    for d in sorted(levels.keys()):

        nodes = levels[d]
        n = len(nodes)

        total_width = (n - 1) * horizontal_gap

        start_x = -total_width / 2

        for i, node in enumerate(nodes):

            x = start_x + i * horizontal_gap

            y = -d * vertical_gap

            pos[node] = (x, y)

    # ---------- 畫圖 ----------
    plt.figure(figsize=(10, 10))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        node_color="lightblue",
        edgecolors="black",
        font_size=8
    )

    plt.axis("equal")
    plt.axis("off")

    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())
    plt.show()
'''
    plt.show(block=False)
    plt.pause(0.001)'''