# Импортируем библиотеки
import matplotlib.pyplot as plt
import math
import numpy as np
t = np.arange(0,2.5,0.1)
# Уравнение функции
y1 = np.sin(math.pi*t)
plt.plot(t,y1,'b-',)
plt.plot(t,y1,'b.') 
plt.show()