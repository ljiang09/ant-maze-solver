# generate maze (which is the pheromone layer)
# represent path by one matrix that we rewrite each time

# ant starts at an entrance. it checks all directions, and makes a choice on where to go
    # this decision is driven by a probability function, which is based on the pheromones
# the ant moves to the next cell, and adds pheromones to that cell
# the ant continues to move until it reaches the exit, backtracking as it goes
# if the ant finds an exit, we have it trace its path again and potentially drop stronger pheromones


# potential steps:
# make the ant die after a certain number of moves (perhaps a boolean feature flag)


