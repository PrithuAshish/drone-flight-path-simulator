import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def show_grid(grid, path=None, start=None, goal=None):

    plt.imshow(grid, cmap="gray_r")

    if path:

        xs = [p[0] for p in path]
        ys = [p[1] for p in path]

        plt.plot(xs, ys)

    if start:
        plt.scatter(start[0], start[1])

    if goal:
        plt.scatter(goal[0], goal[1])

    plt.title("Drone Flight Path Simulator")
    plt.savefig("flight_path.png")
    plt.close()
    print("Flight path saved to flight_path.png")
