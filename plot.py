import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.1) # значения которые может принимать х
a = x ** 3
b = x ** 2
y = 40 * a - 3 * b - 20 * x + 5 # уравнение

plt.title("График функции y=40х^3-3*x^2-20*x + 5", color='#000000', fontstyle="oblique", fontweight="bold")# оформление заглавления
plt.xlabel('Ось х', color='#000000', fontweight="bold")# оформление надписи 
plt.ylabel('Ось y', color='#000000', fontweight="bold")# оформление надписи 

plt.plot(x, y, color='#800000', marker='.', markersize=7)# оформление графика 
plt.show()