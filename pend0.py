import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81    # acceleration due to gravity (m/s^2)
m = 1.0     # mass of pendulum (kg)
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
    omega[k+1] = omega[k] + dt*(-g/L*np.sin(theta[k]) - c/(m*L**2)*omega[k])

# Plot angle and angular velocity as functions of time
plt.figure(figsize=(10,5))
plt.plot(t_array, theta, label='Angle')
plt.plot(t_array, omega, label='Angular velocity')
plt.xlabel('Time (s)')
plt.ylabel('Angle, Angular velocity')
plt.title('Damped pendulum')
plt.legend()
plt.grid()
plt.show()