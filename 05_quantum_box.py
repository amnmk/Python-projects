import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the geometry of our quantum box
box_width = 1.0       # Size of the box (L)
num_points = 1000     # Smoothness of our grid
x = np.linspace(0, box_width, num_points)

# 2. Asks a value for what "n" should be
n = int(input("What should n be? \n "))
          
# 3. Solve the Schrödinger Equation for this specific level
# This formula calculates the Wave Function (Psi)
psi = np.sqrt(2 / box_width) * np.sin((n * np.pi * x) / box_width)

# 4. Calculate the Probability Density (Psi squared)
# In quantum mechanics, squaring the wave tells you exactly WHERE 
# the particle is most likely to be found inside the box.
probability_density = psi ** 2

# 5. Plot the results side by side using Matplotlib
plt.figure(figsize=(10, 5))

# Plots the Wave Function
plt.subplot(1, 2, 1)
plt.plot(x, psi, color="purple", linewidth=2)
plt.title(f"Quantum Wave Function ($\Psi$) for n={n}")
plt.xlabel("Position inside Box")
plt.ylabel("Amplitude")
plt.grid(True)

# Plots the Probability Density
plt.subplot(1, 2, 2)
plt.plot(x, probability_density, color="crimson", linewidth=2, linestyle="--")
plt.fill_between(x, probability_density, color="crimson", alpha=0.3)
plt.title(f"Where is the Particle? ($|\Psi|^2$) for n={n}")
plt.xlabel("Position inside Box")
plt.ylabel("Probability Level")
plt.grid(True)

plt.tight_layout()
plt.show()
