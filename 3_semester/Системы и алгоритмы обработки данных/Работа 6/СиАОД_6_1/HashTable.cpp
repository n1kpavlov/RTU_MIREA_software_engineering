#include "HashTable.h"

int HashTable::hash(long long key) {
    return key % capacity;
}

void HashTable::resize() {
    capacity *= 2;
    vector<list<Product>> newTable(capacity);
    for (auto& list : table) {
        for (auto& product : list) {
            int index = hash(product.code);
            newTable[index].push_back(product);
        }
    }
    table = newTable;
}

HashTable::HashTable(int initialCapacity) : capacity(initialCapacity), size(0) {
    table.resize(capacity);
}

void HashTable::insert(const Product& product) {
    int index = hash(product.code);
    table[index].push_back(product);
    size++;
    /*if (size > capacity / 2) {
        resize();
    }*/
}

void HashTable::remove(long long key) {
    int index = hash(key);
    auto it = table[index].begin();
    while (it != table[index].end()) {
        if (it->code == key) {
            table[index].erase(it);
            size--;
            return;
        }
        it++;
    }
}

Product* HashTable::find(long long key) {
    int index = hash(key);
    for (auto& product : table[index]) {
        if (product.code == key) {
            return &product;
        }
    }
    return nullptr;
}

void HashTable::display() {
    cout << "Хеш-таблица:\n";
    for (int i = 0; i < capacity; i++) {
        cout << "Индекс " << i << ": ";
        if (table[i].empty()) {
            cout << "Пусто\n";
        }
        else {
            for (auto& product : table[i]) {
                cout << "(" << product.code << ", " << product.name << ", " << product.price << ") ";
            }
            cout << "\n";
        }
    }
}