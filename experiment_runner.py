from main import run_simulation

test_cases = [0, 20, 40]

for obs in test_cases:
    run_simulation(obs, run_drone_sim=False)