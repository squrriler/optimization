# -*- coding: UTF-8 -*-

import function
import fitness
import crossover
import mutation
import random

population_size = 50
probability_cross = 0.6
probability_mutation = 0.001
max_generation = 100
fitness_value = []
population = [random.uniform(0, 10) for i in range(population_size)]  #initial population
for i in range(max_generation):
    function_value = function.cal_function_value(population)
    fitness_value = fitness.cal_fitness_value(function_value)
    crossover.crossover(population, fitness_value, probability_cross)
    mutation.mutation(population, probability_mutation)
results = dict(zip(population, function.cal_function_value(population)))
print sorted(results.items(), key = lambda d: d[1])
