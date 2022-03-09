import numpy as np
import cv2
# import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from genetic_algorithm import *


def run_genetic_algorithm(func,min_or_max,num_eras, population_size, chromosome_length, 
                            crossover_probability=0.4,mutation_probability=0.005):
    
    # '''
    # # perform reproduction to create a new population from the old population
    # # perform crossover on the population
    # # perform mutation on the population
    # # '''
        
    g=genetic_algorithm(min_or_max,func)
    population=g.generate_random_population(population_size,chromosome_length)
    populations = [population]
    for i in range(num_eras):
        population=g.reproduction(population)
        population=g.population_crossover(population, crossover_probability)
        population=g.population_mutation(population,mutation_probability)
        populations.append(population) 
    # print(populations)

    return populations
  


def dejong_OF(*x):
    return sum(xi**2 for xi in x)

def split_string_into_chunks(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

def dejong_decoder(coding):
    bits_list = split_string_into_chunks(coding,3)
    # take first bit as the sign, and the remaining bits as integers
    signs_nums = [(-1 if bits[0] == '0' else 1, int(bits[1:], 2)) 
                  for bits in bits_list]
    # use modulo to ensure that the numbers fall within the require interval:
    #   -5.12 ≤ x ≤ 5.12
    xlist = [sign * (num % 5.12) for sign, num in signs_nums]
    return xlist


# *****************************************************************
# def calculate_fitness(gen, target, panjang_target):
#     fitness = 0
#     for i in range (panjang_target):
#         if gen[i:i+1] == target[i:i+1]:
#             fitness += 1
#     fitness = fitness / panjang_target * 100
#     return fitness


# target = 'Hello World!'
# panjang_target = len(target)
# max_population = 10
# min_or_max='MIN'
# func=lambda c:calculate_fitness(c, target, panjang_target)
# populations=run_genetic_algorithm(func,min_or_max, num_eras=10, population_size=int(max_population), chromosome_length=panjang_target, 
#                             crossover_probability=0.4,mutation_probability=0.005)



min_or_max='MIN'
obj_fun = dejong_OF
func =  lambda c:obj_fun(*dejong_decoder(c)) 
populations=run_genetic_algorithm(func,min_or_max, num_eras=10, population_size=10, chromosome_length=5, 
                            crossover_probability=0.4,mutation_probability=0.005)


all_chromosomes = {c for pop in populations for c in pop}
optimizer = min if min_or_max == 'MIN' else max
global_optimum = optimizer(all_chromosomes, key=func)
fittest_fitness = func(global_optimum)

print("Global optimum:", global_optimum)
print("Fitness:", fittest_fitness)
print("Decoded:", dejong_decoder(global_optimum))

# Start plotting
# Define the data ranges
x_axis = range(len(populations))
fitnesses = [[func(m) for m in population] for population in populations]
mins = [min(f) for f in fitnesses]
maxs = [max(f) for f in fitnesses]
avgs = [sum(f)/len(f) for f in fitnesses]

optima = [(it, fittest_fitness) for it, pop in enumerate(populations) 
        if fittest_fitness in map(func, pop)]
x_optima, y_optima = zip(*optima) # unzip pairs into two sequences


fig, ax = plt.subplots(1)
l_mins, l_maxs, l_avgs = ax.plot(x_axis, mins, 'r--', maxs, 'b--', avgs, 'g-')
scatter_ceil = ax.scatter(x_optima, y_optima, c='purple')
plt.legend(
    (l_mins, l_maxs, l_avgs, scatter_ceil),("min pop fitness", "max pop fitness", "average pop fitness", "occurrences of global optimum"), loc="upper right",)
# set parameters for the axes
ax.set_xlim(0, len(populations))
ax.set_ylim(0, int(max(maxs) * 1.20))
ax.set_xlabel("era")
ax.set_ylabel("fitness")
plt.show()