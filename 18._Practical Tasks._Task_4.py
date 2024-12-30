import networkx as nx


def bfs_farthest_node(graph, start_node):
    visited = {start_node}
    queue = [(start_node, 0)]
    farthest_node = start_node
    max_distance = 0

    while queue:
        current_node, distance = queue.pop(0)

        if distance > max_distance:
            max_distance = distance
            farthest_node = current_node

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return farthest_node, max_distance


def tree_diameter(graph):
    arbitrary_start = list(graph.nodes())[0]
    farthest_node_A, _ = bfs_farthest_node(graph, arbitrary_start)
    farthest_node_B, diameter = bfs_farthest_node(graph, farthest_node_A)

    return diameter


tree_graph = nx.Graph()
tree_edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
tree_graph.add_edges_from(tree_edges)

diameter = tree_diameter(tree_graph)
print("Диаметр дерева:", diameter)









