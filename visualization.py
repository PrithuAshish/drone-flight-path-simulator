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
        color = "#00FF00" if algorithm == "A*" else "#FF6600"
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

def animate_paths(grid, path_astar, path_dijkstra, start, goal):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    for ax, path, title, color in [
        (ax1, path_astar, "A* Algorithm", "#00FF00"),
        (ax2, path_dijkstra, "Dijkstra Algorithm", "#FF6600")
    ]:
        ax.imshow(grid, cmap="gray_r")
        
        if path:
            xs = [p[0] for p in path]
            ys = [p[1] for p in path]
            ax.plot(xs, ys, color=color, linewidth=2, alpha=0.8)
            ax.scatter(xs[::max(1, len(xs)//5)], ys[::max(1, len(ys)//5)], 
                      color=color, s=50, alpha=0.6)
        
        ax.scatter(start[0], start[1], color="cyan", s=200, marker="s", zorder=5)
        ax.scatter(goal[0], goal[1], color="red", s=200, marker="*", zorder=5)
        ax.set_title(f"{title}\n{len(path)} steps", fontsize=12, fontweight="bold")
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("algorithm_comparison.png", dpi=100)
    plt.close()
    print("Algorithm comparison saved to algorithm_comparison.png")
