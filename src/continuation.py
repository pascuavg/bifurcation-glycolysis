
import numpy as np
from scipy.optimize import fsolve
from .model import selkov, jacobian

def find_fixed_point(a, b, guess=[0.5, 0.5]):
    def equations(z):
        return selkov(0, z, a, b)
    sol = fsolve(equations, guess)
    return sol

def stability_analysis(xy, a):
    J = jacobian(xy[0], xy[1], a)
    eigvals = np.linalg.eigvals(J)
    return eigvals
