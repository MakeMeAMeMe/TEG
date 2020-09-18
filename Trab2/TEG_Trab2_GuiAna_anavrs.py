import graphics
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
            #print("caminho testado:")
            #for v in aux_path:
                #print(v.nome)
            #print("distância: " + str(aux_distance))
            if self.minimum_distance_tree > aux_distance:
                self.minimum_distance_tree = aux_distance
                self.minimum_tree_path = aux_path
        return (self.minimum_distance_tree)
        ##print menor caminho
          

    def minimos_sucessivos(self, root):
        minimum_child_distance = 99999
        if root.children:
            for child in root.children:
                if child.distancia < minimum_child_distance:
                    minimum_child_distance = child.distancia
                    next_child = child
                    self.minimum_distance_next += child.distancia
            self.minimum_next_path.append(next_child.vertice)
            self.minimos_sucessivos(next_child)

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
grafo_teste = Grafo()
qtcidades = 10
cidades = ["Joinville","Florianópolis","Blumenau","São José", "Criciúma", "Chapecó", "Itajaí", "Jaguará", "Lages", "Palhoça"]
x = [1,2,3,4,5,6,5,5, 3, 2]
y = [2, 4, 1, 3.5, 1.5, 3.5, 4, 1, 4.3, 3]
for i in range(0,qtcidades):
    draw_ponto(x[i], y[i], window)
    draw_ponto(x[i], y[i], window2)
    draw_ponto(x[i], y[i], window3)

for i in range(0,qtcidades):
    grafo_teste.add_vertice(Vertice(cidades[i],i,x[i],y[i]))
    nome_cidade = Text(Point(x[i]*constantex, y[i]*constantey), str(cidades[i])) 
    nome_cidade.setSize(20)
    nome_cidade.draw(window)
    nome_cidade2 = Text(Point(x[i]*constantex, y[i]*constantey), str(cidades[i])) 
    nome_cidade2.setSize(20)
    nome_cidade2.draw(window2)
    nome_cidade3 = Text(Point(x[i]*constantex, y[i]*constantey), str(cidades[i])) 
    nome_cidade3.setSize(20)
    nome_cidade3.draw(window3)

#Joinville
grafo_teste.add_aresta(0, 1, 186) 
grafo_teste.add_aresta(0, 2, 104) 
grafo_teste.add_aresta(0, 3, 176)
grafo_teste.add_aresta(0, 4, 366)
grafo_teste.add_aresta(0, 5, 512)
grafo_teste.add_aresta(0, 6, 92)
grafo_teste.add_aresta(0, 7, 53)
grafo_teste.add_aresta(0, 8, 312)
grafo_teste.add_aresta(0, 9, 182)

#Florianópolis
grafo_teste.add_aresta(1, 0, 186)
grafo_teste.add_aresta(1, 2, 152)
grafo_teste.add_aresta(1, 3, 16)
grafo_teste.add_aresta(1, 4, 207)
grafo_teste.add_aresta(1, 5, 556)
grafo_teste.add_aresta(1, 6, 99)
grafo_teste.add_aresta(1, 7, 190)
grafo_teste.add_aresta(1, 8, 229)
grafo_teste.add_aresta(1, 9, 22)


#Blumenau
grafo_teste.add_aresta(2, 0, 104)
grafo_teste.add_aresta(2, 1, 152)
grafo_teste.add_aresta(2, 3, 146)
grafo_teste.add_aresta(2, 4, 337)
grafo_teste.add_aresta(2, 5, 477)
grafo_teste.add_aresta(2, 6, 62)
grafo_teste.add_aresta(2, 7, 65)
grafo_teste.add_aresta(2, 8, 223)
grafo_teste.add_aresta(2, 9, 153)

#São José
grafo_teste.add_aresta(3, 0, 176)
grafo_teste.add_aresta(3, 1, 16)
grafo_teste.add_aresta(3, 2, 146)
grafo_teste.add_aresta(3, 4, 192)
grafo_teste.add_aresta(3, 5, 541)
grafo_teste.add_aresta(3, 6, 91)
grafo_teste.add_aresta(3, 7, 182)
grafo_teste.add_aresta(3, 8, 214)
grafo_teste.add_aresta(3, 9, 9)

#Criciúma
grafo_teste.add_aresta(4, 0, 366)
grafo_teste.add_aresta(4, 1, 207)
grafo_teste.add_aresta(4, 2, 337)
grafo_teste.add_aresta(4, 3, 192)
grafo_teste.add_aresta(4, 5, 532)
grafo_teste.add_aresta(4, 6, 281)
grafo_teste.add_aresta(4, 7, 371)
grafo_teste.add_aresta(4, 8, 204)
grafo_teste.add_aresta(4, 9, 185)

#Chapecó
grafo_teste.add_aresta(5, 0, 512)
grafo_teste.add_aresta(5, 1, 556)
grafo_teste.add_aresta(5, 2, 477)
grafo_teste.add_aresta(5, 3, 541)
grafo_teste.add_aresta(5, 4, 532)
grafo_teste.add_aresta(5, 6, 530)
grafo_teste.add_aresta(5, 7, 487)
grafo_teste.add_aresta(5, 8, 331)
grafo_teste.add_aresta(5, 9, 534)

#Itajaí
grafo_teste.add_aresta(6, 0, 92)
grafo_teste.add_aresta(6, 1, 99)
grafo_teste.add_aresta(6, 2, 62)
grafo_teste.add_aresta(6, 3, 91)
grafo_teste.add_aresta(6, 4, 281)
grafo_teste.add_aresta(6, 5, 530)
grafo_teste.add_aresta(6, 7, 97)
grafo_teste.add_aresta(6, 8, 303)
grafo_teste.add_aresta(6, 9, 96)

#Jaguará
grafo_teste.add_aresta(7, 0, 53)
grafo_teste.add_aresta(7, 1, 190)
grafo_teste.add_aresta(7, 2, 65)
grafo_teste.add_aresta(7, 3, 182)
grafo_teste.add_aresta(7, 4, 371)
grafo_teste.add_aresta(7, 5, 487)
grafo_teste.add_aresta(7, 6, 97)
grafo_teste.add_aresta(7, 8, 262)
grafo_teste.add_aresta(7, 9, 186)

#Lages
grafo_teste.add_aresta(8, 0, 312)
grafo_teste.add_aresta(8, 1, 229)
grafo_teste.add_aresta(8, 2, 223)
grafo_teste.add_aresta(8, 3, 214)
grafo_teste.add_aresta(8, 4, 204)
grafo_teste.add_aresta(8, 5, 331)
grafo_teste.add_aresta(8, 6, 303)
grafo_teste.add_aresta(8, 7, 262)
grafo_teste.add_aresta(8, 9, 207)

#Palhoça
grafo_teste.add_aresta(9, 0, 182)
grafo_teste.add_aresta(9, 1, 22)
grafo_teste.add_aresta(9, 2, 153)
grafo_teste.add_aresta(9, 3, 9)
grafo_teste.add_aresta(9, 4, 185)
grafo_teste.add_aresta(9, 5, 534)
grafo_teste.add_aresta(9, 6, 96)
grafo_teste.add_aresta(9, 7, 186)
grafo_teste.add_aresta(9, 8, 207)


for i in range(0,qtcidades):
    for j in range(i,qtcidades):
        if i != j:
            print(str(j) + str(i))
            verticea = Vertice(cidades[i],i,x[i],y[i])
            pt1 = Point(verticea.x*constantex, verticea.y*constantey) 
            verticeb = Vertice(cidades[j],j,x[j],y[j])
            pt2 = Point(verticeb.x*constantex, verticeb.y*constantey)
            draw_aresta("black", pt1, pt2, window)
            draw_aresta("black", pt1, pt2, window2)  
            draw_aresta("black", pt1, pt2, window3)         


for v in grafo_teste.vertices:
    if v.id == 0:
        root = grafo_teste.criar_arvore(v)


#MÉTODO DAS ÁRVORES

grafo_teste.construir_arvore(root)
grafo_teste.fechar_ciclo(root, root)
root.print_tree()
aux = grafo_teste.caminho_minimo_arvore(root, 0, [], root)

for v in grafo_teste.vertices:
    if v.id == 0:
        grafo_teste.minimum_tree_path.insert(0,v)

print("")
print("********Algoritmo das Árvores***********")
print("****************************************")
print("Caminho escolhido:")
lista = list()
for vertice in grafo_teste.minimum_tree_path:
    print(vertice.nome)
    lista.append(vertice)
    print()
print("Distancia: " + str(aux))
print("****************************************")
for i in range(0,qtcidades):
        pt_1 = Point(lista[i].x*constantex, lista[i].y*constantey)
        pt_2 = Point(lista[i+1].x*constantex, lista[i+1].y*constantey)
        draw_aresta("red", pt_1, pt_2, window)

#MÉTODO DOS MÍNIMOS SUCESSIVOS:

print("----------")
min_next_dist = 999999
min_next_path = []
for vertice in grafo_teste.vertices:
    teste_min_suc = grafo_teste.criar_arvore(vertice)
    grafo_teste.construir_arvore(teste_min_suc)
    grafo_teste.fechar_ciclo(teste_min_suc, teste_min_suc)
    grafo_teste.minimum_next_path = []
    grafo_teste.minimum_distance_next = 0
    grafo_teste.minimos_sucessivos(teste_min_suc)
    if min_next_dist > grafo_teste.minimum_distance_next:
        min_next_path = []
        min_next_path.append(vertice)
        min_next_dist = grafo_teste.minimum_distance_next
        min_next_path.extend(grafo_teste.minimum_next_path)


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
    
for i in range(0,qtcidades):
    pt1_m = Point(lista_minimos_x[i]*constantex, lista_minimos_y[i]*constantey)
    pt2_m = Point(lista_minimos_x[i+1]*constantex, lista_minimos_y[i+1]*constantey)
    draw_aresta("yellow", pt1_m, pt2_m, window2)
  
print("Distância: "+str(grafo_teste.minimum_distance_next))
print("--------------")
print("****************************************")


#MÉTODO DA ORDENAÇÃO DE PESOS DAS ARESTAS
grafo_teste.sort_aresta_peso()
arestas_minimizadas = grafo_teste.peso_arestas()

vertice_1 = Vertice("",0,0,0)
vertice_2 = Vertice("",0,0,0)
for vertice in grafo_teste.vertices:
    count_1 = 0
    for aresta in arestas_minimizadas:
        if vertice == aresta.pontoA or vertice == aresta.pontoB:
            count_1 += 1
    if count_1 == 1:
        vertice_1 = vertice

for vertice in grafo_teste.vertices:
    count_2 = 0
    for aresta in arestas_minimizadas:
        if vertice != vertice_1:
            if vertice == aresta.pontoA or vertice == aresta.pontoB:
                count_2 += 1
    if count_2 == 1:
        vertice_2 = vertice

for aresta in grafo_teste.arestas:
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