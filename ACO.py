"""
This file contains our implementation of the Ant Colony Optimization (ACO) algorithm.
"""

import state
import ants


def ACO(
    num_ants, num_iterations, maze, exits, pheromone_strength=1.0, evaporation_rate=0.1
):
    """
    Our implementation of the Ant Colony Optimization algorithm for maze solving.
    The algorithm simulates a number of ants exploring the maze, depositing pheromones
    on the successful paths they take. At the end of the simulation, the best path
    (with the strongest pheromones) is returned.

    Args:
        num_ants (int): Number of ants to simulate.
        num_iterations (int): Number of iterations to run the simulation.
        maze (list): 2D list of ints representing the maze, where -1 indicates
                     a wall and 0 indicates a valid path.
        exits (list): List of tuples representing the coordinates of the start index
                      and end index, respectively.
        pheromone_strength (float): Amount of pheromone to deposit on the path.
        evaporation_rate (float): Rate at which pheromone evaporates.

    Returns:
        best_path (list): A list of tuples representing the best path found by the ants.
        pheromone_layer (list): 2D list of floats representing the pheromone layer.
    """
    best_path = None
    start = exits[0]
    end = exits[1]

    # create pheromone layer based on maze
    pheromone_layer = state.generate_pheromone_layer(maze)

    for _ in range(num_iterations):
        for _ in range(num_ants):
            path = ants.simulate_ant(maze, pheromone_layer, start, end, max_steps=100)

            # only add pheromones if ant reaches the end
            # this is so that we only reinforce successful paths, find best path
            if path and path[-1] == end:
                state.add_pheromone(pheromone_layer, path, pheromone_strength)

            if path:
                if not best_path or len(path) < len(best_path):
                    best_path = path

            # print(f"Ant: this is my path!{path}")

        state.evaporate_pheromone(pheromone_layer, evaporation_rate)

    return best_path, pheromone_layer
