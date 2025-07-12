import numpy as np
import matplotlib.pyplot as plt

epsilon = 0.9
steps = np.arange(0, 5000, 50)
epsilons = epsilon * (1 - np.exp(-steps / 20))
epsilons = np.minimum(epsilons, epsilon)

plt.plot(steps, epsilons)
plt.xlabel('Step')
plt.ylabel('Epsilon')
plt.title('Epsilon Greedy Decay (epsilon=0.9)')
plt.grid(True)
plt.show()