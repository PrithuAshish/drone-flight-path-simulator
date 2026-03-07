def simulate_drone_realistic(path):
    print(f"Starting realistic drone simulation: {len(path)} waypoints")
    
    velocity = 5.0
    energy = 100.0
    energy_per_unit = 0.3
    
    for i, (x, y) in enumerate(path):
        if i > 0:
            prev_x, prev_y = path[i-1]
            distance = abs(x - prev_x) + abs(y - prev_y)
            time_cost = distance / velocity
            energy -= distance * energy_per_unit
            
            print(f"  [{i:3d}] Moving to ({x:2d}, {y:2d}) | Distance: {distance} | Energy: {energy:.1f}% | Est. Time: {time_cost:.1f}s")
        else:
            print(f"  [{i:3d}] Starting at ({x:2d}, {y:2d}) | Energy: {energy:.1f}%")
    
    total_distance = len(path) - 1
    total_time = total_distance / velocity
    print(f"\nDrone arrived at destination!")
    print(f"Total distance: {total_distance} units")
    print(f"Total time: {total_time:.1f}s")
    print(f"Energy remaining: {energy:.1f}%")
