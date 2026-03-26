import time
from grid import GridEnvironment
from astar import astar
from dijkstra import dijkstra
from visualization import show_grid, animate_paths
from simulator import simulate_drone_realistic
from utils import compute_metrics

env = GridEnvironment(20, 20)
env.generate_random_obstacles(40)

start = (0, 0)
goal = (18, 18)

print("\n" + "="*50)
print("DRONE FLIGHT PATH SIMULATOR")
print("="*50)
print(f"Grid: {env.width}x{env.height} | Obstacles: 40 | Start: {start} | Goal: {goal}\n")

print("Running A* Algorithm...")
start_time = time.time()
path_astar = astar(env.grid, start, goal)
time_astar = time.time() - start_time

print("Running Dijkstra Algorithm...")
start_time = time.time()
path_dijkstra = dijkstra(env.grid, start, goal)
time_dijkstra = time.time() - start_time

print("\n" + "-"*50)
print("ALGORITHM COMPARISON")
print("-"*50)

if path_astar:
    print(f"A* Path Length: {len(path_astar)} steps | Execution Time: {time_astar*1000:.2f}ms")
else:
    print("A* could not find a path")

if path_dijkstra:
    print(f"Dijkstra Path Length: {len(path_dijkstra)} steps | Execution Time: {time_dijkstra*1000:.2f}ms")
else:
    print("Dijkstra could not find a path")

if path_astar and path_dijkstra:
    print(f"A* is {(time_dijkstra/time_astar - 1)*100:.1f}% faster\n")

distance, time_taken, battery = compute_metrics(path_astar)

print("-"*50)
print("PATH METRICS (A* Algorithm)")
print("-"*50)
print(f"Distance: {distance} units")
print(f"Time Estimate: {time_taken:.1f} seconds")
print(f"Battery Usage: {battery:.1f}%\n")

print("Simulating realistic drone movement...")
if path_astar:
    simulate_drone_realistic(path_astar)
else:
    print("Skipping drone simulation — no path found")

print("\nGenerating visualizations...")
if path_astar:
    show_grid(env.grid, path_astar, start, goal, algorithm="A*")

if path_astar and path_dijkstra:
    animate_paths(env.grid, path_astar, path_dijkstra, start, goal)
else:
    print("Skipping comparison visualization — one or more paths missing")

print("\n" + "="*50)
print("SIMULATION COMPLETE")
print("="*50)
