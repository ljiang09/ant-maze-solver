"""
Ant Colony Optimization (ACO) for maze solving

This is a simulation of the Ant Colony Optimization (ACO) algorithm for maze solving.
Here, we choose a number of ants to simulate, and a number of iterations to run the simulation.
Then we generate a maze of a certain size, and run the ACO algorithm on it. The visual
representation of the original maze, the best path found, as well as the pheromone layer are printed.
"""

from maze import generate_maze, print_maze, print_maze_with_path
from ACO import ACO

# 1) generate maze
MAZE_LENGTH = 15
NUM_EXITS = 2  # for entrance and exit
exits, maze = generate_maze(MAZE_LENGTH, MAZE_LENGTH, NUM_EXITS)

# 2) establish number of ants, iterations, and other parameters
NUM_ANTS = 100
NUM_ITERATIONS = 100
PHEROMONE_STRENGTH = 1.0
EVAPORATION_RATE = 0.05

# 3) run ACO algorithm on maze
best_path, pheromone_layer = ACO(
    NUM_ANTS,
    NUM_ITERATIONS,
    maze,
    exits,
    pheromone_strength=PHEROMONE_STRENGTH,
    evaporation_rate=EVAPORATION_RATE,
)

# 4) visualize maze, best path, and pheromone layer
print(
    f"Number of ants: {NUM_ANTS}\n Number of iterations: {NUM_ITERATIONS} \n Maze size: {MAZE_LENGTH}x{MAZE_LENGTH}"
)
print(
    f"Evaporation rate: {EVAPORATION_RATE} \n Pheromone strength: {PHEROMONE_STRENGTH}\n"
)
print("Best path found by ants:", best_path)

print("OG maze:")
print_maze(maze)
print("*********************************************")
print("Best path:")
print_maze_with_path(maze, best_path)
print("*********************************************")
print("Pheromone layer:")
print_maze(pheromone_layer)
