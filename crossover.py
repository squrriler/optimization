import random
import selection as st
import function as ft

def crossover(population, fitness_value, probability_cross):  #BLX-alpha, alpha = 0.5
    for i in range(len(population)):
        child = 0
        parent1 = population[i]
        parent2 = population[st.selection(fitness_value)]
        if(probability_cross > random.random()):
            r = 2 * random.random() - 0.5
            if parent1 < parent2:
                child = (1 - r) * parent1 + r * parent2
            else:
                child = (1 - r) * parent2 + r * parent1
        if ft.fun(child) > ft.fun(parent1):
            population[i] = child        