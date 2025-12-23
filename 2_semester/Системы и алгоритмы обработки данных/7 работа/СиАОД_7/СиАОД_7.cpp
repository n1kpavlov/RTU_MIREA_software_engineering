#include <iostream>
#include <string>

using namespace std;

struct Node
{
    int val;
    Node* next;
    Node(char _val) : val(_val), next(nullptr) {}
};

struct list
{
    Node* first;
    Node* last;
    list() : first(nullptr), last(nullptr) {}

    bool is_empty()
    {
        return first == nullptr;
    }
    void push_back(int _val) {
        Node* p = new Node(_val);
        if (is_empty()) {
            first = p;
            last = p;
            return;
        }
        last->next = p;
        last = p;
    }
    void print() {
        if (is_empty()) return;
        Node* p = first;
        while (p) {
            cout << p->val << " ";
            p = p->next;
        }
        cout << endl;
    }
};

void del(Node*& first, char key)
{
    if (first == nullptr)
        return;
    if (first->val == key) {
        Node* temp = first;
        first = first->next;
        delete temp;
        del(first, key);
    }
    else {
        del(first->next, key);
    }
}

bool Palindrome(string str)
{
    int low = 0;
    int high = str.length() - 1;
    while (low < high) {
        if (str[low] != str[high]) {
            return false;
        }
        low++;
        high--;
    }
    return true;
}

bool Palindrome_recursion(string str, int low, int high)
{
    if (low >= high) {
        return true;
    }
    if (str[low] != str[high]) {
        return false;
    }
    return Palindrome_recursion(str, low + 1, high - 1);
}

int main()
{
    setlocale(LC_ALL, "rus");

    cout << "Задание №1" << endl << endl;
    cout << "Введите строку: ";
    string str;
    getline(cin, str);
    cout << "Введенная строка: " << str << endl;
    int len = str.length();
    cout << "Результат итерационного алгоритма: ";
    if (Palindrome(str)) {
        cout << "Палиндром" << endl;
    }
    else {
        cout << "Не палиндром" << endl;
    }
    cout << "Результат рекурсивного алгоритма: ";
    if (Palindrome_recursion(str, 0, len - 1)) {
        cout << "Палиндром" << endl;
    }
    else {
        cout << "Не палиндром" << endl;
    }

    cout << endl << "Задание №2" << endl << endl;
    int key = 1;
    list a;
    for (int i = 0; i < 5; i++) {
        a.push_back(1);
    }
    for (int i = 0; i < 7; i++) {
        a.push_back(2);
    }
    for (int i = 0; i < 3; i++) {
        a.push_back(1);
    }
    for (int i = 0; i < 3; i++) {
        a.push_back(5);
    }
    for (int i = 0; i < 2; i++) {
        a.push_back(4);
    }
    a.push_back(1);
    cout << "Удаляемое значение: " << key << endl;
    cout << "Исходный список: ";
    a.print();
    cout << "Полученный список: ";
    del(a.first, key);
    a.print();
}