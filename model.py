import numpy as np
import matplotlib.pylab as plot
import math as m
from math import tan, pi, cos, sin

v = 30 # начальная скорость (м/с)
g = 9.8 # ускорение свободного падения (м/с**2)
angle=30 # начальный угол
y0=10 # начальная вертикальная координата 
rad=180/pi
angle1=angle/rad
t = np.linspace(0, 5, num=100)
x1 = []
y1 = []

for k in t:
    x = ((v*k)*np.cos(angle1))
    y = ((v*k)*np.sin(angle1))-((0.5*g)*(k**2))+y0
    x1.append(x)
    y1.append(y)
p = [i for i, j in enumerate(y1) if j < 0]                         
for i in sorted(p, reverse = True):
    del x1[i]
    del y1[i]

plot.plot(x1, y1)

plot.show()