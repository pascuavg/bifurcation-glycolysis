# Glycolysis Bifurcation Analysis

This project numerically analyzes a reduced model of glycolysis (Sel'kov model) to identify and visualize bifurcation behavior as parameters vary. It focuses on the transition from steady state to oscillations via Hopf bifurcation.

## Model Equations

\[
\begin{aligned}
\frac{dx}{dt} &= -x + ay + x^2 y \\
\frac{dy}{dt} &= b - ay - x^2 y
\end{aligned}
\]

## Files

- `src/model.py`: Defines the ODE system and Jacobian
- `src/solver.py`: Integrates the ODEs
- `src/continuation.py`: Tracks equilibrium points over parameter range
- `notebooks/bifurcation_diagram.ipynb`: Main analysis and plotting
