parametrosCompilacao=-Wall -o3 -g -lgvc -lcgraph -lcdt
execName=busca
graphFolder=graph/
coordFolder=coordinate/
buildFolder=build/
graphvizFolder=graphimage/
imgGraphFolder=img_graph/
imgTreeFolder=img_tree/

all: check_build_folder compile

compile: main.o graph.o graphviz.o node.o edge.o coordinate.o
	g++ $(buildFolder)main.o $(buildFolder)graph.o $(buildFolder)node.o $(buildFolder)coordinate.o $(buildFolder)edge.o $(buildFolder)graphviz.o $(parametrosCompilacao) -o $(execName)

main.o: main.cpp
	g++ -c main.cpp $(parametrosCompilacao) -o $(buildFolder)main.o

graph.o: $(graphFolder)graph.cpp $(graphFolder)graph.hpp
	g++ -c $(graphFolder)graph.cpp $(parametrosCompilacao) -o $(buildFolder)graph.o

node.o: $(graphFolder)node.cpp $(graphFolder)node.hpp
	g++ -c $(graphFolder)node.cpp $(parametrosCompilacao) -o $(buildFolder)node.o

edge.o: $(graphFolder)edge.cpp $(graphFolder)edge.hpp
	g++ -c $(graphFolder)edge.cpp $(parametrosCompilacao) -o $(buildFolder)edge.o

graphviz.o: $(graphvizFolder)graphviz.cpp $(graphvizFolder)graphviz.hpp
	g++ -c $(graphvizFolder)graphviz.cpp $(parametrosCompilacao) -o $(buildFolder)graphviz.o

coordinate.o: $(coordFolder)coordinate.cpp $(coordFolder)coordinate.hpp
	g++ -c $(coordFolder)coordinate.cpp $(parametrosCompilacao) -o $(buildFolder)coordinate.o

clear: remove_build_folder
	rm $(execName)

check_build_folder:
	mkdir -p $(buildFolder)
	mkdir -p $(imgGraphFolder)
	mkdir -p $(imgTreeFolder)

remove_build_folder:
	rm $(buildFolder)*.o
	rmdir $(buildFolder)
