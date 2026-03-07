# Drone Flight Path Simulator

A Python-based drone navigation simulator that computes and visualizes optimal flight paths in a grid environment with obstacles. Implements A* and Dijkstra pathfinding algorithms.

## Project Structure

- `main.py` - Entry point: sets up grid, runs both algorithms, outputs metrics, simulates drone, saves visualization
- `grid.py` - `GridEnvironment` class: creates NumPy grid and generates random obstacles
- `astar.py` - A* pathfinding algorithm implementation
- `dijkstra.py` - Dijkstra pathfinding algorithm implementation
- `simulator.py` - Drone movement simulation (prints each step)
- `visualization.py` - Matplotlib-based grid/path visualization (saves to `flight_path.png`)
- `utils.py` - `compute_metrics()`: distance, time, battery usage
- `requirements.txt` - Python dependencies: numpy, matplotlib
- `test_cases/scenarios.md` - Manual test scenarios

## Runtime

- Language: Python 3.12
- Dependencies: numpy, matplotlib
- Workflow: `python main.py` (console output type)

## Notes

- `visualization.py` uses `matplotlib` with `Agg` backend (non-interactive) since no display is available. Flight path is saved to `flight_path.png`.
- `simulator.py` prints each drone movement step without sleep delays for fast console output.
- On each run, a 20x20 grid is generated with 40 random obstacles; start=(0,0), goal=(18,18).
