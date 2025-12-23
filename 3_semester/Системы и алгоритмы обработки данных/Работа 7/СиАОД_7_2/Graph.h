#pragma once
#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Edge {
	string destination;
	int weight;
};

class Graph
{
private:
	vector<pair<string, vector<Edge>>> table;

public:
	Graph(int numVertices);
	void addEdge(string sourse, string destination, int weight);
	void printGraph();
	vector<pair<string, int>> bellmanFord(string source);
};