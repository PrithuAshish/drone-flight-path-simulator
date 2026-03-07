# Drone Flight Path Simulator

A Python-based drone navigation simulator that computes and visualizes optimal flight paths in a grid environment with obstacles. Implements A* and Dijkstra pathfinding algorithms with execution timing and realistic movement simulation.

## Key Features

1. **Execution Time Comparison** - Measures A* vs Dijkstra performance in milliseconds
2. **Colored Path Visualization** - A* (green), Dijkstra (orange) with distinct markers
3. **Animated Side-by-Side Comparison** - Generates comparison visualization with both paths
4. **Realistic Drone Simulation** - Includes velocity (5 units/s), energy tracking, waypoint analysis
5. **Enhanced Obstacle Generation** - Random, clustered, and corridor patterns available

## Project Structure

- `main.py` - Full pipeline: timing comparison, metrics, realistic simulation, dual visualizations
- `grid.py` - GridEnvironment with pattern-based obstacle generation (random/clusters/corridor)
- `astar.py` - A* heuristic pathfinding algorithm
- `dijkstra.py` - Dijkstra shortest-path algorithm
- `simulator.py` - Realistic drone sim with velocity, energy, per-waypoint analysis
- `visualization.py` - Colored paths, algorithm comparison side-by-side, grid/legends
- `utils.py` - Path metrics (distance, time, battery)
- `requirements.txt` - Dependencies: numpy, matplotlib

## Runtime

- Language: Python 3.12
- Dependencies: numpy, matplotlib
- Workflow: `python main.py` (console output)
- Output: Console summary + 2 PNG files (individual path, side-by-side comparison)

## Outputs

- `flight_path_a*.png` - Individual path visualization with grid and obstacles
- `algorithm_comparison.png` - Side-by-side paths with step counts and metrics
