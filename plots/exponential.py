import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.power(x, 2)

plt.plot(x, y, 'o')

def plot():
    plt.show()
