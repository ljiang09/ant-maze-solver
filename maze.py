"""
This file contains functions related to the maze generation and view. Note
that since maze generation was not the goal of this project, we are using
code that is not ours.
"""

import random


def generate_maze(rows, cols, num_exits=2):
    """
    Randomly generates a maze of a specified size and with the specified number of exits.
    The maze is treated as a matrix of cells, where -1 indicates a wall and 0 indicates
    a valid path.

    Args:
        rows (int): Number of rows in the maze
        cols (int): Number of columns in the maze
        num_exits (int): Number of exits to create in the maze,
                         must be more than 2 for a maze to actually work

    Returns:
        A tuple containing:
        - exits: A list of tuples representing the coordinates of the exits
        - maze: A 2D list representing the maze, where -1 indicates a wall
            and 0 indicates a valid path
    """
    maze = [[-1 for _ in range(cols)] for _ in range(rows)]

    start_row, start_col = random.randint(1, rows - 2), random.randint(1, cols - 2)
    maze[start_row][start_col] = 0

    def carve(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 1 <= nx < rows - 1 and 1 <= ny < cols - 1:
                if maze[nx][ny] == -1:
                    maze[x + dx][y + dy] = 0
                    maze[nx][ny] = 0
                    carve(nx, ny)

    carve(start_row, start_col)

    # Generate exits on border
    exits = set()
    potential_exits = []
    for i in range(1, cols - 1):
        potential_exits += [(0, i), (rows - 1, i)]  # top and bottom
    for i in range(1, rows - 1):
        potential_exits += [(i, 0), (i, cols - 1)]  # left and right

    random.shuffle(potential_exits)

    for x, y in potential_exits:
        if len(exits) >= num_exits:
            break
        if (
            (x == 0 and maze[1][y] == 0)
            or (x == rows - 1 and maze[rows - 2][y] == 0)
            or (y == 0 and maze[x][1] == 0)
            or (y == cols - 1 and maze[x][cols - 2] == 0)
        ):
            maze[x][y] = 0
            exits.add((x, y))

    return list(exits), maze


def print_maze(maze):
    """
    Prints a visual of the maze in terminal. Maze paths are represented in numbers,
    and walls are represented in dots.

    Args:
        maze (list): 2D list of ints representing the maze, where -1 indicates
                     a wall and 0 (or numbers for pheromones) indicates a valid path.
    """
    BLACK = "\033[1;30m"
    RED = "\033[91m"
    RESET = "\033[0m"
    for row in maze:
        line = ""
        for cell in row:
            if cell == -1:
                line += f"{BLACK} .{RESET} "
            else:
                line += f"{RED}{str(cell*10)[:2]:>2}{RESET} "
        print(line)


def print_maze_with_path(maze, best_path):
    """
    Prints a visual of the maze in terminal, with the best path highlighted.
    Maze paths are represented with a `0`, and maze walls are represented with a `.`.
    The best path is represented with a `0` in red.

    Args:
        maze (list): 2D list of ints representing the maze, where -1 indicates
                     a wall and any other value indicates a valid path.
        best_path (list): A list of tuples representing the coordinates of the
                          best path in the maze.
    """
    BLACK = "\033[1;30m"
    RED = "\033[91m"
    RESET = "\033[0m"

    if not best_path:
        print("No path found. Try increasing the num iterations or num ants.")
        return

    for r, row in enumerate(maze):
        line = ""
        for c, cell in enumerate(row):
            if cell == -1:
                line += f"{BLACK} .{RESET} "
            elif (r, c) in best_path:
                line += f"{RED} 0{RESET} "
            else:
                line += " 0 "
        print(line)
