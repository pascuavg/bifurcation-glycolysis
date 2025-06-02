
import numpy as np

def selkov(t, z, a, b):
    x, y = z
    dxdt = -x + a*y + x**2 * y
    dydt = b - a*y - x**2 * y
    return [dxdt, dydt]

def jacobian(x, y, a):
    j11 = -1 + 2*x*y
    j12 = a + x**2
    j21 = -2*x*y
    j22 = -a - x**2
    return np.array([[j11, j12], [j21, j22]])
