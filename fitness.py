def cal_fitness_value(function_value):
    fitness_value = []
    for i in range(len(function_value)):
        fitness_value.append(1 / (max(function_value) - function_value[i]))
    return fitness_value