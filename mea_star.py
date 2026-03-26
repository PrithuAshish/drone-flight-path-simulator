import heapq
import math

def heuristic(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def mea_star(grid, start, goal, memory_limit=200):

    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    memory_queue = []

    while open_set:

        current = heapq.heappop(open_set)[1]

        memory_queue.append(current)
        if len(memory_queue) > memory_limit:
            memory_queue.pop(0)

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
            (x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)
        ]

        for nx, ny in neighbors:

            if 0 <= nx < cols and 0 <= ny < rows:

                if grid[ny][nx] == 1:
                    continue

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