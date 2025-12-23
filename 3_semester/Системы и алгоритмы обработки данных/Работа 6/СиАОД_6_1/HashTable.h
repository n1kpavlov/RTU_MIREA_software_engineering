#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

struct Product {
    long long code;
    string name;
    double price;
};

class HashTable
{  
private:
    vector<list<Product>> table;
    int size;
    int capacity;

    int hash(long long key);
    void resize();

public:
    
    HashTable(int initialCapacity = 10);
    void insert(const Product& product);
    void remove(long long key);
    Product* find(long long key);
    void display();
};

