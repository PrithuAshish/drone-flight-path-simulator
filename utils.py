import math

def compute_metrics(path):

    if not path or len(path) < 2:
        return 0, 0, 0

    distance = 0

    for i in range(1, len(path)):

        x1, y1 = path[i-1]
        x2, y2 = path[i]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx == 1 and dy == 1:
            distance += math.sqrt(2)
        else:
            distance += 1

    # realistic drone speed model
    drone_speed = 2.0   # units per second
    time_taken = distance / drone_speed

    # realistic battery drain model
    battery_usage = distance * 0.3   # % per unit distance

    return round(distance,2), round(time_taken,2), round(battery_usage,2)
