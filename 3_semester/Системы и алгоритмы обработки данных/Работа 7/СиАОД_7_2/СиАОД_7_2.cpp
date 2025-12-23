#include "Graph.h"

void main() {
	setlocale(LC_ALL, "rus");
	system("chcp 1251");

	Graph graph(9);
	graph.addEdge("A", "B", 27);
	graph.addEdge("B", "A", 27);
	graph.addEdge("A", "M", 15);
	graph.addEdge("M", "A", 15);
	graph.addEdge("B", "G", 9);
	graph.addEdge("G", "B", 9);
	graph.addEdge("B", "L", 7);
	graph.addEdge("L", "B", 7);
	graph.addEdge("G", "S", 11);
	graph.addEdge("S", "G", 11);
	graph.addEdge("G", "N", 8);
	graph.addEdge("N", "G", 8);
	graph.addEdge("L", "N", 10);
	graph.addEdge("N", "L", 10);
	graph.addEdge("D", "S", 17);
	graph.addEdge("S", "D", 17);
	graph.addEdge("M", "S", 15);
	graph.addEdge("S", "M", 15);
	graph.addEdge("D", "M", 21);
	graph.addEdge("M", "D", 21);
	graph.addEdge("D", "R", 32);
	graph.addEdge("R", "D", 32);
	graph.addEdge("N", "R", 31);
	graph.addEdge("R", "N", 31);
	graph.printGraph();

	/*int numVertices, numEdges;
	cout << "Введите количество вершин: ";
	cin >> numVertices;
	cout << "Введите количество направленных ребер: ";
	cin >> numEdges;
	Graph graph(numVertices);
	string source, destination;
	int weight;
	cout << "Введите ребра в формате <начало> <конец> <вес>: " << endl;
	for (int i = 0; i < numEdges; i++) {
		cin >> source >> destination >> weight;
		graph.addEdge(source, destination, weight);
	}
	graph.printGraph();*/

	string sourceVertex;
	cout << "Введите начальную вершину для поиска кратчайших путей: ";
	cin >> sourceVertex;
	vector<pair<string, int>> distances = graph.bellmanFord(sourceVertex);
	if (!distances.empty()) {
		cout << "Кратчайшие расстояния от вершины " << sourceVertex << ":" << endl;
		for (int i = 0; i < 9; i++) {
			if (distances[i].second == INF) {
				cout << "Вершина " << distances[i].first << ": Достижима" << endl;
			}
			else {
				cout << "Вершина " << distances[i].first << ": " << distances[i].second << endl;
			}
		}
	}
}