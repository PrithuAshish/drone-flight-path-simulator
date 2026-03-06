import heapq

def dijkstra(grid,start,goal):

    rows = len(grid)
    cols = len(grid[0])

    pq = [(0,start)]

    visited = set()

    parent = {}

    while pq:

        cost,node = heapq.heappop(pq)

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

        x,y = node

        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx,ny in neighbors:

            if 0 <= nx < cols and 0 <= ny < rows:

                if grid[ny][nx] == 1:
                    continue

                heapq.heappush(pq,(cost+1,(nx,ny)))

                if (nx,ny) not in parent:
                    parent[(nx,ny)] = node

    return None
