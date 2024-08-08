import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81    # acceleration due to gravity (m/s^2)
m = 1.0     # mass of pendulum (kg)
L = 1.0     # length of pendulum (m)
c = 0.5     # damping coefficient (s^-1)
theta_0 = np.pi/8  # initial angle (rad)
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

# Midpoint method for undamped pendulum
for k in range(0, t_array.size-1):
    # Compute midpoints
    theta_mid = theta[k] + 0.5 * dt * omega[k]
    omega_mid = omega[k] + 0.5 * dt * (-g/L*np.sin(theta[k]))
    
    # Update the values using midpoints
    theta[k+1] = theta[k] + dt * omega_mid
    omega[k+1] = omega[k] + dt * (-g/L*np.sin(theta_mid))

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

# ------------------------ APPENDIX ------------------------

# Euler's method is a first-order method, which means 
# that the error in the method is proportional to the time step.

# # Explicit Euler's method for undamped pendulum
# for k in range(0, t_array.size-1):
#     theta[k+1] = theta[k] + dt*omega[k]
#     omega[k+1] = omega[k] + dt*(-g/L*np.sin(theta[k]) )

# The midpoint method is a second-order method, which means 
# that the error in the method is proportional to the square of the time step.
# https://en.wikipedia.org/wiki/Midpoint_method

# # Explicit midpoint method for undamped pendulum
# for k in range(0, t_array.size-1):
#     # Compute midpoints
#     theta_mid = theta[k] + 0.5 * dt * omega[k]
#     omega_mid = omega[k] + 0.5 * dt * (-g/L*np.sin(theta[k]))
    
#     # Update the values using midpoints
#     theta[k+1] = theta[k] + dt * omega_mid
#     omega[k+1] = omega[k] + dt * (-g/L*np.sin(theta_mid))

# # Midpoint method for damped pendulum
# for k in range(0, t_array.size-1):
#     # Compute midpoints
#     theta_mid = theta[k] + 0.5 * dt * omega[k]
#     omega_mid = omega[k] + 0.5 * dt * (-g/L*np.sin(theta[k]) - c/(m*L**2)*omega[k])
    
#     # Update the values using midpoints
#     theta[k+1] = theta[k] + dt * omega_mid
#     omega[k+1] = omega[k] + dt * (-g/L*np.sin(theta_mid) - c/(m*L**2)*omega[k])

# -------------------------------------------------