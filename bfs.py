visited = []
queue = []


def bfs(visited, graph, src, goal):
    visited.append(src)
    queue.append(src)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == goal:
            print("\nGoal node reached!")
            break

        for i in graph[m]:
            if i == " " and i != goal:
                continue
            elif i not in visited:
                visited.append(i)
                queue.append(i)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [" "],
    "E": ["F"],
    "F": [" "],
    "G": [" "]
}

src = input("Enter source node: ")
goal = input("Enter goal node: ")

print(f"Following is the Breadth-First Search from node {src} to node {goal}:")
bfs(visited, graph, src, goal)
