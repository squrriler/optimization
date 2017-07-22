import random

def mutation(population, probability_mutation):                     #uniform mutation
    for i in range(len(population)):
        if(random.random() < probability_mutation):
            population[i] = population[i] + random.uniform(0, max(population) - population[i])
        