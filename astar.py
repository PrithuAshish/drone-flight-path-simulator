import heapq
import math


def heuristic(a, b):
    # Euclidean distance (better for diagonal movement)
    return math.hypot(a[0] - b[0], a[1] - b[1])


def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    visited = set()

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current in visited:
            continue

        visited.add(current)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        x, y = current

        neighbors = [
            (x+1, y), (x-1, y), (x, y+1), (x, y-1),        # straight
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1) # diagonal
        ]

        for nx, ny in neighbors:

            if 0 <= nx < cols and 0 <= ny < rows:

                if grid[ny][nx] == 1:
                    continue

                # --- Prevent Corner Cutting ---
                if nx != x and ny != y:
                    if grid[y][nx] == 1 or grid[ny][x] == 1:
                        continue
                    move_cost = math.sqrt(2)
                else:
                    move_cost = 1

                tentative = g_score[current] + move_cost

                if (nx, ny) not in g_score or tentative < g_score[(nx, ny)]:

                    g_score[(nx, ny)] = tentative
                    f = tentative + heuristic((nx, ny), goal)

                    heapq.heappush(open_set, (f, (nx, ny)))
                    came_from[(nx, ny)] = current

    return None
