from grid import GridEnvironment
from astar import astar
from dijkstra import dijkstra
from visualization import show_grid
from simulator import simulate_drone
from utils import compute_metrics

env = GridEnvironment(20,20)

env.generate_random_obstacles(40)

start = (0,0)
goal = (18,18)

print("Running A*")

path_astar = astar(env.grid,start,goal)

print("Running Dijkstra")

path_dijkstra = dijkstra(env.grid,start,goal)

print("A* path length:",len(path_astar))
print("Dijkstra path length:",len(path_dijkstra))

distance,time_taken,battery = compute_metrics(path_astar)

print("Distance:",distance)
print("Time:",time_taken)
print("Battery:",battery)

simulate_drone(path_astar)

show_grid(env.grid,path_astar,start,goal)
