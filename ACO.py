'''
This file contains our implementation of the Ant Colony Optimization (ACO) algorithm.
'''
import state
import ants
def ACO(num_ants, num_iterations, maze, start_idx, end_idx):
    '''
    Our implementation of the Ant Colony Optimization algorithm for maze solving.
    The algorithm simulates a number of ants exploring the maze, depositing pheromones
    on the successful paths they take. At the end of the simulation, the best path (with the strongest pheromones) 
    is returned.

    Args:
        num_ants (int): Number of ants to simulate.
        num_iterations (int): Number of iterations to run the simulation.
        maze (list): 2D list of ints representing the maze, where -1 indicates
        a wall and 0 indicates a valid path.
        start_idx (tuple): Starting position of the ant in the maze (row, col).
        end_idx (tuple): Ending position of the ant in the maze (row, col).

    Returns:
        best_path (list): A list of tuples representing the best path found by the ants.
        TODO: we can also return pheromone layer for visualization
    '''
    best_path = None

    # create pheromone layer based on maze
    pheromone_layer = state.generate_pheromone_layer(maze)

    for _ in range(num_iterations):
        for _ in range(num_ants):
            path = ants.simulate_ant(maze, pheromone_layer, start_idx)

            # only add pheromones if ant reaches the end
            # this is so that we only reinforce successful paths, find best path
            if path and path[-1] == end_idx:
                state.add_pheromone(pheromone_layer, path, 1.0) # TODO: determine pheromone value. could be a tunable param
    
            if best_path is None or len(path) < len(best_path):
                    best_path = path

        state.evaporate_pheromone(pheromone_layer, 0.1) # TODO: determine decay rate. could be a tunable param

    return best_path
