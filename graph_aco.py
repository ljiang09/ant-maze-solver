'''
Parameter sweeps for the ACO algorithm.
'''

import copy
from ACO import ACO
from matplotlib import pyplot as plt

# hardcoded maze for testing
exits = [(0, 8)]
maze = [[-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1], [-1, -1, -1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1], [-1, -1, 0, -1, 0, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1], [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1], [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1], [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1], [-1, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1], [-1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

NUM_ANTS = 10
NUM_ITERATIONS = 50
PHEROMONE_STRENGTH = 3
EVAPORATION_RATE = 0.05


# sweep num_ants
def sweep_num_ants(start, end, step, num_iterations=20):
    asymptotic_iterations_avg = []
    asymptotic_iterations_best = []

    for num_ants in range(start, end + 1, step):
        curr_iterations = []
        curr_maze = copy.deepcopy(maze)

        print(f"Running ACO with {num_ants} ants...")

        for _ in range(num_iterations):
            _, best_path_iteration, _ = ACO(
                num_ants,
                NUM_ITERATIONS,
                curr_maze,
                exits,
                pheromone_strength=PHEROMONE_STRENGTH,
                evaporation_rate=EVAPORATION_RATE,
            )
            curr_iterations.append(best_path_iteration)
        
        asymptotic_iterations_avg.append(sum(curr_iterations) / len(curr_iterations))
        asymptotic_iterations_best.append(min(curr_iterations))
    
    plt.figure(1)
    plt.plot(asymptotic_iterations_avg)
    plt.xlabel('Number of Ants')
    plt.ylabel('Average number of iterations to converge')
    plt.figure(2)
    plt.plot(asymptotic_iterations_best)
    plt.xlabel('Number of Ants')
    plt.ylabel('Best number of iterations to converge')
    plt.show()

sweep_num_ants(5, 15, 1)

# num_iterations
# evaporation_rate
