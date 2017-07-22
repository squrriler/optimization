import numpy as np
from matplotlib import pyplot as plt

def cal_function_value(population):
    function_value = []
    for i in range(len(population)):
        x = population[i]
        function_value.append(10 * np.sin(5 * x) + 7 * np.cos(4 * x))
    return function_value

def fun(x):
    return 10 * np.sin(5 * x) + 7 * np.cos(4 * x)
