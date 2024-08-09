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
