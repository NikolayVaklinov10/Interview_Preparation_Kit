def constructGraph(graph_nodes, graph_from, graph_to):
    graph = dict()

    for i in range(graph_nodes):
        graph[i + 1] = []

    for i in range(len(graph_from)):
        from_node = graph_from[i]
        to_node = graph_to[i]
        graph[from_node].append(to_node)
        graph[to_node].append(from_node)

    return graph


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = constructGraph(graph_nodes, graph_from, graph_to)
    # Graph is now constructed.
    # Example: {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}

    nodes_of_target_color = []

    for i in range(graph_nodes):
        if ids[i] == val:
            nodes_of_target_color.append(i + 1)

    # Got a list of nodes of target color. Example: [1, 3, 4]

    depths = []

    for node in nodes_of_target_color:
        seen = set()
        depth = 0
        neighbors = []
        seen.add(node)
        neighbors.extend(graph[node])

        while len(neighbors) > 0:
            depth += 1

            for node in neighbors:
                seen.add(node)
                if node in nodes_of_target_color:
                    depths.append(depth)

            new_neighbors = []

            for node in neighbors:
                new_neighbors.extend(graph[node])

            deduped_new_neighbors = [node for node in new_neighbors if node not in seen]
            neighbors = deduped_new_neighbors

    if len(depths) > 0:
        return min(depths)
    else:
        return -1
