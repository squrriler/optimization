import random

def selection(fitness_value):
    probability_fitness = []
    total_fitness = sum(fitness_value)
    for i in range(len(fitness_value)):
        probability_fitness.append(fitness_value[i] / total_fitness)
    p = random.random()
    i = 0
    s = probability_fitness[i]
    while s < p:
        i = i + 1
        s = s + probability_fitness[i]
    return i