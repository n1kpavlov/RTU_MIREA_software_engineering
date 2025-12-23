#ifndef _LIST_H
#define _LIST_H
#include <iostream>

using namespace std;

struct Node {
public:
    string bilet;
    string station;
    int train;
    int cart;
    int seat;
    int cost;
    string date_sale;
    string date_leave;
    string time;

    Node* next = nullptr;
    Node* prev = nullptr;
};

class List {
    Node* first = nullptr;
    Node* last = nullptr;
    int count;
public:
    List();
    void push_behind();
    void push_behind_node(Node* node);
    void push_back();
    void push_back_node(Node* node);
    void add(int pos);
    void del(int pos);
    void add_node(Node* node, int pos);

    void print();
    void printback();

    void cartsorted();
    void del_reach(string date);
    List list_date(string date);

    Node* clone_single(Node* t);
}
;
#endif