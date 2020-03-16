from typing import (List, Tuple, Union, Hashable)
from pathlib import Path
from pprint import pprint


class Graph:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def add_vertice(self, vertice: Hashable):
        if vertice not in self.vertices:
            self.vertices.append(vertice)

    # Match para aresta já existente
    def add_aresta(self, aresta: Union[Tuple[Hashable, Hashable], Tuple[Hashable, Hashable, int]]):
        if len(aresta) == 2:
            aresta = (*aresta, 1)
        self.add_vertice(aresta[0])
        self.add_vertice(aresta[1])
        aresta = (self.get_inner_vertice(aresta[0]), self.get_inner_vertice(aresta[1]), aresta[2])
        self.arestas.append(aresta)

    def _organize_data(self):
        self.arestas.sort(key=lambda aresta: (aresta[0], aresta[1]))

    def create_adjacent_matrix(self):
        matrix = list()
        for i in range(len(self.vertices)):
            matrix.append(list())
            for j in range(len(self.vertices)):
                matrix[i].append(0)
        for aresta in self.arestas:
            i, j, weight = aresta
            matrix[i][j] = weight
        return matrix

    def create_incident_matrix(self):
        matrix = list()
        for i in range(len(self.arestas)):
            matrix.append(list())
            for j in range(len(self.vertices)):
                matrix[i].append(0)
                if j == self.arestas[i][0] and self.arestas[i][0] == self.arestas[i][1]:
                    matrix[i][j] = -2
                elif j == self.arestas[i][0]:
                    matrix[i][j] = -1
                elif j == self.arestas[i][1]:
                    matrix[i][j] = 1
        return matrix

    def get_origin_vertice(self, inner_vertice: int):
        return self.vertices[inner_vertice]

    def get_inner_vertice(self, outter_vertice):
        for index, vertice in enumerate(self.vertices):
            if outter_vertice == vertice:
                return index

    def get_arestas_vertice(
            self, vertice: Hashable, mode: str = "origin", vertice_mode: str = "origin"):
        if vertice_mode.lower() == "origin":
            vertice = self.get_inner_vertice(vertice)
        arestas = list()
        for aresta in self.arestas:
            if vertice in aresta[:1]:
                if mode.lower() == "origin":
                    origem = self.get_origin_vertice(aresta[0])
                    dest = self.get_origin_vertice(aresta[1])
                    aresta = (origem, dest, aresta[2])
                arestas.append(aresta)
        return arestas

    def get_vertice_degree(self, vertice: Hashable, mode: str = "full", weight: bool = False):
        degree = 0
        if mode.lower() == "full":
            return len(self.get_arestas_vertice(vertice))
        elif mode.lower() == "out":
            for aresta in self.get_arestas_vertice(vertice, mode="origin"):
                if aresta[0] == vertice:
                    degree += aresta[2] if weight else 1
        elif mode.lower() == "in":
            for aresta in self.get_arestas_vertice(vertice, mode="origin"):
                if aresta[1] == vertice:
                    degree += aresta[2] if weight else 1
        return degree

    def _update_arestas(self, old: int, new: int):
        arestas = list()
        for aresta in self.arestas:
            if old == aresta[0]:
                aresta = (new, aresta[1], aresta[2])
            if old == aresta[1]:
                aresta = (aresta[0], new, aresta[2])
            arestas.append(aresta)
        self.arestas = arestas

    def remove_vertice(self, vertice: Hashable):
        if vertice not in self.vertices:
            return
        vertice_inner = self.get_inner_vertice(vertice)
        del self.vertices[vertice_inner]
        for aresta in self.get_arestas_vertice(vertice_inner, mode="inner", vertice_mode="inner"):
            self.arestas.remove(aresta)
        for i in range(vertice_inner+1, len(self.vertices) + 1):
            self._update_arestas(i, i-1)
        for index, value in enumerate(self.vertices):
            if index != self.vertices[value]:
                self._update_arestas(self.vertices[value], index)
                self.vertices[value] = index

    def complemento(self):
        matrix = list()
        for i in range(len(self.vertices)):
            matrix.append(list())
            for j in range(len(self.vertices)):
                matrix[i].append(1)
        for aresta in self.arestas:
            i, j, _ = aresta
            matrix[i][j] = 0
        return matrix


if __name__ == "__main__":
    alpha = ['a', 'b', 'c', 'd', 'e']
    graph = Graph()

    with Path("data/grafo_1.txt").open("r") as input_file:
        for i, line in enumerate(input_file.readlines()):
            for j, char in enumerate(line.strip()):
                if char != '0':
                    graph.add_aresta((alpha[i], alpha[j], int(char)))

    pprint(graph.create_adjacent_matrix())
    pprint(graph.create_incident_matrix())
    pprint(graph.get_arestas_vertice(alpha[2]))
    print(graph.get_vertice_degree(alpha[1], weight=True))
    graph.remove_vertice(alpha[3])
    pprint(graph.create_adjacent_matrix())
    pprint(graph.complemento())
