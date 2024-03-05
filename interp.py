# Cubic Hermite spline interpolation
# https://en.wikipedia.org/wiki/Cubic_Hermite_spline
import numpy as np
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y = [1, -1/2, 1/3, -1/4, 1/5, -1/6]
dx = [-1/2, 1/3, -1/4, 1/5, -1/6, 1/7]
points = list(zip(x, y, dx))

def h00(t):
  return 2 * t**3 - 3*t**2 + 1

def h10(t):
  return t**3 - 2*t**2 + t

def h01(t):
  return -2*t**3 + 3*t**2

def h11(t):
  return t**3 - t**2


def get_poly(point1, point2):
  x1, y1, dx1 = point1
  x2, y2, dx2 = point2
  return lambda x: h00((x - x1) / (x2 - x1)) * y1 + h10((x - x1)/(x2-x1))*(x2-x1)*dx1 + h01((x-x1)/(x2-x1))*y2 + h11((x-x1)/(x2-x1))*(x2-x1)*dx2

plt.plot(x, y, 'o')
for k in range(0, len(points) - 1):
  f = get_poly(points[k], points[k+1])
  x_dense = np.linspace(x[k], x[k+1], 1000)
  y_points = np.array([f(i) for i in x_dense])
  plt.plot(x_dense, y_points, color='r')
plt.show()
