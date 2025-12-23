#pragma once
#include <iostream>
#include <string>

using namespace std;

struct Node {
    string data;
    Node* left, * right;

    Node(string data) {
        this->data = data;
        left = right = nullptr;
    }
};

class BinarySearchTree
{
private:
    Node* root;
    Node* insert(Node* node, string data);
    void preorder(Node* node);
    void inorder(Node* node);
    int sumNodes(Node* node);
    int countNodes(Node* node);
    int pathLength(Node* node, string target, int length);

public:
    BinarySearchTree();
    void insert(string data);
    void preorder();
    void inorder();
    double average();
    int pathLength(string target);
};