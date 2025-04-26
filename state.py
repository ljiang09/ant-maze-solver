'''This file contains functions related to the pheromonal state of the map.'''
import copy

def generate_pheromone_layer(maze):
    '''
    Generates a pheromone layer for the maze.

    Accessible cells in the maze are represented by 0, while walls are
    represented by -1.

    For each accessible cell in the maze, the value of the cell
    represents the amount of pheromone present.

    Args:
        maze (list): 2D list of ints representing the maze, where -1 indicates
        a wall and 0 indicates a valid path.

    Returns:
        pheromone_layer (list): 2D list of floats representing the pheromone layer,
        where -1 indicates a wall and 0 indicates a valid path.
    '''
    pheromone_layer = copy.deepcopy(maze)
    return pheromone_layer

def add_pheromone(pheromone_layer, path, value):
    '''
    Adds pheromones onto cell of maze in the pheromone layer,
    given a value. The amount of pheromone is also divided by the
    length of the path, so that the pheromone is evenly distributed. 

    Args:
        pheromone_layer (list): 2D list representing the pheromone layer
        path (list): list of tuples representing the path taken by an ant
        value (float): amount of pheromone to add
    '''
    # indexes the cell in the layer and edits value
    for cell in path:
        row, col = cell

        # add pheromones to path
        if pheromone_layer[row][col] != -1: 
            pheromone_layer[row][col] += value / len(path)


def evaporate_pheromone(pheromone_layer, evaporation_rate):
    '''
    Evenly evaporates pheromone in the pheromone layer at the end of
    each ant iteration, based on an evaporation rate.

    Args:
        pheromone_layer (list): 2D list representing the pheromone layer
        evaporation_rate (float): rate at which pheromone evaporates

    Returns:
        pheromone_layer (list): 2D list representing the updated pheromone layer
    '''
    # for every path cell in layer, reduces value by evaporation rate
    for row in range(len(pheromone_layer)):
        for col in range(len(pheromone_layer[0])):
            if pheromone_layer[row][col] != -1:
                pheromone_layer[row][col] *= (1 - evaporation_rate)
