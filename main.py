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
print(f"A* Path Length: {len(path_astar)} steps | Execution Time: {time_astar*1000:.2f}ms")
print(f"Dijkstra Path Length: {len(path_dijkstra)} steps | Execution Time: {time_dijkstra*1000:.2f}ms")
print(f"A* is {(time_dijkstra/time_astar - 1)*100:.1f}% faster\n")

distance, time_taken, battery = compute_metrics(path_astar)

print("-"*50)
print("PATH METRICS (A* Algorithm)")
print("-"*50)
print(f"Distance: {distance} units")
print(f"Time Estimate: {time_taken:.1f} seconds")
print(f"Battery Usage: {battery:.1f}%\n")

print("Simulating realistic drone movement...")
simulate_drone_realistic(path_astar)

print("\nGenerating visualizations...")
show_grid(env.grid, path_astar, start, goal, algorithm="A*")
animate_paths(env.grid, path_astar, path_dijkstra, start, goal)

print("\n" + "="*50)
print("SIMULATION COMPLETE")
print("="*50)
