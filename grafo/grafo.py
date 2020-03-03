from typing import (List, Tuple, Union)
from pathlib import Path
from pprint import pprint

class Graph:
    def __init__(self, vertices: List[int] = []):
        self.vertices = vertices
        self.arestas = []

    def add_vertice(self, vertice: int):
        self.vertices.append(vertice)

    def add_aresta(self, aresta: Union[Tuple[int, int], Tuple[int, int, int]]):
        if len(aresta) == 2:
            aresta = (*aresta, 1)
        self.arestas.append(aresta)
        if aresta[0] not in self.vertices:
            self.add_vertice(aresta[0])
        if aresta[1] not in self.vertices:
            self.add_vertice(aresta[1])

    def organize_data(self):
        self.arestas.sort(key=lambda aresta: (aresta[0], aresta[1]))
        self.vertices.sort()

    def create_adjacent_matrix(self):
        self.organize_data()
        matrix = list()
        for i in range(len(self.vertices)):
            matrix.append(list())
            for j in range(len(self.vertices)):
                matrix[i].append(0)
        for aresta in self.arestas:
            i, j, weight = aresta
            matrix[i][j] = weight
        return matrix

if __name__ == "__main__":
    graph = Graph()
    with Path("./entrada.txt").open("r") as input_file:
        for i, line in enumerate(input_file.readlines()):
            for j, char in enumerate(line.strip()):
                if char != '0':
                    graph.add_aresta((i, j, int(char)))
    pprint(graph.create_adjacent_matrix())