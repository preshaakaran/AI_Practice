import random


def total_distance(path, tsp):
    # Calculate the total distance traveled in the given path
    total = 0
    for i in range(len(path) - 1):
        total += tsp[path[i]][path[i+1]]
    total += tsp[path[-1]][path[0]]  # Return to starting city
    return total


def hill_climbing_tsp(tsp, max_iterations=10000):
    num_cities = len(tsp)
    # Initial solution, visiting cities in order
    current_path = list(range(num_cities))
    current_distance = total_distance(current_path, tsp)
    for _ in range(max_iterations):
        # Generate a neighboring solution by swapping two random cities
        neighbor_path = current_path.copy()
        i, j = random.sample(range(num_cities), 2)
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        neighbor_distance = total_distance(neighbor_path, tsp)

        # If the neighbor solution is better, move to it
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
    return current_path


tsp = [
    [0, 16, 11, 6],
    [8, 0, 13, 16],
    [4, 7, 0, 9],
    [5, 12, 2, 0]
]

solution = hill_climbing_tsp(tsp)
print("Optimal path:", solution)
print("Total distance:", total_distance(solution, tsp))
