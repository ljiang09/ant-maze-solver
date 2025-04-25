from maze_generation import generate_maze, print_maze
import random

def generate_pheromone_layer(rows, cols, num_exits=2):
    '''
    Generates a pheromone layer for the maze.

    Accessible cells in the maze are represented by 0, while walls are
    represented by -1.

    For each accessible cell in the maze, the value of the cell
    represents the amount of pheromone present.

    Args:
        rows (int): Number of rows in the maze.
        cols (int): Number of columns in the maze.
        num_exits (int): Number of exits to create in the maze.
            Must be more than 2 for a maze to actually work.

    Returns:
        A tuple containing:
        - exits: A list of tuples representing the coordinates of the exits
        - maze: A 2D list representing the maze, where -1 indicates a wall
            and 0 indicates a valid path
    '''
    return generate_maze(rows, cols, num_exits)

def add_pheromone(pheromone_layer, path, amount=1.0):
    '''
    Adds pheromone(s) along a given path in the pheromone layer.
    
    Args:
        pheromone_layer (2D list of floats): The pheromone grid.
        path (list of (row, col)): The path taken by an ant.
        amount (float): Amount of pheromone to add, split across the path.
    '''
    for r, c in path:
        if pheromone_layer[r][c] != -1:  # skip walls
            pheromone_layer[r][c] += amount / len(path)

def evaporate_pheromone(pheromone_layer, decay_rate=0.05):
    '''
    Simulates pheromone evaporation across the grid.
    
    Args:
        pheromone_layer (list of list of float): The pheromone grid.
        decay_rate (float): Proportion of pheromone to evaporate.
    '''
    for r in range(len(pheromone_layer)):
        for c in range(len(pheromone_layer[0])):
            if pheromone_layer[r][c] != -1:
                pheromone_layer[r][c] *= (1 - decay_rate)

def update_probability(pheromone_layer, neighbors):
    '''
    Chooses the next move for an ant based on pheromone levels.
    
    Args:
        pheromone_layer (list of list of float): Current pheromone grid.
        position ((row, col)): Current ant position.
        neighbors (list of (row, col)): Valid next positions.
    
    Returns:
        (row, col): Chosen next move.
    '''
    pheromones = [pheromone_layer[r][c] + 1e-6 for r, c in neighbors]
    total = sum(pheromones)
    probabilities = [p / total for p in pheromones]
    return random.choices(neighbors, weights=probabilities)[0]

def get_neighbors(maze, position):
    r, c = position
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] != -1:
                neighbors.append((nr, nc))
    return neighbors

def simulate_ant(maze, pheromone_layer, start, end, max_steps=100):
    position = start
    path = [position]
    for _ in range(max_steps):
        if position == end:
            break
        neighbors = get_neighbors(maze, position)
        if not neighbors:
            break
        position = update_probability(pheromone_layer, neighbors)
        path.append(position)
    return path

# Example main loop
def run_simulation(maze, start, end, iterations=100, num_ants=10):
    pheromone_layer = [[0 if cell != -1 else -1 for cell in row] for row in maze]
    best_path = None

    for _ in range(iterations):
        for _ in range(num_ants):
            path = simulate_ant(maze, pheromone_layer, start, end)
            if path and path[-1] == end:
                add_pheromone(pheromone_layer, path)
                if best_path is None or len(path) < len(best_path):
                    best_path = path  # ✅ track shortest successful path
        evaporate_pheromone(pheromone_layer)

    return best_path, pheromone_layer


exits, maze = generate_pheromone_layer(20, 20, num_exits=2)

print_maze(maze)

print("*********************************************")

def print_maze_with_path(maze, best_path):
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

best_path, new_maze = run_simulation(maze, exits[0], exits[1], iterations=1000, num_ants=5)
print_maze_with_path(new_maze, best_path)
