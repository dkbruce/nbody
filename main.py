from Body import Body
from System import System
import numpy as np

bodies = [Body(np.array([0., 0.]), np.array([0., 0.]), 1.989e30, 6.9551e11, 'Planet A'),
          Body(np.array([1.496e14, 0.]), np.array([0., 3e9]), 5.972e26, 6.371e9, 'Planet B'),
          Body(np.array([1.496e14, 2.25e14]), np.array([5e9, -4e9]), 2.972e28, 6.371e9, 'Planet C')]
system = System(bodies)

def days(number):
    # given input of number of days, outputs number of seconds
    return 86400 * number

tf = days(10)
dt = days(0.001)

system.simulate(tf, dt)