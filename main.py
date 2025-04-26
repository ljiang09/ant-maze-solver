# generate maze (which is the pheromone layer)
# represent path by one matrix that we rewrite each time

# ant starts at an entrance. it checks all directions, and makes a choice on where to go
    # this decision is driven by a probability function, which is based on the pheromones
    # its path is tracked as it goes along
# the ant continues to move until it reaches the exit, reaches a dead end, or reaches the max number of steps
# if the ant finds an exit, we drop pheromones on the path it took based on the length of path

# after each ant run, we evaporate pheromones by a certain decay rate, which ensures that the strongest paths are reinforced
# the algorithm runs for a certain number of iterations, and the best path at the end is returned


# potential steps:
# make the ant die after a certain number of moves (perhaps a boolean feature flag)
from maze_generation import generate_maze, print_maze
from ACO import ACO

#1) generate maze
exits, maze = generate_maze(10,10,2)
start_idx = exits[0]
end_idx = exits[1]

#2) establish number of ants and iterations
num_ants = 10
num_iterations = 100

# 3) run ACO algorithm on maze
best_path, pheromone_layer = ACO(num_ants, num_iterations, maze, start_idx, end_idx)
print("Best path found by ants:", best_path)

# 4) visualize maze and path
print_maze(f"Original Maze:{maze}")

print("*********************************************")

print(f"Path found: {pheromone_layer}")
