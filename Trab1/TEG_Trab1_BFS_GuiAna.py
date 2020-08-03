import random
import math
from operator import itemgetter

class Vertice:
    def __init__ (self, n, x, y):
        self.name = n
        self.vizinhos = list()
        self.x = x
        self.y = y

        self.nivel = 9999
        self.color = 'black'
    
    def __str__(self):
        return str(self.name) + ": " + "(" + str(self.x) + "," + str(self.y) + ")"

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
                    value.add_vizinho(v)
                #if key == v:
                #    value.add_vizinho(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(key) + str(self.vertices[key].vizinhos) + "  " + str(self.vertices[key].nivel))

    def busca_largura(self, vertice):
        fila = list()
        vertice.nivel = 0
        vertice.color = 'red'
        for v in vertice.vizinhos:
            self.vertices[v].nivel = vertice.nivel + 1
            fila.append(v)
        
        while len(fila) > 0:
            u = fila.pop(0)
            nodo_u = self.vertices[u]
            nodo_u.color = 'red'

            for v in nodo_u.vizinhos:
                nodo_v = self.vertices[v]
                if nodo_v.color == 'black':
                    fila.append(v)
                    if nodo_v.nivel > nodo_u.nivel + 1:
                        nodo_v.nivel = nodo_u.nivel + 1

g50 = Grafo()

for i in range(1,51):
    x = random.random()
    y = random.random()
    g50.add_vertice(Vertice(i,x,y))

for i in range(1,51):
    niveis = list()
    for j in range(1,51):
        if i != j:
            niveis.append(tuple([j , math.sqrt((g50.vertices[i].x - g50.vertices[j].x)**2 + (g50.vertices[i].y - g50.vertices[j].y)**2)]))
    niveis.sort(key = itemgetter(1))
    ordem = [x[0] for x in niveis]
    
    for j in range(1,int(math.log2(50)+1)):
        g50.add_aresta(i,ordem[j])

print("Grafo 50:")
for i in range(1,51):
    print(g50.vertices[i])
g50.busca_largura(g50.vertices[1])
g50.print_graph()

g100 = Grafo()

for i in range(1,101):
    x = random.random()
    y = random.random()
    g100.add_vertice(Vertice(i,x,y))

for i in range(1,101):
    niveis = list()
    for j in range(1,101):
        if i != j:
            niveis.append(tuple([j , math.sqrt((g100.vertices[i].x - g100.vertices[j].x)**2 + (g100.vertices[i].y - g100.vertices[j].y)**2)]))
    niveis.sort(key = itemgetter(1))
    ordem = [x[0] for x in niveis]
    
    for j in range(1,int(math.log2(100)+1)):
        g100.add_aresta(i,ordem[j])

print("Grafo 100:")
for i in range(1,101):
    print(g100.vertices[i])
g100.busca_largura(g100.vertices[1])
g100.print_graph()

g200 = Grafo()

for i in range(1,201):
    x = random.random()
    y = random.random()
    g200.add_vertice(Vertice(i,x,y))

for i in range(1,201):
    niveis = list()
    for j in range(1,201):
        if i != j:
            niveis.append(tuple([j , math.sqrt((g200.vertices[i].x - g200.vertices[j].x)**2 + (g200.vertices[i].y - g200.vertices[j].y)**2)]))
    niveis.sort(key = itemgetter(1))
    ordem = [x[0] for x in niveis]
    
    for j in range(1,int(math.log2(200)+1)):
        g200.add_aresta(i,ordem[j])

print("Grafo 200:")
for i in range(1,201):
    print(g200.vertices[i])
g200.busca_largura(g200.vertices[1])
g200.print_graph()

g300 = Grafo()

for i in range(1,301):
    x = random.random()
    y = random.random()
    g300.add_vertice(Vertice(i,x,y))

for i in range(1,301):
    niveis = list()
    for j in range(1,301):
        if i != j:
            niveis.append(tuple([j , math.sqrt((g300.vertices[i].x - g300.vertices[j].x)**2 + (g300.vertices[i].y - g300.vertices[j].y)**2)]))
    niveis.sort(key = itemgetter(1))
    ordem = [x[0] for x in niveis]
    
    for j in range(1,int(math.log2(300)+1)):
        g300.add_aresta(i,ordem[j])

print("Grafo 300:")
for i in range(1,301):
    print(g300.vertices[i])
g300.busca_largura(g300.vertices[1])
g300.print_graph()