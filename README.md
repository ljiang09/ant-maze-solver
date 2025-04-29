<!-- A technical writeup present in the README

A technical appendix, also in the README, containing any additional information
relating to your project (ex: pseudocode, diagrams, proofs that didn’t fit into
writeup sections) -->

1 - Understand how to implement ACO

- This will give us a deeper understanding of heuristics
- If the algorithm works, we know we’ve understood how to implement it
- If the solution is an optimized solution (finds shortest path) vs just a
  working solution

# Technical Exploration

## Ant Colony Optimization (ACO) Algorithm

ACO is a probabilistic algorithm inspired by the behavior of ants. It is useful
for finding a lowest cost path through a graph, as well as any problem that can
be reduced to this.

When ants look for food, they leave a pheromone trail behind them which other
ants can then follow. A pheromone trail becomes stronger as more ants take a
path more often, and subsequent ants will tend to follow more pheromone-heavy
paths. Over time, shorter paths end up acquiring more pheromones, creating a
feedback loop to hone in on the best path. Thus, the main strength of this
algorithm is that it uses feedback from previous iterations to build an idea of
what the best path is.

## Applications of ACO in other contexts

ACO is commonly used as an approach to NP-hard problems. The most common of
these is, of course, the Traveling Salesman problem.

ACO can be applied to a variety of NP-hard problems, as long as the problem can
be reduced to a graph.

A tangible application of ACO is protein folding. In this case, the optimization
problem is to find the lowest energy conformation of a protein given its amino
acid sequence. The energy of a conformation can be modeled as a graph, where the
nodes are the amino acids and the edges represent the interactions between them.
The ACO algorithm can be used to explore the conformation space and find the
lowest energy conformation.

<!-- 3. https://lopez-ibanez.eu/doc/StuLopDor2011eorms.pdf -->

<!-- For each method, find a paper that showcases a real-world application where it
has been used effectively. Summarize the application and how the method was
applied to it. Explain why that method is particularly well-suited to the
problem. (5 points per method) -->

## Comparison to Other Maze-Solving Algorithms

erm

## Sources

1. https://induraj2020.medium.com/implementation-of-ant-colony-optimization-using-python-solve-traveling-salesman-problem-9c14d3114475
2. https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://cap.stanford.edu/profiles/cwmd%3Ffid%3D301672%26cwmId%3D10839%23:~:text%3DThe%2520Ant%2520Colony%2520Optimization%2520Algorithm,cost%2520path%2520through%2520a%2520graph.&ved=2ahUKEwj4iM-exfiMAxXuvokEHX2JFeAQFnoECBcQAw&usg=AOvVaw13UjzGvWwFw_3UKssVfxaX
3. http://lopez-ibanez.eu/doc/StuLopDor2011eorms.pdf
