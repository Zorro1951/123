import math
import matplotlib.pyplot as plt
import numpy as np

v0 = float(input("Введите начальную скорость тела: "))
h0 = float(input("Введите начальную высоту: "))

class Fall(object):
  g = 9.81
  alpha = 45
  def __init__(self, h0, v0):
    self.__h0 = h0
    self.__v0 = v0
  def y(self, t):
    return self.__h0 + self.__v0* np.sin(Fall.alpha) * t - (Fall.g * (t**2))/2
  def x(self, t):
    return self.__v0 * np.cos(Fall.alpha) * t
  def max_time(self):
    return (2 * (np.sqrt(2 * self.__h0 / Fall.g))) + ((self.__v0 * np.sin(Fall.alpha)) / Fall.g)

fall = Fall(h0, v0)
t_max = fall.min_time()

t = np.linspace(0, t_max , 1000)
x = fall.x(t)
y = fall.y(t)

plt.plot(x, y, color='green', linewidth=2)
plt.ylim(bottom = 0)
plt.xlim(left = 0)
plt.legend(loc='upper right', fontsize=27, title='Движение тела')
plt.grid(True)

H = float(input ('H = '))
V = float(input('V = '))
T = float(input('T = '))
M = 32 * 10**(-3)
p0 = 10**5
R = 8.31
g = 9.81
k = 1.38 * 10**(-23)
p = p0 * math.exp(-(M* g * H) / (R * T))
N = (p * V) * (k * T)
print("p =", p, "N =", N)
