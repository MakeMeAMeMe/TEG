parametrosCompilacao=-Wall -o3 -g -lgvc -lcgraph -lcdt
execName=busca
graphFolder=graph/
buildFolder=build/
graphvizFolder=graphimage/
imgGraphFolder=img_graph/
imgTreeFolder=img_tree/
treeFolder=tree/

all: check_build_folder compile

compile: main.o graph.o graphviz.o node.o path.o
	g++ $(buildFolder)main.o $(buildFolder)graph.o $(buildFolder)node.o $(buildFolder)graphviz.o $(buildFolder)path.o $(parametrosCompilacao) -o $(execName)

main.o: main.cpp
	g++ -c main.cpp $(parametrosCompilacao) -o $(buildFolder)main.o

graph.o: $(graphFolder)graph.cpp $(graphFolder)graph.hpp
	g++ -c $(graphFolder)graph.cpp $(parametrosCompilacao) -o $(buildFolder)graph.o

node.o: $(graphFolder)node.cpp $(graphFolder)node.hpp
	g++ -c $(graphFolder)node.cpp $(parametrosCompilacao) -o $(buildFolder)node.o

graphviz.o: $(graphvizFolder)graphviz.cpp $(graphvizFolder)graphviz.hpp
	g++ -c $(graphvizFolder)graphviz.cpp $(parametrosCompilacao) -o $(buildFolder)graphviz.o

path.o: $(treeFolder)path.cpp $(treeFolder)path.hpp
	g++ -c $(treeFolder)path.cpp $(parametrosCompilacao) -o $(buildFolder)path.o

clear: remove_build_folder
	rm $(execName)

check_build_folder:
	mkdir -p $(buildFolder)
	mkdir -p $(imgGraphFolder)
	mkdir -p $(imgTreeFolder)

remove_build_folder:
	rm $(buildFolder)*.o
	rmdir $(buildFolder)
