from operator import itemgetter
import graphics
import random

class TreeNode:
    def __init__(self, vertice, distancia):
        self.vertice = vertice
        self.distancia = distancia
        self.children = list()
        self.parent = []
        self.color = "black"

    def add_child(self, child):
        child.parent.append(self)
        for parent in self.parent:
            child.parent.append(parent)
        self.children.append(child)
    
    def get_level(self):
        return self.parent.__len__()
    
    def print_tree(self):
        spaces = " " * self.get_level()*3
        print(spaces + self.vertice.nome)
        if self.children:
            for child in self.children:
                child.print_tree()

class Vertice:
    def __init__(self, nome, id, x, y):
        self.nome = nome
        self.id = id
        self.x = x
        self.y = y
        self.vizinhos = list()

    def add_vizinho(self, vizinho):
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)

class Aresta:
    def __init__(self, pontoA, pontoB, peso):
        self.pontoA = pontoA
        self.pontoB = pontoB
        self.peso = peso
    
    def get_pontoA(self):
        return self.pontoA

class Grafo:
    vertices = list()
    arestas = list()
    minimum_distance_tree = 999999
    minimum_distance_next = 999999
    minimum_tree_path = list()
    minimum_next_path = list()

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice not in self.vertices:
            self.vertices.append(vertice)
            return True
        else:
            return False

    def add_aresta(self, id_pontoA, id_pontoB, peso):
        for v in self.vertices:
            if id_pontoA == v.id:
                for u in self.vertices:
                    if id_pontoB == u.id:   
                        if [u,peso] not in v.vizinhos:   
                            v.add_vizinho([u,peso,])
                            u.add_vizinho([v,peso,])
                            self.arestas.append(Aresta(v,u,peso))
                            return True
        else:
            return False

    def print_grafo(self):
        for v in self.vertices:
            print(v.nome)
            print("----------")
            for u in v.vizinhos:
                print(str(u[0].nome) + ": " + str(u[1]))
    
    def criar_arvore(self, vertice):
        root = TreeNode(vertice,0)
        return root

    def construir_arvore(self, root):
        queue = []
        queue.extend(root.vertice.vizinhos)
        checker = True
        while queue:
            u = queue.pop()
            for parent in root.parent:
                if parent.vertice.nome == u[0].nome:
                    checker = False
            if checker:
                tree_u = TreeNode(u[0],u[1])
                root.add_child(tree_u)
                self.construir_arvore(tree_u)
            checker = True
        
    def fechar_ciclo(self, root, origin):
        root.color = "red"
        queue = []
        queue.extend(root.children)
        if root.children:
            while queue:
                u = queue.pop()
                if u.color == "black": 
                    self.fechar_ciclo(u, origin)
        else:
            for v in root.vertice.vizinhos:
                if v[0] == origin.vertice:
                    tree_v = TreeNode(v[0],v[1])
                    tree_v.color = "red"
                    root.add_child(tree_v)
    
    def caminho_minimo_arvore(self, root, aux_distance, aux_path, origin):
        root.color = "blue"
        if root.children:
            queue = root.children
            while queue:
                u = queue.pop()
                if u.color == "red":
                    aux_distance += u.distancia
                    node_path = []
                    node_path.extend(aux_path)
                    node_path.append(u.vertice)
                    self.caminho_minimo_arvore(u, aux_distance, node_path, origin)
        else:
            print("caminho testado:")
            for v in aux_path:
                print(v.nome)
            print("distância: " + str(aux_distance))
            if self.minimum_distance_tree > aux_distance:
                self.minimum_distance_tree = aux_distance
                self.minimum_tree_path = aux_path  

    def minimos_sucessivos(self, root):
        minimum_child_distance = 99999
        if root.children:
            print(root.children)
            for child in root.children:
                print(child.distancia + " -- " + minimum_child_distance)
                if child.distancia < minimum_child_distance:
                    minimum_child_distance = child.distancia
                    next_child = child
            self.minimum_next_path.append(next_child.vertice)
            self.minimos_sucessivos(next_child)

    def peso_arestas(self):
        return True

grafo_teste = Grafo()
cidades = ["cidade1","cidade2","cidade3","cidade4"]
x = [1,2,3,4]
y = [1,2,3,4]

for i in range(0,4):
    grafo_teste.add_vertice(Vertice(cidades[i],i,x[i],y[i]))

for i in range(0,4):
    for j in range(i,4):
        if i != j:
            grafo_teste.add_aresta(i,j,random.random()*100)

for v in grafo_teste.vertices:
    if v.id == 0:
        root = grafo_teste.criar_arvore(v)

grafo_teste.construir_arvore(root)
grafo_teste.fechar_ciclo(root, root)

root.print_tree()

grafo_teste.print_grafo()
grafo_teste.caminho_minimo_arvore(root, 0, [], root)
for v in grafo_teste.vertices:
    if v.id == 0:
        grafo_teste.minimum_tree_path.insert(0,v)
for vertice in grafo_teste.minimum_tree_path:
    print(vertice.nome)

print("----------")
grafo_teste.minimos_sucessivos(root)
for v in grafo_teste.vertices:
    if v.id == 0:
        grafo_teste.minimum_next_path.insert(0,v)
for vertice in grafo_teste.minimum_next_path:
    print(vertice.nome)
