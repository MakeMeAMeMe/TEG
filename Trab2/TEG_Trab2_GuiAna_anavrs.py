import random
from graphics import GraphWin, Line, Point, Circle, Text

window = GraphWin("Método das Árvores", 900, 600)
window2 = GraphWin("Método dos mínimos sucessivos", 900, 600)
window3 = GraphWin("Método da ordenação dos peso das arestas", 900, 600)
constantex = 100
constantey = 110

class TreeNode:
    def __init__(self, vertice, distancia):
        self.vertice = vertice #elemento do nodo
        self.distancia = distancia #distancia para o pai imediato
        self.children = list() #lista de filhos imediatos
        self.parent = [] #lista de todos os pais
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

    def add_vizinho(self, vizinho): #lista de [vertice,distância até o vertice]
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
    minimum_distance_tree = 999999 #distancia método de árvores
    minimum_distance_next = 0 #distância mínimos sucessivos
    minimum_tree_path = list() #caminho minimo do método de árvores
    minimum_next_path = list() #caminho minimo do método de sucessivos
    minimum_tree_distances_list = list() #lista de distancias método árvoes

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
        for i in range (len(self.arestas)):
            for j in range (len(self.arestas)):
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

        #se o número de pais = número de vizinhos, fechar ciclo
        if len(root.parent) == len(root.vertice.vizinhos):
            for v in root.vertice.vizinhos:
                if v[0] == origin.vertice:
                    tree_v = TreeNode(v[0],v[1])
                    root.add_child(tree_v)
        #se o número de pais != número de vizinhos, continuar a construção
        else:    
            queue = []
            queue.extend(root.vertice.vizinhos)
            checker = True
            while queue:
                u = queue.pop()
                for parent in root.parent:
                    if parent.vertice.nome == u[0].nome: #checar se vertice já é pai
                        checker = False #se sim então não add como filho
                if checker: #se não criar nodo com distância até vertice e add como filho
                    tree_u = TreeNode(u[0],u[1])
                    root.add_child(tree_u)
                    self.construir_arvore(tree_u, origin)
                checker = True
    
    def caminho_minimo_arvore(self, root, aux_distance, aux_path, aux_distance_list, origin):
        root.color = "red" #marcar como visitado
        if root.children: #se tiver filhos continua a percorrer
            queue = root.children
            while queue:
                u = queue.pop()
                if u.color == "black": #entrar se não tiver sido visitado
                    node_distance = 0
                    node_distance = u.distancia + aux_distance #distância até o nodo
                    node_path = []
                    node_path.extend(aux_path)
                    node_path.append(u.vertice) #caminho até o nodo
                    node_dist_list = list()
                    node_dist_list.extend(aux_distance_list)
                    node_dist_list.append(u.distancia)
                    self.caminho_minimo_arvore(u, node_distance, node_path, node_dist_list, origin)
        else: #sem filhos = fim do percurso
            if self.minimum_distance_tree > aux_distance: #compara menor distancia registrada com a do caminho
                self.minimum_distance_tree = aux_distance
                self.minimum_tree_path = aux_path
                self.minimum_tree_distances_list = aux_distance_list
        #self.minimum_tree_distances_list.append(root.distancia
        return (self.minimum_distance_tree)
        

    def minimos_sucessivos(self, root, origin):
        minimum_child_distance = 99999

        #se número de pais = número de vizinhos, fechar ciclo
        if len(root.parent) == len(root.vertice.vizinhos):
            for v in root.vertice.vizinhos:
                if v[0] == origin.vertice:
                    tree_v = TreeNode(v[0],v[1])
                    root.add_child(tree_v)
                    self.minimum_distance_next += v[1]
                    self.minimum_next_path.append(v[0])
        #se número de pais != número de vizinhos, continuar a construir árvore
        else:    
            queue = []
            queue.extend(root.vertice.vizinhos)
            checker = True
            while queue:
                u = queue.pop()
                for parent in root.parent:
                    if parent.vertice.nome == u[0].nome: #checar se vertice já é pai 
                        checker = False #se sim não fazer nada
                if checker: #se não ver se é a menor distância encontrada até o momento
                    if u[1] < minimum_child_distance:
                        minimum_child_distance = u[1]
                        next_child = u[0]
                checker = True
            #criar nodo e continuar a árvore mínima usando o vertice com menor distância não inserido encontrado
            tree_u = TreeNode(next_child,minimum_child_distance)
            root.add_child(tree_u)
            self.minimum_tree_distances_list.append(minimum_child_distance)
            self.minimum_distance_next += minimum_child_distance
            self.minimum_next_path.append(tree_u.vertice)
            self.minimos_sucessivos(tree_u,origin)

    #achar pai absoluto (método das arestas)
    def find_parent(self, pos, parent_list):
        if parent_list[pos] == pos:
            return pos
        return self.find_parent(parent_list[pos], parent_list)

    def peso_arestas(self):
        arestas_minimizadas = list()

        parent = list() #lista inicial de pais absolutos (pai = ele mesmo)
        for i in range(self.vertices.__len__()):
            parent.append(i)

        i = 0 #percorrer arestas
        count = 0 #número de arestas inseridas
        while count != self.vertices.__len__()-1: #número final de arestas = número de vertices - 1
            aresta_atual = self.arestas[i]

            #checar se vertice A ou B na aresta já foi adicionado 2 vezes, se sim pular aresta
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

            #achar pai absoluto do ponto A e do ponto B
            ponto_a_parent = self.find_parent(aresta_atual.pontoA.id, parent)
            ponto_b_parent = self.find_parent(aresta_atual.pontoB.id, parent)
            
            #se o pai absoluto for diferente, não fecha ciclo, inserir aresta
            if ponto_a_parent != ponto_b_parent:
                arestas_minimizadas.append(aresta_atual)
                count += 1
                parent[ponto_a_parent] = ponto_b_parent
            i += 1
            
        return arestas_minimizadas

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
x = [1,1,2.5,4.5,6,6,6,4.5,2.5,1]
y = [1.5,4,0.5,5,1.5,2.7,4,0.5,5,2.7]
for i in range(qtcidades):
    draw_ponto(x[i], y[i], window)
    draw_ponto(x[i], y[i], window2)
    draw_ponto(x[i], y[i], window3)

for i in range(qtcidades):
    grafo.add_vertice(Vertice(cidades[i],i,x[i],y[i]))
    nome_cidade = Text(Point(x[i]*constantex, -10+y[i]*constantey), str(cidades[i])) 
    nome_cidade.setSize(20)
    nome_cidade.draw(window)
    nome_cidade2 = Text(Point(x[i]*constantex, -10+y[i]*constantey), str(cidades[i])) 
    nome_cidade2.setSize(20)
    nome_cidade2.draw(window2)
    nome_cidade3 = Text(Point(x[i]*constantex, -10+y[i]*constantey), str(cidades[i])) 
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


#MÉTODO DAS ÁRVORES

root = grafo.criar_arvore(grafo.vertices[0]) #criar árvore saindo de joinville
grafo.construir_arvore(root, root) #constrói árvore
aux = grafo.caminho_minimo_arvore(root, 0, [],[], root) #calcula distância mínima (e caminho)
grafo.minimum_tree_path.insert(0,root.vertice) #insere cidade inicial
print("")
print("********Algoritmo das Árvores***********")
print("****************************************")
print("Caminho escolhido:")
aux1=0
rotatree_text = Text(Point(750, 80),"Rota:")
rotatree_text.setSize(15)
rotatree_text.setTextColor("black")
rotatree_text.draw(window)
for i in range(qtcidades):
    print(str(i+1) + ": " + grafo.minimum_tree_path[i].nome)
    cidadetree_text = Text(Point(750, 100+aux1), str(grafo.minimum_tree_path[i].nome))
    cidadetree_text.setSize(13)
    cidadetree_text.setTextColor("red")
    cidadetree_text.draw(window) 
    aux1=aux1+20
    distancias_text = Text(Point(750, 100+aux1), str(grafo.minimum_tree_distances_list[i])+"km")
    distancias_text.setSize(13)
    distancias_text.setTextColor("black")
    distancias_text.draw(window) 
    aux1=aux1+20

distancias_text = Text(Point(750, 100+aux1),grafo.minimum_tree_path[0].nome)
distancias_text.setSize(13)
distancias_text.setTextColor("red")
distancias_text.draw(window)

distanciattree_text = Text(Point(750, 530), "Distância: " + str(aux)+ "km")
distanciattree_text.setSize(15)
distanciattree_text.setTextColor("black")
distanciattree_text.draw(window)

print("Distancia: " + str(aux) + " km")
print("****************************************")
for i in range(qtcidades):
        pt_1 = Point(grafo.minimum_tree_path[i].x*constantex, grafo.minimum_tree_path[i].y*constantey)
        pt_2 = Point(grafo.minimum_tree_path[i+1].x*constantex, grafo.minimum_tree_path[i+1].y*constantey)
        draw_aresta("red", pt_1, pt_2, window)

#MÉTODO DOS MÍNIMOS SUCESSIVOS:

print("----------")
min_next_dist = 999999
min_next_path = []
for vertice in grafo.vertices: #testar partindo de todas as cidades
    teste_min_suc = grafo.criar_arvore(vertice) #cria arvore
    grafo.minimum_next_path = [] #zera caminho minimo interno
    grafo.minimum_distance_next = 0 #zera distancia minima interna
    grafo.minimum_next_path.append(teste_min_suc.vertice) #add vertice de partida
    grafo.minimos_sucessivos(teste_min_suc, teste_min_suc) #calcula caminho e dist minima saindo do vertice
    if min_next_dist > grafo.minimum_distance_next: #se caminho menor então caminho é o novo caminho minimo
        min_next_path = []
        min_next_dist = grafo.minimum_distance_next
        min_next_path.extend(grafo.minimum_next_path)

print("")
print("****Algoritmo das minimos sucessivos****")
print("****************************************")
print("Caminho escolhido:")


saux=0
srota_text = Text(Point(750, 80),"Rota:")
srota_text.setSize(15)
srota_text.setTextColor("black")
srota_text.draw(window2)
list_min_sc_dist = list()   
for i in range(qtcidades):    
    for vizinho in min_next_path[i].vizinhos:
        if min_next_path[i+1] == vizinho[0]:
            list_min_sc_dist.append(vizinho[1])
for i in range(qtcidades):
    print(str(i) + ": " + min_next_path[i].nome)
    scidade_text = Text(Point(750, 100+saux),min_next_path[i].nome)
    scidade_text.setSize(13)
    scidade_text.setTextColor("red")
    scidade_text.draw(window2)
    saux=saux+20
    distancias_text = Text(Point(750, 100+saux), str(list_min_sc_dist[i])+"km")
    distancias_text.setSize(13)
    distancias_text.setTextColor("black")
    distancias_text.draw(window2) 
    saux=saux+20

distancias_text = Text(Point(750, 100+saux),min_next_path[0].nome)
distancias_text.setSize(13)
distancias_text.setTextColor("red")
distancias_text.draw(window2)

for i in range(qtcidades):
    pt1_m = Point(min_next_path[i].x*constantex, min_next_path[i].y*constantey)
    pt2_m = Point(min_next_path[i+1].x*constantex, min_next_path[i+1].y*constantey)
    draw_aresta("red", pt1_m, pt2_m, window2)

sdistancia_text = Text(Point(750, 530),"Distância:"+ str(min_next_dist)+"km")
sdistancia_text.setSize(15)
sdistancia_text.setTextColor("black")
sdistancia_text.draw(window2)

print("Distância: " + str(min_next_dist) + " km")
print("--------------")
print("****************************************")

#MÉTODO DA ORDENAÇÃO DE PESOS DAS ARESTAS
grafo.sort_aresta_peso()
arestas_minimizadas = grafo.peso_arestas()

#achar vertices inseridos apenas uma vez e inserir aresta entre eles (fechar ciclo)
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
print("***Algoritmo de ordenação das arestas***")
print("****************************************")
print("Caminho escolhido:")
listaux = list()
for aresta in arestas_minimizadas:
    pt1_a = Point(aresta.pontoA.x*constantex, aresta.pontoA.y*constantey)
    pt2_a = Point(aresta.pontoB.x*constantex, aresta.pontoB.y*constantey)
    draw_aresta("red", pt1_a,pt2_a , window3) 
    listaux.append(aresta.peso)

distancia = 0
for aresta in arestas_minimizadas:
    distancia += aresta.peso

minimum_aresta_path = list()
minimum_aresta_path.append(arestas_minimizadas[0].pontoA)
minimum_aresta_path.append(arestas_minimizadas[0].pontoB)
for i in range(1,11):
    for j in range(1,len(arestas_minimizadas)):
        if arestas_minimizadas[j].pontoA == minimum_aresta_path[i]:
            minimum_aresta_path.append(arestas_minimizadas[j].pontoB)
            arestas_minimizadas.remove(arestas_minimizadas[j])
            break
        elif arestas_minimizadas[j].pontoB == minimum_aresta_path[i]:
            minimum_aresta_path.append(arestas_minimizadas[j].pontoA)
            arestas_minimizadas.remove(arestas_minimizadas[j])
            break
aux=0
rota_text = Text(Point(750, 80),"Rota:")
rota_text.setSize(15)
rota_text.setTextColor("black")
rota_text.draw(window3)
for i in range(qtcidades):
    print(str(i) + ": " + minimum_aresta_path[i].nome)
    cidade_text = Text(Point(750, 100+aux), minimum_aresta_path[i].nome)
    cidade_text.setSize(13)
    cidade_text.setTextColor("red")
    cidade_text.draw(window3) 
    aux=aux+20
    distancias_text = Text(Point(750, 100+aux), str(listaux[i])+"km")
    distancias_text.setSize(13)
    distancias_text.setTextColor("black")
    distancias_text.draw(window3) 
    aux=aux+20

distancias_text = Text(Point(750, 100+saux),minimum_aresta_path[0].nome)
distancias_text.setSize(13)
distancias_text.setTextColor("red")
distancias_text.draw(window3)

distancia_text = Text(Point(750, 530),"Distância:"+ str(distancia)+"km")
distancia_text.setSize(15)
distancia_text.setTextColor("black")
distancia_text.draw(window3)
print("Distância: " + str(distancia) + " km")
print("****************************************")

window.getMouse()
window2.getMouse()
window3.getMouse()