#include "Graph.h"

Graph::Graph(int numVertices) : table(numVertices){}

void Graph::addEdge(string source, string destination, int weight) {
	for (int i = 0; i < table.size(); i++) {
		if (table[i].first == source) {
			table[i].second.push_back({ destination, weight });
			break;
		}
		else if (table[i].first.empty()) {
			table[i].first = source;
			table[i].second.push_back({ destination, weight });
			break;
		}
	}
}

void Graph::printGraph() {
	for (int i = 0; i < table.size(); i++) {
		cout << "Вершина " << table[i].first << ":";
		for (auto edge : table[i].second) {
			cout << " (" << edge.destination << ", " << edge.weight << ")";
		}
		cout << endl;
	}
}

vector<pair<string, int>> Graph::bellmanFord(string source) {
	vector<pair<string, int>> distances;
	for (int i = 0; i < table.size(); i++) {
		if (table[i].first == source) {
			distances.push_back({ table[i].first, 0 });
		}
		else {
			distances.push_back({ table[i].first, INF });
		}
	}
	//релаксация ребер
	for (int i = 0; i < table.size() - 1; i++) {
		for (int j = 0; j < table.size(); j++) {
			for (int k = 0; k < table[j].second.size(); k++) {
				int d, w = table[j].second[k].weight;
				for (int u = 0; u < distances.size(); u++) {
					if (distances[u].first == table[j].second[k].destination) {
						d = u;
						break;
					}
				}				
				if (distances[j].second != INF && distances[j].second + w < distances[d].second) {
					distances[d].second = distances[j].second + w;
				}
			}
		}
	}
	//проверка на наличие отрицательных циклов
	for (int i = 0; i < table.size(); i++) {
		for (int j = 0; j < table[i].second.size(); j++) {
			int d, w = table[i].second[j].weight;
			for (int k = 0; k < distances.size(); k++) {
				if (distances[k].first == table[i].second[j].destination) {
					d = k;
					break;
				}
			}
			if (distances[i].second != INF && distances[i].second + w < distances[d].second) {
				cout << "Граф содержит отрицательный цикл!" << endl;
				return vector<pair<string, int>>();
			}
		}
	}
	return distances;
}