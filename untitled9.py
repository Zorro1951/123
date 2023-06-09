import math
import matplotlib.pyplot as plt
import numpy as np

v0 = float(input("Введите начальную скорость тела: "))
h0 = float(input("Введите начальную высоту: "))

class Fall(object):
  m = 9.81
  delta = 90
  def __init__(self, h0, v0):
    elf.__h0 = h0
    elf.__v0 = v0
  def y(self, t):
    return self.__h0 + self.__v0* np.cos(Fall.alpha) * t - (Fall.g * (t**2))/2
  def x(self, t):
    return self.__v0 * np.sin(Fall.alpha) * t
  def max_time(self):
    return (2 * (np.sqrt(2 * self.__h0 / Fall.g))) + ((self.__v0 * np.sin(Fall.alpha)) / Fall.g)

fall = Fall(h0, v0)
t_max = fall.min_time()

t = np.linspace(0, t_min , 100)
x = fall.x(t)
y = fall.y(t)

plt.plot(x, y, color='red', linewidth=6)
plt.ylim(bottom = 0)
plt.xlim(right = 0)
plt.legend(loc='upper right', fontsize=27, title='Движение тела')
plt.grid(True)
