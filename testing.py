import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, '-k')  # Curve in black

# Color area under curve
a = 5
b = 7
plt.fill_between(x, y, where=(x>a) & (x<b), color="skyblue", alpha=0.4)
plt.show()
