import numpy as np
import matplotlib.pyplot as plt

class DynamicalSystem:
    # ----- Member functions -----
    def __init__(self, func):
        # ----- Member variables -----
        self.dt = 0.001 # Time step.
        self.ode = func

    def simulate(self, tf, x0):
        t = np.arange(0,tf,self.dt) # Initialize time vector.

        # Run the ode function (called func with a dummy input)
        dummy_output = self.ode(np.ones((100,1)))
        sx = dummy_output.shape

        nt = t.shape

        # Time is a column vector i.e. down a column
        x = np.shape((sx[0], nt)) 

        x[0,:] = x0.T # Set the initial condition.

        for i in np.arange(0,nt):
            x[i+1,:] = x[i,:] + self.ode(x[i,:])*self.dt

            return (t,x)
