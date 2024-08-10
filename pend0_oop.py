import numpy as np
import matplotlib.pyplot as plt

class DynamicalSystem:
    # ----- Member functions -----
    def __init__(self, func):
        # ----- Member variables -----
        self.dt = 0.001 # Time step.
        self.ode = func

    def simulate(self, tf, x0):
        t = np.arange(0, tf, self.dt) # Initialize time vector.

        # Run the ode function (called func with a dummy input)
        dummy_output = self.ode(np.ones((100, 1)))
        sx = dummy_output.shape

        nt = t.shape[0]

        # Time is a column vector i.e. down a column
        x = np.zeros((nt, sx[0])) 

        x[0, :] = x0.T # Set the initial condition.

        for i in range(nt - 1):
            x[i + 1, :] = x[i, :] + self.ode(x[i, :]) * self.dt

        return (t, x)

    def Hello(self):
        print("Hello World")

def main():
    def pendEOM(x):
        dx = np.zeros(2)
        dx[0] = x[1]
        dx[1] = -9.8 * np.sin(x[0])
        return dx
    
    Pendulum = DynamicalSystem(pendEOM)
    Pendulum.Hello()
    (t, x) = Pendulum.simulate(5, np.array([np.pi / 4, 0]))
    plt.plot(t, x[:, 0])
    plt.show()

if __name__ == "__main__":
    main()