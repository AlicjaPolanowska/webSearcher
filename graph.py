class Vertex:
    def __init__(self, index: int, url: str, previous: int):
        self.index = index
        self.url = url
        self.previous = previous

    def __eq__(self, other):
        return other == self.index

    def __str__(self):
        return f'([{self.previous if self.previous is not None else -1}][{self.index}] {self.url})'


class Graph:
    def __init__(self):
        self.root = None
        self.vertices = []

    def __contains__(self, item):
        return item in [x.index for x in self.vertices]

    def __getitem__(self, item):
        return [x for x in self.vertices if x.previous == item.index]

    def __str__(self):
        value = ''
        for a in self:
            value += f'{a}, \n'
        return value

    def __iter__(self):
        for x in self.custom_iter(self.root):
            yield x

    def custom_iter(self, item, visited=None):
        if visited is None:
            visited = []
        if item not in visited:
            visited.append(item)
        for n in self[item]:
            if n not in visited:
                return self.custom_iter(n, visited)
        if item.index != self.root.index:
            return self.custom_iter(self.get_vertex_by_index(item.previous), visited)
        return visited


    def add_vertex(self, url: str, previous: int):
        index = len(self.vertices)
        vertex = Vertex(index, url, previous)
        if index == 0:
            self.root = vertex
        self.vertices.append(vertex)

    def remove_vertex(self, index: int):
        if len(self.vertices) == 1:
            self.root = None
        return self.vertices.pop(index)

    def get_vertex_by_index(self, index: int):
        return self.vertices.copy()[index:index+1][0]

    def is_empty(self):
        return self.root is None

