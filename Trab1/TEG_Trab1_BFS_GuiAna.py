import random
import math
from operator import itemgetter

class Vertice:
    def __init__ (self, n, x, y):
        self.name = n
        self.vizinhos = list()
        self.x = x
        self.y = y

        self.nivel = 0
        self.distancia = 9999
        self.color = 'black'
    
    def getValue(self):
        return self.name

    def add_vizinho(self, v):
        if v not in self.vizinhos:
            self.vizinhos.append(v)
            self.vizinhos.sort()

class Grafo:
    vertices = {}

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.name not in self.vertices:
            self.vertices[vertice.name] = vertice
            return True
        else:
            return False
    
    def add_aresta(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    if v not in value.vizinhos:
                        value.add_vizinho(v)
                if key == v:
                    if u not in value.vizinhos:
                        value.add_vizinho(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(key) + str(self.vertices[key].vizinhos) + "  " + str(self.vertices[key].distancia))

    def busca_largura(self, vertice):
        fila = list()
        vertice.distancia = 0
        vertice.color = 'red'
        for v in vertice.vizinhos:
            self.vertices[v].distancia = vertice.distancia + 1
            fila.append(v)
        
        while len(fila) > 0:
            u = fila.pop(0)
            nodo_u = self.vertices[u]
            nodo_u.color = 'red'

            for v in nodo_u.vizinhos:
                nodo_v = self.vertices[v]
                if nodo_v.color == 'black':
                    fila.append(v)
                    if nodo_v.distancia > nodo_u.distancia + 1:
                        nodo_v.distancia = nodo_u.distancia + 1

g = Grafo()
n = 51

for i in range(1,n):
    x = random.random()
    y = random.random()
    g.add_vertice(Vertice(i,x,y))

for i in range(1,n):
    distancias = list()
    for j in range(1,n):
        if i != j:
            distancias.append(tuple([j , math.sqrt((g.vertices[i].x - g.vertices[j].x)**2 + (g.vertices[i].y - g.vertices[j].y)**2)]))
    distancias.sort(key = itemgetter(1))
    ordem = [x[0] for x in distancias]
    
    for j in range(1,5):
        g.add_aresta(i,ordem[j])

g.busca_largura(g.vertices[1])
g.print_graph()