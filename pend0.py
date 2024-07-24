import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81    # acceleration due to gravity (m/s^2)
L = 1.0     # length of pendulum (m)
c = 0.5     # damping coefficient (s^-1)
theta_0 = np.pi/4  # initial angle (rad)
omega_0 = 0.0      # initial angular velocity (rad/s)
dt = 0.01         # time step (s)
t_final = 10.0     # final time (s)

# Initialize arrays for time, angle, and angular velocity
t_array = np.arange(0, t_final, dt)
theta = np.zeros(t_array.size)
omega = np.zeros(t_array.size)

# Initial conditions
theta[0] = theta_0
omega[0] = omega_0

# Euler's method
for k in range(0, t_array.size-1):
    theta[k+1] = theta[k] + dt*omega[k]
    omega[k+1] = omega[k] + dt*(-g/L*np.sin(theta[k]) - c/())
    

# Plot angle and angular velocity as functions of time
