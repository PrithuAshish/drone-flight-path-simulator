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

    def generate_random_obstacles(self, count, seed=None, pattern="random"):
        if seed is not None:
            random.seed(seed)
        
        if pattern == "random":
            for _ in range(count):
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                self.add_obstacle(x, y)
        
        elif pattern == "clusters":
            clusters = max(1, count // 10)
            for _ in range(clusters):
                cx = random.randint(2, self.width - 3)
                cy = random.randint(2, self.height - 3)
                for dx in range(-2, 3):
                    for dy in range(-2, 3):
                        if random.random() < 0.6:
                            self.add_obstacle(cx + dx, cy + dy)
        
        elif pattern == "corridor":
            for y in range(self.height):
                if random.random() < 0.3:
                    x = random.randint(0, self.width - 1)
                    for dy in range(-1, 2):
                        self.add_obstacle(x, y + dy)
