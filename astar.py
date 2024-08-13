def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None, float('inf')  # Return None and infinity for cost

        if n == stop_node or Graph_nodes[n] is None:
            break

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

    if n == stop_node:
        path = []
        total_cost = g[n]  # Total cost of the path
        while n != start_node:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('Path found: {}'.format(path))
        return path, total_cost
    else:
        print('Path does not exist!')
        return None, float('inf')  # Return None and infinity for cost


def get_neighbors(v):
    return Graph_nodes.get(v, [])


def heuristic(n):
    H_dist = {
        'S': 5,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 6,
        'G': 0
    }
    return H_dist.get(n, float('inf'))  # Return infinity for unknown nodes


Graph_nodes = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [],
    'C': [('D', 3), ('G', 4)],
    'D': [],
}

path, total_cost = aStarAlgo('S', 'G')
print("Path:", path)
print("Total cost:", total_cost)