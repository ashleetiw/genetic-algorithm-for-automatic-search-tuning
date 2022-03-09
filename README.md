# Search alogrithm - BFS, DFS, Astar
`.py`-This is an implementation of the Simple Genetic Algorithm.Given a list of genes and a fitness function, the algorithm starts from a random population and evolves it, generation after generation, until it has converged to a good solution.


## Problem statement 
### Hypothesis: pool of function candidates
[ log(x), x , -x , log(-x), e^x, e^-x, 1/x ,-1/x, sin(x), cos(x)]

### Decoding
Genetic algorithm accepts a binary string.Eg ( '111000011010').To use genetic algorithm for finding the correct pattern, I mapped the chromosome length to the number of candidates in the hypothesis.
#### Example
Binary string 10100000110 maps to function log(x)-x -1/x+sin(x)


### Fitness function 

### Other Fitness Function 
Benchmarks and decoders  that were implemented and tested here are:
1. DeJong function (Sphere function)
2. Elementary Symmetric Function


## General Genetic Algorithm 
![main](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/Untitled%20drawing.jpg)

### Generate First Population
I implemented the `chromosome` as a Python string, where each character is eother 0 or 1.`Population` is a Python list of strings.This implementation ensure that chromosomes in the initial population are uniformly pseudo-random!
#### Example
![pop](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/first_pop.png)

### Reproduction
It takes a population and generates a new population based on based roulette selection.
1. Each chromosome is assgined a weight, based on `fitness function`.
2. These weights define how likely the member will be passed in the new generation
3. optimizer can be `Min` or `Max` based on if you want to optimize to global maxima or minima

### Crossover
Crossover is the most significant phase in a genetic algorithm. For each pair of parents to be mated, a crossover point is chosen at random from within the genes.
Offspring are created by exchanging the genes of parents among themselves until the crossover point is reached.
#### Example
![cross](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/crossover.png)

### Mutation
In certain new offspring formed, some of their genes can be subjected to a mutation with a low random probability. This implies that some of the bits in the bit string can be flipped. Mutation occurs to maintain diversity within the population and prevent premature convergence.
#### Example
![mut](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/mutation.png)


### Termination
The algorithm terminates if the population has converged (does not produce offspring which are significantly different from the previous generation). Then it is said that the genetic algorithm has provided a set of solutions to our problem.
Another method is to define the number of eras that one wish to perform evolution

### Evaluation


