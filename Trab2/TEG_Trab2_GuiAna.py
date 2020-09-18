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

    def construir_arvore(self, root, origin):
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
        
    #def fechar_ciclo(self, root, origin):
    #    root.color = "red"
    #    queue = []
    #    queue.extend(root.children)
    #    if root.children:
    #        while queue:
    #            u = queue.pop()
    #            if u.color == "black": 
    #                self.fechar_ciclo(u, origin)
    #    else:
    #        for v in root.vertice.vizinhos:
    #            if v[0] == origin.vertice:
    #                tree_v = TreeNode(v[0],v[1])
    #                tree_v.color = "red"
    #                root.add_child(tree_v)
    #
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


grafo_teste = Grafo()
cidades = ["cidade1","cidade2","cidade3","cidade4","cidade5"]
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

grafo_teste.construir_arvore(root, root)

root.print_tree()

grafo_teste.print_grafo()
#grafo_teste.caminho_minimo_arvore(root, 0, [], root)
#for v in grafo_teste.vertices:
#    if v.id == 0:
#        grafo_teste.minimum_tree_path.insert(0,v)
#for vertice in grafo_teste.minimum_tree_path:
#    print(vertice.nome)
###graphics
#print("----------")
#min_next_dist = 999999
#min_next_path = []
#for vertice in grafo_teste.vertices:
#    teste_min_suc = grafo_teste.criar_arvore(vertice)
#    grafo_teste.construir_arvore(teste_min_suc, teste_min_suc)
#    grafo_teste.minimum_next_path = []
#    grafo_teste.minimum_distance_next = 0
#    grafo_teste.minimos_sucessivos(teste_min_suc)
#    if min_next_dist > grafo_teste.minimum_distance_next:
#        min_next_path = []
#        min_next_path.append(vertice)
#        min_next_dist = grafo_teste.minimum_distance_next
#        min_next_path.extend(grafo_teste.minimum_next_path)
#
#
##
#for vertice in min_next_path:
#    print(vertice.nome)
#print("--------------")
#
#grafo_teste.sort_aresta_peso()
#arestas_minimizadas = grafo_teste.peso_arestas()
#
#vertice_1 = Vertice("",0,0,0)
#vertice_2 = Vertice("",0,0,0)
#for vertice in grafo_teste.vertices:
#    count_1 = 0
#    for aresta in arestas_minimizadas:
#        if vertice == aresta.pontoA or vertice == aresta.pontoB:
#            count_1 += 1
#    if count_1 == 1:
#        vertice_1 = vertice
#
#for vertice in grafo_teste.vertices:
#    count_2 = 0
#    for aresta in arestas_minimizadas:
#        if vertice != vertice_1:
#            if vertice == aresta.pontoA or vertice == aresta.pontoB:
#                count_2 += 1
#    if count_2 == 1:
#        vertice_2 = vertice
#
#for aresta in grafo_teste.arestas:
#    if aresta.pontoA == vertice_1 and aresta.pontoB == vertice_2:
#        arestas_minimizadas.append(aresta)
#    elif aresta.pontoB == vertice_1 and aresta.pontoA == vertice_2:
#        arestas_minimizadas.append(aresta)
#
#for aresta in arestas_minimizadas:
#    print(str(aresta.pontoA.nome) + "," + str(aresta.pontoB.nome) + ":" + str(aresta.peso))
#