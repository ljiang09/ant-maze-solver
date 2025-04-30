"""This file contains the functions related to ant movement and choices in the maze."""

import random


def find_probability(pheromone_layer, neighbors, pheromone_strength):
    """
    Finds the probability of moving to each neighboring cell based on pheromone levels.

    Args:
        pheromone_layer (list of list of float): Current pheromone grid.
        neighbors (list of (row, col)): Valid next positions.

    Returns:
        probabilities (list of float): Probabilities of moving to each neighboring cell.
    """
    # reads pheromones of neighboring cells
    pheromones = [pheromone_layer[row][col] + pheromone_strength / 10 for row, col in neighbors]

    # normalizes pheromones
    total = sum(pheromones)
    probabilities = [p / total for p in pheromones]

    # chooses next move based on pheromone levels
    return probabilities


def get_neighbors(maze, position, path):
    """
    Finds the neighboring path cells of a given position in the maze. If a cell
    has already been visited, it is not considered a neighbor. This prevents
    backtracking or ants looping its already traversed path.

    Args:
        maze (list): 2D list of ints representing the maze, where -1 indicates
                     a wall and 0 indicates a valid path.
        position (tuple): The current position in the maze (row, col).
        path (list): The current path taken by the ant.

    Returns:
        neighbors (list): A list of tuples representing the coordinates of the
                          neighboring cells that are not walls.
    """
    # getting row/col
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    # finding new positions based on direction
    for delta_r, delta_c in directions:
        new_r, new_c = row + delta_r, col + delta_c

        # check if new pos is within path bounds
        if 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]):
            if maze[new_r][new_c] != -1 and (new_r, new_c) not in path:
                neighbors.append((new_r, new_c))
    return neighbors


def simulate_ant(maze, pheromone_layer, start, end, pheromone_strength, max_steps=100):
    """
    Simulates the ant finding the path in the maze. Does not backtrack. If the ant
    reaches a dead end, or max number of steps, then simulation ends.

    Args:
        maze (list): 2D list of ints representing the maze, where -1 indicates
                     a wall and 0 indicates a valid path.
        pheromone_layer (list): 2D list of floats representing the pheromone layer,
                                where -1 indicates a wall and 0 indicates a valid path.
        start (tuple): Where the ant starts in the maze (row, col).
        end (tuple): Where the end cell of the maze is (row, col).
        max_steps (int): Max number of steps an ant can take.

    Returns:
        path (list): A list of tuples representing the path taken by the ant.
                     If the ant can't reach the end, the path will be incomplete and None
                     will be returned.
    """
    curr_position = start
    path = [curr_position]

    # while the ant is not at the end and has not reached max steps
    for _ in range(max_steps):
        if curr_position == end:
            break
        neighbors = get_neighbors(maze, curr_position, path)
        if not neighbors or (
            len(neighbors) == 1 and neighbors[0] in path
        ):  # if no neighbors or neighbor is already in path
            # ant is stuck, return None
            return path

        # finds probs of moving to a cell, and chooses next move
        probabilities = find_probability(pheromone_layer, neighbors, pheromone_strength)
        curr_position = random.choices(neighbors, weights=probabilities)[0]
        path.append(curr_position)
    return path
