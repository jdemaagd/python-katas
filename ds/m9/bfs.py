from collections import deque

graph1 = dict()
graph1['A'] = ['B', 'G', 'D']
graph1['B'] = ['A', 'F', 'E']
graph1['C'] = ['F', 'H']
graph1['D'] = ['F', 'A']
graph1['E'] = ['B', 'G']
graph1['F'] = ['B', 'D', 'C']
graph1['G'] = ['A', 'E']
graph1['H'] = ['C']


# NOTE: O(|V| + |E|) where V is the number of vertices and E is the number of edges
# efficient web crawler in which multiple levels of indexes can be maintained for search engines,
# and it can maintain a list of closed web pages from a source web page
# also useful for navigation systems in which neighboring locations
# can be easily retrieved from a graph of different locations
def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]

        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)

    return visited_vertices


print(breadth_first_search(graph1, 'A'))
