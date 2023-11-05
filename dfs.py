from graph import Graph


def dfs_find_value(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
    print(current_vertex.index)
    visited.append(current_vertex)

    if current_vertex == target_value:
        return visited

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs_find_value(graph, neighbor, target_value, visited)
            if path:
                return path


def run():
    url_graph = Graph()
    url_graph.add_vertex('0', None)
    url_graph.add_vertex('1', 0)
    url_graph.add_vertex('2', 0)
    url_graph.add_vertex('3', 1)
    url_graph.add_vertex('4', 3)
    url_graph.add_vertex('5', 2)
    val = dfs_find_value(url_graph, url_graph.root, 3)
    print(f'end {val}')

