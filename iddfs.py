def depth_limited_search(node, goal, depth_limit):
    if node == goal:
        return True
    if depth_limit <= 0:
        return False
    print(node, end=" -> ")  # Print the current node
    for child in get_children(node):
        if depth_limited_search(child, goal, depth_limit - 1):
            return True
    return False


def iterative_deepening_search(start, goal):
    depth_limit = 0
    while True:
        print("Traversing at Depth", depth_limit, ": ", end="")
        if depth_limited_search(start, goal, depth_limit):
            return True
        print()  # Move to the next line for the next depth
        depth_limit += 1


# Example graph and helper function
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": ["G"],
    "G": [],
}

def get_children(node):
    return graph.get(node, [])

# Take input for start and goal nodes
start_node = input("Enter start node: ").upper()
goal_node = input("Enter goal node: ").upper()

# Example usage
print("Traversal Sequence:")
if iterative_deepening_search(start_node, goal_node):
    print("\nGoal node found!")
else:
    print("\nGoal node not found within depth limit.")
