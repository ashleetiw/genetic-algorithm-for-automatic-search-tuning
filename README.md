#  Function search/generation using Genetic algorithm 
This is an implementation of the Simple Genetic Algorithm.Given a list of genes and a fitness function, the algorithm starts from a random population and evolves it, generation after generation, until it has converged to a good solution.


## Problem statement 
### Hypothesis: pool of function candidates
[ log(x), x , -x , log(-x), e^x, e^-x, 1/x ,-1/x, sin(x), cos(x)]

### Decoding
Genetic algorithm accepts a binary string.Eg ( '111000011010').To use genetic algorithm for finding the correct pattern, I mapped the chromosome length to the number of candidates in the hypothesis.
#### Example
Binary string 10100000110 maps to function log(x)-x -1/x+sin(x)
![decode](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/decode.png)


### Fitness function 
Benchmarks and decoders that `main.py` has implemented and tested here is:
1. DeJong function (Sphere function)
2. Using base 10 value of the binary string to represent the fitness of the chromosome

### Other Fitness Function 
![obje](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/objective.png)

*https://github.com/epfl-disal/SwarmViz/tree/master/src*
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
For each pair of parents to be mated, a crossover point is chosen at random from within the genes.
Offspring are created by exchanging the genes of parents among themselves until the crossover point is reached.
#### Example
![cross](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/crossover.png)

### Mutation
Creates perturbations in the population. This implies that some of the bits in the bit string can be flipped with a probability P (called mutation probability). Mutation occurs to maintain diversity within the population and prevent premature convergence.
#### Example
![mut](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/mutation.png)


### Termination
The algorithm terminates if the population has converged (does not produce offspring which are significantly different from the previous generation). Then it is said that the genetic algorithm has provided a set of solutions to our problem.
Another method is to define the number of eras that one wish to perform evolution


## Main loop
It runs  for any number of eras. In each era,we:
1. perform reproduction to create a new population from the old population 
2. perform crossover on the population
3. perform mutation on the population 


![p1](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/gaplot.png)
![p2](https://github.com/ashleetiw/genetic-algorithm-for-automatic-search-tuning/blob/main/gaplot2.png)



## References 

1: [https://www.ewh.ieee.org/soc/es/May2001/14/Begin.html](https://www.ewh.ieee.org/soc/es/May2001/14/Begin.htm)

2: [https://github.com/epfl-disal/SwarmViz/tree/master/src](https://github.com/epfl-disal/SwarmViz/tree/master/src)

3: [https://medium.com/backyard-programmers/genetic-algorithm-b5bea51dd969](https://medium.com/backyard-programmers/genetic-algorithm-b5bea51dd969)

4: [https://cppsecrets.com/article.php?id=8633](https://cppsecrets.com/article.php?id=8633)
