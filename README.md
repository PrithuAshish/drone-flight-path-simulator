# 🚁 Drone Flight Path Simulator

A grid-based drone path planning simulator that compares **Dijkstra’s Algorithm**, **A***, and **Memory-Efficient A*** (MEA*) under realistic movement and energy constraints.

---

## 📌 Overview

This project simulates autonomous drone navigation in a 2D grid environment with randomly generated obstacles. It evaluates the performance of classical pathfinding algorithms using:

* 8-directional movement (including diagonals)
* Weighted traversal costs
* Realistic drone metrics (time, battery usage)

The simulator generates both **visual outputs** and **performance comparisons** across different obstacle densities.

---

## ⚙️ Features

* 🧠 Implements:

  * Dijkstra’s Algorithm
  * A* Algorithm (with Euclidean heuristic)
  * Memory-Efficient A* (MEA*)

* 🧭 Realistic Navigation:

  * 8-directional movement
  * Diagonal cost = √2
  * Corner-cutting prevention

* 📊 Performance Metrics:

  * Distance traveled
  * Traversal time (drone)
  * Battery consumption
  * Execution time (algorithm)

* 📈 Visualization:

  * Path plots for each algorithm
  * Comparison image (A* vs Dijkstra vs MEA*)
  * Terminal output logs

---

## 🗂️ Project Structure

```
.
├── main.py                  # Runs single simulation
├── experiment_runner.py     # Runs multiple test cases
├── astar.py                 # A* implementation
├── dijkstra.py              # Dijkstra implementation
├── mea_star.py              # Memory-efficient A*
├── grid.py                  # Environment + obstacles
├── visualization.py         # Plotting + comparison
├── simulator.py             # Drone movement simulation
├── utils.py                 # Metrics computation
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run a single simulation

```
python main.py
```

### 3. Run experiments (0, 20, 40 obstacles)

```
python experiment_runner.py
```

---

## 📊 Sample Output

### Algorithm Comparison (Execution Time)

```
A*       → Steps: 24 | Exec Time: 1.49 ms
Dijkstra → Steps: 24 | Exec Time: 1.95 ms
MEA*     → Steps: 24 | Exec Time: 0.87 ms
```

### Drone Metrics (Traversal)

```
Distance      : 28.38
Traversal Time: 14.19s
Battery Usage : 8.52%
```

---

## 🖼️ Visual Outputs

* Path visualizations for:

  * A*
  * Dijkstra
  * MEA*

* Generated for obstacle densities:

  * 0
  * 20
  * 40

* Comparison plot:

```
algorithm_comparison.png
```

---

## 🧠 Key Insights

* All algorithms produce **optimal paths (same distance)**
* Differences arise in:

  * Execution time
  * Search efficiency
* A* is fastest due to heuristic guidance
* Dijkstra explores more nodes → slower
* MEA* balances memory and performance

---

## 📚 Applications

* Autonomous drone navigation
* Robotics path planning
* AI search algorithm comparison
* Simulation-based optimization

---

## 🔮 Future Improvements

* Dynamic obstacle handling
* Real-time path replanning
* 3D navigation
* Path smoothing techniques
* Integration with reinforcement learning

---

## 👨‍💻 Authors

* Prithu Ashish
* Pradeep C
* Lakshmi Anand
* Ansh Gupta

VIT University, Vellore

---

## 📄 License

This project is for academic and educational use.
