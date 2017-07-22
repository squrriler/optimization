import numpy as np
from matplotlib import pyplot
import function

x = np.linspace(0, 10)
pyplot.plot(10 * np.sin(5 * x) + 7 * np.cos(4 * x))
pyplot.show()

print function.fun(1.5105697566103822)