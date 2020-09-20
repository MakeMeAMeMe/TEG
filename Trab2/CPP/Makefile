parametrosCompilacao=-Wall -o3 -g -lgvc -lcgraph -lcdt
execName=minPath
graphFolder=graph/
buildFolder=build/
graphvizFolder=graphimage/
imgGraphFolder=img_graph/
imgTreeFolder=img_tree/
methodsFolder=methods/

all: check_build_folder compile

compile: main.o graph.o graphviz.o node.o path.o min.o ord.o
	g++ $(buildFolder)main.o $(buildFolder)graph.o $(buildFolder)node.o $(buildFolder)ord.o $(buildFolder)graphviz.o $(buildFolder)path.o $(buildFolder)min.o $(parametrosCompilacao) -o $(execName)

main.o: main.cpp
	g++ -c main.cpp $(parametrosCompilacao) -o $(buildFolder)main.o

graph.o: $(graphFolder)graph.cpp $(graphFolder)graph.hpp
	g++ -c $(graphFolder)graph.cpp $(parametrosCompilacao) -o $(buildFolder)graph.o

node.o: $(graphFolder)node.cpp $(graphFolder)node.hpp
	g++ -c $(graphFolder)node.cpp $(parametrosCompilacao) -o $(buildFolder)node.o

graphviz.o: $(graphvizFolder)graphviz.cpp $(graphvizFolder)graphviz.hpp
	g++ -c $(graphvizFolder)graphviz.cpp $(parametrosCompilacao) -o $(buildFolder)graphviz.o

path.o: $(methodsFolder)path.cpp $(methodsFolder)path.hpp
	g++ -c $(methodsFolder)path.cpp $(parametrosCompilacao) -o $(buildFolder)path.o

min.o: $(methodsFolder)min.cpp $(methodsFolder)min.hpp
	g++ -c $(methodsFolder)min.cpp $(parametrosCompilacao) -o $(buildFolder)min.o

ord.o: $(methodsFolder)ord_pesos.cpp $(methodsFolder)ord_pesos.hpp
	g++ -c $(methodsFolder)ord_pesos.cpp $(parametrosCompilacao) -o $(buildFolder)ord.o

clear: remove_build_folder
	rm $(execName)

check_build_folder:
	mkdir -p $(buildFolder)
	mkdir -p $(imgGraphFolder)
	mkdir -p $(imgTreeFolder)

remove_build_folder:
	rm $(buildFolder)*.o
	rmdir $(buildFolder)
