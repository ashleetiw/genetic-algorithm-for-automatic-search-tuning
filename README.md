# Search alogrithm - BFS, DFS, Astar
`.py`-This is an implementation of the Simple Genetic Algorithm.Given a list of genes and a fitness function, the algorithm starts from a random population and evolves it, generation after generation, until it has converged to a good solution.

## Explanation of Algorithm

Two important entities which were modelled in the code : the `chromosome` and the `population`
### Fitness Function 


## steps to run genetic algorithm 

### Generate First Population


### Reproduction


### Crossover
Crossover is the most significant phase in a genetic algorithm. For each pair of parents to be mated, a crossover point is chosen at random from within the genes.
Offspring are created by exchanging the genes of parents among themselves until the crossover point is reached.
![cross](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/crossover.png)

### Mutation
In certain new offspring formed, some of their genes can be subjected to a mutation with a low random probability. This implies that some of the bits in the bit string can be flipped. Mutation occurs to maintain diversity within the population and prevent premature convergence.
![mut](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/mutation.png)

### Termination
The algorithm terminates if the population has converged (does not produce offspring which are significantly different from the previous generation). Then it is said that the genetic algorithm has provided a set of solutions to our problem.

### Evaluation


