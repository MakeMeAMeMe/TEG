from operator import itemgetter
import graphics
import random

class TreeNode:
    def __init__(self, vertice, distancia):
        self.vertice = vertice
        self.distancia = distancia
        self.children = list()
        self.parent = list()
        self.color = "black"

    def add_child(self, child):
        child.parent.append(self.parent)
        child.parent.append(self)
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
        ##vizinho = [vertice, distancia] -> [0] = vert, [1] = dist
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)

class Aresta:
    def __init__(self, pontoA, pontoB, peso):
        self.pontoA = pontoA
        self.pontoB = pontoB
        self.peso = peso
    
    def get_pontoA(self):
        return self.pontoA

##quanto print deuzdoceu vai saber diferenciar o q é o q? pontoA 
class Grafo:
    vertices = list()
    arestas = list()

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
                            v.add_vizinho(u)
                            print(v.vizinhos.__len__())
                            u.add_vizinho(v)
                            self.arestas.append(Aresta(v,u,peso))
                            return True
        else:
            return False

    def print_grafo(self):
        for v in self.vertices:
            print(v.nome)
            print("----------")
            print(v.vizinhos.__len__())
    
    #def criar_arvore(self, vertice):
    #    root = TreeNode(vertice,0)
    #    return root
#
    #def construir_arvore(self, root):
    #    queue = root.vertice.vizinhos
    #    while queue:
    #        ##print(root.vertice.children)
    #        u = queue.pop()
    #        if u[0] not in root.parent:
    #            tree_u = TreeNode(u[0],u[1])
    #            root.add_child(tree_u)
    #            self.construir_arvore(tree_u)
    #    
    #def fechar_ciclo(self, root, origin):
    #    root.color = "red"
    #    queue = root.children
    #    if queue:
    #        while queue:
    #            u = queue.pop()
    #            if u.color == "black": 
    #                self.fechar_ciclo(u, origin) ##distancia de u ate root?
    #    else:
    #        for v in root.vertice.vizinhos:
    #            if v[0] == origin:
    #                tree_v = TreeNode(v[0],v[1])
    #                tree_v.color = "red"
    #                root.add_child(tree_v)
    #
    #def caminho_minimo_arvore(self, root, aux):
    #    min_distance = 99999999
    #    aux_dist = 0
    #    aux_path = aux
    #    min_path = list()
    #    root.color = "blue"
    #    queue = root.children
    #    if queue:
    #        while queue:
    #            u = queue.pop()
    #            if u.color == "red": 
    #                aux_dist += u.distancia
    #                aux_path.append(u.vertice)
    #                self.caminho_minimo_arvore(u, aux_path)
    #    else:
    #        aux_dist += root.distancia
    #        aux_path.append(root.vertice)
    #        if min_distance > aux_dist:
    #            min_distance = aux_dist
    #            min_path = aux_path
    #    
    #    return min_path
    

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

#for v in grafo_teste.vertices:
#    if v.id == 0:
#        print(v.nome)
#        root = grafo_teste.criar_arvore(v)
#
#grafo_teste.construir_arvore(root)
#grafo_teste.fechar_ciclo(root, root)

grafo_teste.print_grafo()
#root.print_tree()
#
#resultado = grafo_teste.caminho_minimo_arvore(root, [])
#for i in range(0,3):
#    print(i)
#    print(resultado[i].nome)