def compute_metrics(path):

    distance = len(path)

    time_taken = distance * 0.5

    battery_usage = distance * 0.2

    return distance, time_taken, battery_usage
