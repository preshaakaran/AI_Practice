def dfs(graph, visited, src, goal):
    if src == goal:
        print(src)
        return True  # Return True to indicate goal found
    if src not in visited:
        print(src, end=" ")
        visited.append(src)
        for neighbor in graph[src]:
            if dfs(graph, visited, neighbor, goal):
                return True  # Terminate recursion if goal found
    return False  # Return False if goal not found

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": []
}

visited = []
src = input("Enter source node: ").upper()
goal = input("Enter goal node: ").upper()
if not dfs(graph, visited, src, goal):
    print("Goal node not reachable from the source node.")
