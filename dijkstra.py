import heapq
import math

def dijkstra(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    pq = [(0, start)]

    parent = {}
    dist = {start: 0}

    visited = set()

    while pq:

        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:

            path = []

            while node in parent:
                path.append(node)
                node = parent[node]

            path.append(start)
            path.reverse()

            return path

        x, y = node

        neighbors = [
            (x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)
        ]

        for nx, ny in neighbors:

            if 0 <= nx < cols and 0 <= ny < rows:

                if grid[ny][nx] == 1:
                    continue

                # Prevent corner cutting
                if nx != x and ny != y:
                    if grid[y][nx] == 1 or grid[ny][x] == 1:
                        continue
                    move_cost = math.sqrt(2)
                else:
                    move_cost = 1

                new_cost = cost + move_cost

                if (nx, ny) not in dist or new_cost < dist[(nx, ny)]:

                    dist[(nx, ny)] = new_cost
                    parent[(nx, ny)] = node
                    heapq.heappush(pq, (new_cost, (nx, ny)))

    return None
