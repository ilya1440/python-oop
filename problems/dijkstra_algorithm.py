import typing as t
from math import inf


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self) -> t.List:
        return self._links

    def get_adj_vertices(self):
        for link in self.links:
            for vertex in [link.v1, link.v2]:
                if vertex != self:
                    yield vertex, link


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Link:
    def __init__(self, vertex_1, vertex_2):
        self._v1 = vertex_1
        self._v2 = vertex_2
        self._dist = 1
        vertex_1.links.append(self)
        vertex_2.links.append(self)

    @property
    def v1(self) -> Vertex:
        return self._v1

    @property
    def v2(self) -> Vertex:
        return self._v2

    @property
    def dist(self) -> int:
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __hash__(self):
        return hash(hash(self._v1) + hash(self._v2))


class LinkMetro(Link):
    def __init__(self, vertex_1, vertex_2, dist):
        super().__init__(vertex_1, vertex_2)
        self.dist = dist


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def make_matrix(self):
        pass

    def add_vertex(self, vertex):
        if vertex not in self._vertex:
            self._vertex.append(vertex)

    def add_link(self, link):
        flag = True
        for link_in in self._links:
            if hash(link_in) == hash(link):
                flag = False
                break
        if flag:
            self._links.append(link)
            for vertex in [link.v1, link.v2]:
                self.add_vertex(vertex)

    @staticmethod
    def argmin(T: t.List, S: t.Set, stop_index: int) -> int:
        m = max(T)
        result_index = stop_index
        for index, value in enumerate(T):
            if value < m and index not in S:
                if index == stop_index:
                    return stop_index
                else:
                    m = value
                    result_index = index
        return result_index

    def find_path(self, start_v: Vertex, stop_v: Vertex) -> t.Tuple[t.List[Vertex], t.List[Link]]:
        N = len(self._vertex)
        hash_map = {
            key: value for value, key in enumerate(self._vertex)
        }
        link_bucket = {
            key: [] for key in range(N)
        }
        T = [inf] * N
        start_index = hash_map.get(start_v)
        stop_index = hash_map.get(stop_v)
        T[start_index] = 0
        S = {start_index}

        while start_index != stop_index:
            adj_vertex_gen = self._vertex[start_index].get_adj_vertices()

            for adj_vertex, link in adj_vertex_gen:
                adj_index = hash_map.get(adj_vertex)
                if adj_index not in S:
                    w = T[start_index] + link.dist
                    if w < T[adj_index]:
                        T[adj_index] = w
                        link_bucket[adj_index] = link_bucket[start_index] + [link]

            start_index = self.argmin(T, S, stop_index)
            if start_index > 0:
                S.add(start_index)

        vert_list = [start_v] + [link.v2 for link in link_bucket[stop_index]]
        return vert_list, link_bucket[stop_index]


map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"




