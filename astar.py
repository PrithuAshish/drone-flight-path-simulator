import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start:0}

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        x,y = current

        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx,ny in neighbors:

            if 0 <= nx < cols and 0 <= ny < rows:

                if grid[ny][nx] == 1:
                    continue

                tentative = g_score[current] + 1

                if (nx,ny) not in g_score or tentative < g_score[(nx,ny)]:

                    g_score[(nx,ny)] = tentative
                    f = tentative + heuristic((nx,ny),goal)

                    heapq.heappush(open_set,(f,(nx,ny)))

                    came_from[(nx,ny)] = current

    return None
