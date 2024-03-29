graph2 = dict()
graph2['A'] = ['B', 'S']
graph2['B'] = ['A']
graph2['S'] = ['A', 'G', 'C']
graph2['D'] = ['C']
graph2['G'] = ['S', 'F', 'H']
graph2['H'] = ['G', 'E']
graph2['E'] = ['C', 'H']
graph2['F'] = ['C', 'G']
graph2['C'] = ['D', 'S', 'E', 'F']


def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root

    while graph_stack:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))

        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node
    return visited_vertices


print(depth_first_search(graph2, 'A'))
