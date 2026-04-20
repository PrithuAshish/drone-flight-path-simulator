import time
from grid import GridEnvironment
from astar import astar
from dijkstra import dijkstra
from mea_star import mea_star
from visualization import show_grid, animate_paths
from simulator import simulate_drone_realistic
from utils import compute_metrics


# High precision timer
def get_time():
    return time.perf_counter()


def run_simulation(obstacle_count, run_drone_sim=True):

    env = GridEnvironment(20, 20)
    env.generate_random_obstacles(obstacle_count)

    start = (0, 0)
    goal = (18, 18)

    print("\n" + "="*60)
    print(f"DRONE FLIGHT PATH SIMULATION | Obstacles = {obstacle_count}")
    print("="*60)

    # ---------- A* ----------
    print("Running A* Algorithm...")
    t0 = get_time()
    path_astar = astar(env.grid, start, goal)
    time_astar = get_time() - t0

    # ---------- Dijkstra ----------
    print("Running Dijkstra Algorithm...")
    t0 = get_time()
    path_dijkstra = dijkstra(env.grid, start, goal)
    time_dijkstra = get_time() - t0

    # ---------- MEA* ----------
    print("Running MEA* Algorithm...")
    t0 = get_time()
    path_mea = mea_star(env.grid, start, goal)
    time_mea = get_time() - t0

    print("\n--- Algorithm Comparison ---")

    if path_astar:
        print(f"A*       → Steps: {len(path_astar):3d} | Time: {time_astar*1000:.4f} ms")
    else:
        print("A*       → No Path Found")

    if path_dijkstra:
        print(f"Dijkstra → Steps: {len(path_dijkstra):3d} | Time: {time_dijkstra*1000:.4f} ms")
    else:
        print("Dijkstra → No Path Found")

    if path_mea:
        print(f"MEA*     → Steps: {len(path_mea):3d} | Time: {time_mea*1000:.4f} ms")
    else:
        print("MEA*     → No Path Found")

    # ---------- Metrics ----------
    if path_astar:
        distance, time_taken, battery = compute_metrics(path_astar)

        print("\n--- Path Metrics (A*) ---")
        print(f"Distance      : {distance}")
        print(f"Est Time      : {time_taken:.2f}s")
        print(f"Battery Usage : {battery:.2f}%")

        if run_drone_sim:
            print("\nSimulating Drone Movement...")
            simulate_drone_realistic(path_astar)

    # ---------- Visualization ----------
    print("\nGenerating Visualizations...")

    if path_astar:
        show_grid(env.grid, path_astar, start, goal,
                  algorithm=f"A*_obs{obstacle_count}")

    if path_mea:
        show_grid(env.grid, path_mea, start, goal,
                  algorithm=f"MEA*_obs{obstacle_count}")

    if path_astar and path_dijkstra:
        animate_paths(env.grid, path_astar, path_dijkstra, start, goal)

    print("\nSimulation Complete\n")


if __name__ == "__main__":
    run_simulation(40)
