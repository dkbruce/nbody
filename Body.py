import random
import string
import numpy as np
import unittest

class Body:
    def __init__(self, initial_position, initial_velocity, mass, radius,
                 id = None):
        self.position = initial_position
        self.velocity = initial_velocity
        self.mass = mass
        self.radius = radius
        if id != None:
            self.id = id
        else:
            self.id = ''.join(random.choices(string.ascii_lowercase +
                                             string.digits, k = 10))
        self.dimension = len(self.position)

    def __repr__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def calculate_movement(self, velocity, dt):
        # Takes np.array velocity vector, computes update position.
        # Done using Euler's method. Could use a different method for
        # improved performance.
        return velocity * dt + self.position
            
    def calculate_velocity(self, acceleration, dt):
        # Takes np.array acceleration vector, computes update velocity.
        # Done using Euler's method. Could use a different method for
        # improved performance.
        return acceleration * dt + self.velocity

    def calculate_acceleration(self, other):
        # Returns scalar value for acceleration created by other body on
        # this body.
        distance = self.calculate_distance(other)
        if distance == 0:
            return 0
        return (6.674e-11) * other.mass / self.calculate_distance(other)

    def calculate_distance(self, other):
        # Returns scalar value for distance between this and other body.
        sq_differences = [(self.position[i] - other.position[i]) ** 2 
                          for i in range(len(self.position))]
        return (sum(sq_differences)) ** 0.5

    def calculate_unit_direction(self, other):
        # Returns np.array unit vector for direction from this body to 
        # other.
        vector = np.array([other.position[i] - self.position[i] 
                           for i in range(len(self.position))])
        return vector / np.linalg.norm(vector)

class TestBody(unittest.TestCase):
    def test_distance(self):
        bodies = [Body(np.array([0, 0]), np.array([0, 0]), 100, 100, 'asdf1234'),
                  Body(np.array([500, 0]), np.array([0, 0]), 5, 10)]
        self.assertEqual(bodies[0].calculate_distance(bodies[1]), 500.0)

    def test_direction(self):
        bodies = [Body(np.array([0, 0]), np.array([0, 0]), 100, 100, 'asdf1234'), 
                  Body(np.array([500, 0]), np.array([0, 0]), 5, 10)]
        self.assertSequenceEqual(bodies[0].calculate_unit_direction(bodies[1]),
                                 np.array([1.,0.]))


if __name__ == '__main__':
    unittest.main()