from pathlib import Path
from pprint import pprint

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

def create_matrix_inc(file_path):
    with Path(file_path).open(mode = "r") as graph_file:
        rows = graph_file.readlines()
    #pprint(rows)
    matrix = list()
    for i,row in enumerate(rows):
        row = row.strip()
        elements = row.split()
        #pprint(elements)
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

def insert_vert(matrix):
    for i in range(len(matrix)):
        matrix[i].append(0)
    matrix.append(list())
    matrix[len(matrix)-1].extend([0 for i in range(len(matrix))])

def delete_vert(matrix, vert):
    new_matrix = list()
    for i in range(len(matrix)):
        if i != vert:
            new_matrix.append(list())
            for j in range(len(matrix[i])):
                if j != vert:
                    new_matrix[i].append(matrix[i][j])

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

#matrix = create_matrix_adj()
#create_matrix_inc()
#pprint(calc_degree_vt_adj(matrix, 5))

pprint("Matriz não direncionada")
matrix = create_matrix_adj("data/grafo_3.txt")
insert_vert(matrix)
compl = matrix_adj_compl_graph(matrix)
pprint(matrix)
pprint(compl)

#for i in range(len(matrix)):
#    pprint(calc_degree_vt_adj(matrix,i,False))
##
##pprint("Matriz direcionada")
##matrix = create_matrix_adj("data/grafo_4.txt")
#for i in range(len(matrix)):
#    pprint(calc_degree_vt_adj(matrix,i))