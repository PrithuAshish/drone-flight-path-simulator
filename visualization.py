import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def show_grid(grid, path=None, start=None, goal=None, algorithm="A*"):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(grid, cmap="gray_r")

    if path:
        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        if "astar" in algorithm.lower():
            color = "#00FF00"
        elif "dijkstra" in algorithm.lower():
            color = "#FF6600"
        else:
            color = "#3399FF"
        ax.plot(xs, ys, color=color, linewidth=2, label=f"{algorithm} Path", alpha=0.8)

    if start:
        ax.scatter(start[0], start[1], color="cyan", s=200, marker="s", label="Start", zorder=5)

    if goal:
        ax.scatter(goal[0], goal[1], color="red", s=200, marker="*", label="Goal", zorder=5)

    ax.set_title(f"Drone Flight Path - {algorithm} Algorithm", fontsize=14, fontweight="bold")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    safe_algo = algorithm.lower().replace("*", "star")
    filename = f"flight_path_{safe_algo}.png"
    plt.savefig(filename, dpi=100)
    plt.close()
    print(f"Path visualization saved to {filename}")

def animate_paths(grid, path_astar, path_dijkstra, path_mea, start, goal):
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    configs = [
        (axes[0], path_astar, "A* Algorithm", "#00FF00"),
        (axes[1], path_dijkstra, "Dijkstra Algorithm", "#FF6600"),
        (axes[2], path_mea, "MEA* Algorithm", "#3399FF"),
    ]

    for ax, path, title, color in configs:
        ax.imshow(grid, cmap="gray_r")

        if path:
            xs = [p[0] for p in path]
            ys = [p[1] for p in path]
            ax.plot(xs, ys, color=color, linewidth=2)

        ax.scatter(start[0], start[1], color="cyan", s=100)
        ax.scatter(goal[0], goal[1], color="red", s=100)

        ax.set_title(title)
        ax.grid(True)

    plt.tight_layout()
    plt.savefig("algorithm_comparison.png")
    plt.close()

    print("Algorithm comparison saved to algorithm_comparison.png")
