import numpy as np
import random

class GridEnvironment:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))

    def add_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1

    def generate_random_obstacles(self, count):

        for _ in range(count):

            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            self.add_obstacle(x, y)
