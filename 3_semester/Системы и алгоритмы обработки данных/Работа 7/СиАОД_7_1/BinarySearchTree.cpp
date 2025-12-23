#include "BinarySearchTree.h"

BinarySearchTree::BinarySearchTree() {
	root = nullptr;
}

void BinarySearchTree::insert(string data) {
	root = insert(root, data);
}

Node* BinarySearchTree::insert(Node* node, string data) {
    if (node == nullptr) {
        return new Node(data);
    }
    if (data < node->data) {
        node->left = insert(node->left, data);
    }
    else if (data > node->data) {
        node->right = insert(node->right, data);
    }
    return node;
}

void BinarySearchTree::preorder() {
    preorder(root);
    cout << endl;
}

void BinarySearchTree::preorder(Node* node) {
    if (node != nullptr) {
        cout << node->data << " ";
        preorder(node->left);
        preorder(node->right);
    }
}

void BinarySearchTree::inorder() {
    inorder(root);
    cout << endl;
}

void BinarySearchTree::inorder(Node* node) {
    if (node != nullptr) {
        inorder(node->left);
        cout << node->data << " ";
        inorder(node->right);
    }
}

double BinarySearchTree::average() {
    if (root == nullptr) {
        return 0;
    }
    int sum = sumNodes(root);
    int count = countNodes(root);
    return (double)sum / count;
}

int BinarySearchTree::sumNodes(Node* node) {
    if (node == nullptr) {
        return 0;
    }
    return node->data.length() + sumNodes(node->left) + sumNodes(node->right);
}

int BinarySearchTree::countNodes(Node* node) {
    if (node == nullptr) {
        return 0;
    }
    return 1 + countNodes(node->left) + countNodes(node->right);
}

int BinarySearchTree::pathLength(string target) {
    return pathLength(root, target, 0);
}

int BinarySearchTree::pathLength(Node* node, string target, int length) {
    if (node == nullptr) {
        return -1;
    }
    if (node->data == target) {
        return length;
    }
    int leftLength = pathLength(node->left, target, length + 1);
    int rightLength = pathLength(node->right, target, length + 1);
    if (leftLength != -1) {
        return leftLength;
    }
    else if (rightLength != -1) {
        return rightLength;
    }
    return -1;
}