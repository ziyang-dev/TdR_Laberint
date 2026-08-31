from pathlib import Path
import numpy as np

MAZE_DIR = Path("mazes")

def save_maze(maze, category, algorithm, size, number):
    folder = MAZE_DIR / category / algorithm / size
    folder.mkdir(parents=True, exist_ok=False)

    path = folder / f"maze_{number:05d}.npy"

    np.save(path, np.array(maze, dtype=np.uint8))

def  load_maze(category, algorithm, size, number):
    maze = np.load(f"{MAZE_DIR}/{category}/{algorithm}/{size}/maze_{number:05d}.npy")
    return maze