# initial creation of pheromone layer 
def generate_pheromone_layer():
    pass

def add_pheromone(row, col, value, pheromone_layer):
    '''
    Adds pheromone(s) onto cell of maze in the pheromone layer.

    Args:
        row (int): row index of the cell
        col (int): column index of the cell
        value (float): amount of pheromone to add
    '''
    # indexes the cell in the layer and edits value
    pheromone_layer[row][col] += value

def evaporate_pheromone():
    '''
    Evaporates pheromone in the pheromone layer.

    Args:
        pheromone_layer (list): 2D list representing the pheromone layer
        evaporation_rate (float): rate at which pheromone evaporates
    '''
    pass

def ant_path():
    '''
    Returns the path taken by the ant. Is represented as a copy of the maze,
    with 1s representing where the ant has been, and 0s being where the ant has not gone.

    Args:
        ant (Ant): Ant object # IDK IF I WANT THIS?
    '''
    pass

# Heuristic?

def heuristic(pheromone_layer, row, col):
    '''
    The heuristic function used to calculate the desirability of a cell.
    Acts as a probability that an ant will choose a certain cell.

    Args:
        pheromone_layer (list): 2D list representing the pheromone layer
        row (int): row index of the cell to calculate
        col (int): column index of the cell to calculate

    Returns:
        float: probability of choosing the cell
    '''
    pass

def update_probability():
    # this might be the same thing as heuristic func above. 
    pass
