import matplotlib.pyplot as plt
import numpy as np
import math as m

x = np.arange(-1, 1, 0.1)
a = x ** 3
b = x ** 2
y = 40 * a - 3 * b - 20 * x + 5

plt.title("График функции y=40х^3-3*x^2-20*x + 5", color='#000000', fontstyle="oblique", fontweight="bold")
plt.xlabel('Ось х', color='#000000', fontweight="bold")
plt.ylabel('Ось y', color='#000000', fontweight="bold")

ax = plt.gca()
ax.set_facecolor('#7B68EE')
plt.gcf().set_facecolor('#7B68EE')

plt.plot(x, y, color='#800000', marker='.', markersize=7)
plt.show()