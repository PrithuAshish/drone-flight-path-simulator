import time

def simulate_drone(path):

    for step in path:

        print("Drone moving to:", step)

        time.sleep(0.3)
