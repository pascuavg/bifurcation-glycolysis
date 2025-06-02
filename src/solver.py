from scipy.integrate import solve_ivp
import numpy as np
from .model import selkov  # ✅ This line fixes your error

def integrate_system(a, b, t_span=(0, 100), y0=[0.5, 0.5]):
    return solve_ivp(lambda t, y: selkov(t, y, a, b), t_span, y0, method='RK45', t_eval=np.linspace(*t_span, 1000))
