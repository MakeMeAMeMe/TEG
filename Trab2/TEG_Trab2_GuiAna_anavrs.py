import random
from graphics import *

window = GraphWin("Método das Árvores", 900, 600)
window2 = GraphWin("Método dos mínimos sucessivos", 900, 600)
window3 = GraphWin("Método da ordenação dos peso das arestas", 900, 600)
constantex = 100
constantey = 130

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

class Grafo:
    vertices = list()
    arestas = list()
    minimum_distance_tree = 999999
    minimum_distance_next = 0
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
    
    def sort_aresta_peso(self):
        for i in range (self.arestas.__len__()):
            for j in range (self.arestas.__len__()):
                if self.arestas[i].peso < self.arestas[j].peso:
                    aux = self.arestas[i]
                    self.arestas[i] = self.arestas[j]
                    self.arestas[j] = aux

    def print_grafo(self):
        for v in self.vertices:
            print(v.nome)
            print("----------")
            for u in v.vizinhos:
                print(str(u[0].nome) + ": " + str(u[1]))
    
    def criar_arvore(self, vertice):
        root = TreeNode(vertice,0)
        return root

    def construir_arvore(self, root : TreeNode, origin : TreeNode):
        parent_vertice_list = list()
        for parent in root.parent:
            parent_vertice_list.append(parent.vertice)

        if len(parent_vertice_list) == len(root.vertice.vizinhos):
            for v in root.vertice.vizinhos:
                if v[0] == origin.vertice:
                    tree_v = TreeNode(v[0],v[1])
                    root.add_child(tree_v)
        else:    
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
                    self.construir_arvore(tree_u, origin)
                checker = True
    
    def caminho_minimo_arvore(self, root, aux_distance, aux_path, origin):
        root.color = "red"
        if root.children:
            queue = root.children
            while queue:
                u = queue.pop()
                if u.color == "black":
                    aux_distance += u.distancia
                    node_path = []
                    node_path.extend(aux_path)
                    node_path.append(u.vertice)
                    self.caminho_minimo_arvore(u, aux_distance, node_path, origin)
        else:
            #print("caminho testado:")
            #for v in aux_path:
                #print(v.nome)
            #print("distância: " + str(aux_distance))
            if self.minimum_distance_tree > aux_distance:
                self.minimum_distance_tree = aux_distance
                self.minimum_tree_path = aux_path
        return (self.minimum_distance_tree)
        ##print menor caminho
          

    def minimos_sucessivos(self, root : TreeNode, origin : TreeNode):
        minimum_child_distance = 99999
        parent_vertice_list = list()
        for parent in root.parent:
            parent_vertice_list.append(parent.vertice)

        if len(parent_vertice_list) == len(root.vertice.vizinhos):
            for v in root.vertice.vizinhos:
                if v[0] == origin.vertice:
                    tree_v = TreeNode(v[0],v[1])
                    root.add_child(tree_v)
                    self.minimum_distance_next += v[1]
                    self.minimum_next_path.append(v[0])
        else:    
            queue = []
            queue.extend(root.vertice.vizinhos)
            checker = True
            while queue:
                u = queue.pop()
                for parent in root.parent:
                    if parent.vertice.nome == u[0].nome:
                        checker = False
                if checker:
                    if u[1] < minimum_child_distance:
                        minimum_child_distance = u[1]
                        next_child = u[0]
                        self.minimum_distance_next += u[1]
                checker = True
            tree_u = TreeNode(next_child,minimum_child_distance)
            root.add_child(tree_u)
            self.minimum_next_path.append(tree_u.vertice)
            self.minimos_sucessivos(tree_u,origin)

    def find_parent(self, pos, parent_list):
        if parent_list[pos] == pos:
            return pos
        return self.find_parent(parent_list[pos], parent_list)

    def peso_arestas(self):
        arestas_minimizadas = list()

        parent = list()
        for i in range(self.vertices.__len__()):
            parent.append(i)

        i = 0
        count = 0
        while count != self.vertices.__len__()-1:
            aresta_atual = self.arestas[i]

            count_1 = 0
            count_2 = 0
            for aresta_min in arestas_minimizadas:
                if aresta_atual.pontoA.id == aresta_min.pontoA.id or aresta_atual.pontoA.id == aresta_min.pontoB.id:
                    count_1 += 1
                if aresta_atual.pontoB.id == aresta_min.pontoA.id or aresta_atual.pontoB.id == aresta_min.pontoB.id:
                    count_2 += 1
            if count_1 == 2:
                i += 1
                continue
            if count_2 == 2:
                i += 1
                continue

            ponto_a_parent = self.find_parent(aresta_atual.pontoA.id, parent)
            ponto_b_parent = self.find_parent(aresta_atual.pontoB.id, parent)

            if ponto_a_parent != ponto_b_parent:
                arestas_minimizadas.append(aresta_atual)
                count += 1
                parent[ponto_a_parent] = ponto_b_parent
            i += 1
        return arestas_minimizadas

##incluir distancias

#Desenhar aresta:
def draw_aresta(color, pt1, pt2, w):
    aresta = Line(pt1, pt2)
    aresta.setWidth(2)
    aresta.setOutline(color)
    aresta.draw(w)
#Desenhar ponto:
def draw_ponto(x, y, w):
    pt = Point(x*constantex, y*constantey)
    cir = Circle(pt,5)
    cir.draw(w)

#Definir entradas:
grafo = Grafo()
qtcidades = 10
cidades = ["Joinville","Florianópolis","Blumenau","São José", "Criciúma", "Chapecó", "Itajaí", "Jaguará", "Lages", "Palhoça"]
x = [1,2,3,4,5,6,5,5,3,2]
y = [2,4,1,3.5,1.5,3.5,4,1,4.3,3]
for i in range(qtcidades):
    draw_ponto(x[i], y[i], window)
    draw_ponto(x[i], y[i], window2)
    draw_ponto(x[i], y[i], window3)

for i in range(qtcidades):
    grafo.add_vertice(Vertice(cidades[i],i,x[i],y[i]))
    nome_cidade = Text(Point(x[i]*constantex, y[i]*constantey), str(cidades[i])) 
    nome_cidade.setSize(20)
    nome_cidade.draw(window)
    nome_cidade2 = Text(Point(x[i]*constantex, y[i]*constantey), str(cidades[i])) 
    nome_cidade2.setSize(20)
    nome_cidade2.draw(window2)
    nome_cidade3 = Text(Point(x[i]*constantex, y[i]*constantey), str(cidades[i])) 
    nome_cidade3.setSize(20)
    nome_cidade3.draw(window3)

distancias = [[0,186,104,176,366,512,92,53,312,182],[186,0,152,16,207,556,99,190,229,22],[104,152,0,146,337,477,62,65,223,153],
[176,16,146,0,192,541,91,182,214,9],[366,207,337,192,0,532,281,371,204,185],[512,556,477,541,532,0,530,487,331,534],
[92,99,62,91,281,530,0,97,303,96],[53,190,65,182,371,487,97,0,262,186],[312,229,223,214,204,331,303,262,0,207],
[182,22,153,9,185,534,96,186,207,0]]
for i in range(qtcidades):
    for j in range(qtcidades):
        if i != j:
            grafo.add_aresta(i,j,distancias[i][j])

for i in range(qtcidades):
    for j in range(i,qtcidades):
        if i != j:
            verticea = Vertice(cidades[i],i,x[i],y[i])
            pt1 = Point(verticea.x*constantex, verticea.y*constantey) 
            verticeb = Vertice(cidades[j],j,x[j],y[j])
            pt2 = Point(verticeb.x*constantex, verticeb.y*constantey)
            draw_aresta("black", pt1, pt2, window)
            draw_aresta("black", pt1, pt2, window2)  
            draw_aresta("black", pt1, pt2, window3)         


for v in grafo.vertices:
    if v.id == 0:
        root = grafo.criar_arvore(v)


#MÉTODO DAS ÁRVORES

grafo.construir_arvore(root, root)
aux = grafo.caminho_minimo_arvore(root, 0, [], root)

for v in grafo.vertices:
    if v.id == 0:
        grafo.minimum_tree_path.insert(0,v)

print("")
print("********Algoritmo das Árvores***********")
print("****************************************")
print("Caminho escolhido:")
lista = list()
for vertice in grafo.minimum_tree_path:
    print(vertice.nome)
    lista.append(vertice)
    print()
print("Distancia: " + str(aux))
print("****************************************")
for i in range(qtcidades):
        pt_1 = Point(lista[i].x*constantex, lista[i].y*constantey)
        pt_2 = Point(lista[i+1].x*constantex, lista[i+1].y*constantey)
        draw_aresta("red", pt_1, pt_2, window)

#MÉTODO DOS MÍNIMOS SUCESSIVOS:

print("----------")
min_next_dist = 999999
min_next_path = []
for vertice in grafo.vertices:
    teste_min_suc = grafo.criar_arvore(vertice)
    grafo.minimum_next_path = []
    grafo.minimum_distance_next = 0
    grafo.minimum_next_path.append(teste_min_suc.vertice)
    grafo.minimos_sucessivos(teste_min_suc, teste_min_suc)
    if min_next_dist > grafo.minimum_distance_next:
        min_next_path = []
        min_next_dist = grafo.minimum_distance_next
        min_next_path.extend(grafo.minimum_next_path)


lista_minimos_x = list()
lista_minimos_y = list()
print("")
print("****Algoritmo das minimos sucessivos****")
print("****************************************")
print("Caminho escolhido:")
for vertice in min_next_path:
    print(vertice.nome)
    lista_minimos_x.append(vertice.x)
    lista_minimos_y.append(vertice.y)
    
for i in range(qtcidades):
    pt1_m = Point(lista_minimos_x[i]*constantex, lista_minimos_y[i]*constantey)
    pt2_m = Point(lista_minimos_x[i+1]*constantex, lista_minimos_y[i+1]*constantey)
    draw_aresta("yellow", pt1_m, pt2_m, window2)
  
print("Distância: "+str(grafo.minimum_distance_next))
print("--------------")
print("****************************************")


#MÉTODO DA ORDENAÇÃO DE PESOS DAS ARESTAS
grafo.sort_aresta_peso()
arestas_minimizadas = grafo.peso_arestas()

vertice_1 = Vertice("",0,0,0)
vertice_2 = Vertice("",0,0,0)
for vertice in grafo.vertices:
    count_1 = 0
    for aresta in arestas_minimizadas:
        if vertice == aresta.pontoA or vertice == aresta.pontoB:
            count_1 += 1
    if count_1 == 1:
        vertice_1 = vertice

for vertice in grafo.vertices:
    count_2 = 0
    for aresta in arestas_minimizadas:
        if vertice != vertice_1:
            if vertice == aresta.pontoA or vertice == aresta.pontoB:
                count_2 += 1
    if count_2 == 1:
        vertice_2 = vertice

for aresta in grafo.arestas:
    if aresta.pontoA == vertice_1 and aresta.pontoB == vertice_2:
        arestas_minimizadas.append(aresta)
    elif aresta.pontoB == vertice_1 and aresta.pontoA == vertice_2:
        arestas_minimizadas.append(aresta)

print("")
print("****Algoritmo de ordenação de arestas***")
print("****************************************")
print("Caminho escolhido:")
for aresta in arestas_minimizadas:
    print(str(aresta.pontoA.nome) + "," + str(aresta.pontoB.nome) + ":" + str(aresta.peso))
    pt1_a = Point(aresta.pontoA.x*constantex, aresta.pontoA.y*constantey)
    pt2_a = Point(aresta.pontoB.x*constantex, aresta.pontoB.y*constantey)
    draw_aresta("green", pt1_a,pt2_a , window3)
print("****************************************")

window.getMouse()
window2.getMouse()
window3.getMouse()