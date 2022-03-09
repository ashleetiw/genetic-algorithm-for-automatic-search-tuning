#!/usr/bin/env python

import numpy as np
import cv2
import scipy.stats as st
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import random

class genetic_algorithm:
    def __init__(self,optimizer,func):
        self.min_or_max=optimizer
        self.fitness_function=func
      
        
    def generate_binary_string(self,length):
        """
        generates random string consisting of "0" and "1"

        :param length: [int] length of random string
        :returns: [string] random string consisting of "0" and "1"
        """
        s=[]
        for _ in range(length):
            # random.random() yields a float between 0 and 1
            if random.random() < 0.5:
                s.append('0')
            else:
                s.append('1')
            
        return ''.join(s)       

    def generate_random_population(self,number,length):
        """
        generates the very first population.
        This implementation ensure that chromosomes in the initial population
        are uniformly pseudo-random!

        :param number: [int] number of strings to return
        :param length: [int] length of the strings to return
        :returns: List[str] list of random binary strings
        """
        return [self.generate_binary_string(length) for _ in range(number)]

   
    def reproduction(self,population):
        """ 
        This function takes a population of chromosomes and generates a new population.
        Each chromosome in the population is assigned a weight, based off the chromosome's fitness function 
        The weights define how likely the member is going to be picked for the next population
        """
        self.min_fitness = min(self.fitness_function(m) for m in population)
        # # Here we normalize the weights to be proportions of the total weighting
        weights = [(m, self.compute_weight(m)) for m in population]
        total_weights = sum(w for m, w in weights)
        pdf = [(m, w/total_weights) for m, w in weights]

        new_population = []
        for i in range(len(population)):
            rand = random.random()
            cumulative = 0
            for member, end_interval in pdf:
                cumulative  += end_interval
                if rand <= cumulative:
                    new_population.append(member)
                    break # generate next member
        
        return new_population
        
    def compute_weight(self,m):
            """
            Weight of each member is commensurate with its distance from the member with lowest fitness in the population.
            Maximizing : Weight=fitness - self.min_fitness + 1
            Minimizing :Weight=1/fitness - self.min_fitness + 1
            """
            fitness = self.fitness_function(m)
            if self.min_or_max == 'MAX':
                return fitness - self.min_fitness + 1
            
            elif self.min_or_max == 'MIN':
                return 1 / (fitness - self.min_fitness + 1)
        

    def crossover_op(self,string1, string2, index):
        head1, tail1 = string1[:index], string1[index:]
        head2, tail2 = string2[:index], string2[index:]
        return head1+tail2, head2+tail1


    def population_crossover(self,population, crossover_probability):
        pairs = []
        new_population = []
        while len(population) > 1:
            pairs.append((population.pop(), population.pop()))
        if len(population) == 1:
            new_population.append(population.pop())
            
        for s1, s2 in pairs:
            if crossover_probability<0.5: 
                # don't perform crossover, just add the original pair
                new_population += [s1, s2]
                continue
            idx = random.randint(1, len(s1)-1) # select crossover index
            new_s1, new_s2 = self.crossover_op(s1, s2, idx)
            new_population.append(new_s1)
            new_population.append(new_s2)
        return new_population


    def mutation_op(self,string, probability):
    
        flipped = []
        for x in string:
            if x=='1':
                flipped.append('0')
            else:
                flipped.append('1')
        return ''.join(flipped)

    def population_mutation(self,population, prob):
        """
        :param population: [List[str]] 
            population of binary strings
        :returns: [List[str]] 
            just the input population with some members possibly mutated
        """
        return [self.mutation_op(m, prob) for m in population]

    


