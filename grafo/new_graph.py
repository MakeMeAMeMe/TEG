from pathlib import Path
from pprint import pprint

#Parte 1: Implementação
#A.1) matriz adjacência (grafo_1.txt)
def create_matrix_adj(file_path):
    with Path(file_path).open(mode = "r") as graph_file:
        rows = graph_file.readlines()
    matrix = list()
    for i in range(len(rows)):
        matrix.append(list())
        for j in range(len(rows)):
            matrix[i].append(0)
    for i,row in enumerate(rows):
        row = row.strip()
        elements = row.split()
        for element in elements:
            j = int(element)
            matrix[i][j] = 1
    return matrix

#A.2) matriz incidência (grafo_1.txt)
def create_matrix_inc(file_path):
    with Path(file_path).open(mode = "r") as graph_file:
        rows = graph_file.readlines()
    matrix = list()
    for i,row in enumerate(rows):
        row = row.strip()
        elements = row.split()
        for element in elements:
            element = int(element)
            matrix.append(list())
            for j in range(len(rows)):
                matrix[len(matrix)-1].append(0)
            if i==element:
                matrix[len(matrix)-1][i] = -2
            else:
                matrix[len(matrix)-1][i] = 1
                matrix[len(matrix)-1][element] = -1
    return matrix

#B)Calcular grau de cada nó
def calc_degree_vt_adj(matrix, vt, dir = True):
    count = 0
    for i in matrix[vt]:
        if i:
            count += 1
    if dir:
        for i in range(len(matrix)):
            if matrix[i][vt]:
                count += 1

    return count

#Parte II.1: Inserir vertice (utilizando da matriz adjacência)
def insert_vert(matrix):
    for i in range(len(matrix)):
        matrix[i].append(0)
    matrix.append(list())
    matrix[len(matrix)-1].extend([0 for i in range(len(matrix))])

#Parte II.2: Deletar vertice (utilizando da matriz adjacência)
def delete_vert(matrix, vert):
    new_matrix = list()
    for i in range(len(matrix)):
        if i != vert:
            new_matrix.append(list())
            for j in range(len(matrix[i])):
                if j != vert:
                    if i > vert:
                        new_matrix[i-1].append(matrix[i][j])
                    else:
                        new_matrix[i].append(matrix[i][j])
    return new_matrix

#Parte III: Matriz adjacência do complemento do grafo (utilizando da matriz adjência)
def matrix_adj_compl_graph(matrix):
    ...
    compl_matrix = list()
    for i in range(len(matrix)):
        compl_matrix.append(list())
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                compl_matrix[i].append(1)
            elif matrix[i][j]:
                compl_matrix[i].append(0)
    
    return compl_matrix

print("Parte 1 | B) Apresentar matriz adjacência e grau")
matrix = create_matrix_adj("data/grafo_3.txt")
pprint(matrix)
print()
print("Grau dos vertices:")
for i in range(len(matrix)):
    print(i, ": ", calc_degree_vt_adj(matrix,i,False))
print()
print("Parte 1 | C) Grafo direcionado (arquivo: grafo_2.txt)")
matrix = create_matrix_adj("data/grafo_4.txt")
pprint(matrix)
print()
print("Grau dos vertices:")
for i in range(len(matrix)):
    print(i, ": ", calc_degree_vt_adj(matrix,i))