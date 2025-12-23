#include <iostream>

using namespace std;

struct Node
{
    int val;
    Node* next;
    Node(int _val) : val(_val), next(nullptr) {}
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
    void push_behind(int _val) {
        Node* p = new Node(_val);
        if (is_empty()) {
            first = p;
            last = p;
            return;
        }
        p->next = first;
        first = p;
    }
    Node* find(int _val) {
        Node* p = first;
        while (p && p->val != _val)
            p = p->next;
        return (p && p->val == _val) ? p : nullptr;
    }
    void remove_first() {
        if (is_empty())
            return;
        Node* p = first;
        first = p->next;
        delete p;
    }
    void remove_last() {
        if (is_empty())
            return;
        if (first == last) {
            remove_first();
            return;
        }
        Node* p = first;
        while (p->next != last)
            p = p->next;
        p->next = nullptr;
        delete last;
        last = p;
    }
    void remove(int _val) {
        if (is_empty())
            return;
        if (first->val == _val) {
            remove_first();
            return;
        }
        else if (last->val == _val) {
            remove_last();
            return;
        }
        Node* slow = first;
        Node* fast = first->next;
        while (fast && fast->val != _val) {
            fast = fast->next;
            slow = slow->next;
        }
        if (!fast) {
            cout << "Этот элемет не найден" << endl;
            return;
        }
        slow->next = fast->next;
        delete fast;
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

list create(int n) {
    list b;
    int k;
    for (int i = 0; i < n; i++)
    {
        cout << "Введите элемент: ";
        cin >> k;
        b.push_back(k);
    }
    return b;
}

void push_key(list* a, int x, int n)
{
    int k;
    k = x % n;
    a[k].push_back(x);
}

int main()
{
    setlocale(LC_ALL, "rus");
    int k = 1, f = 0, x, n, i = 0;
    cout << "Введите количество списков в массиве: ";
    cin >> n;
    list* a = new list[n];
    while (k)
    {
        cout << "Выбранный список: " << i + 1 << endl << "Операции:" << endl << "1. Добавить элемент на первую позицию" << endl 
        << "2. Удалить элемент" << endl << "3. Создать список вручную" << endl << "4. Использовать готовый список" << endl 
        << "5. Вывести список на экран" << endl << "6. Добавление элемента в один из списков" << endl 
        << "7. Поиск элемента в списке" << endl << "8. Выбрать номер массива для работы" << endl;
        cin >> f;
        switch (f)
        {
        case 1:
            cout << "Введите элемент: ";
            cin >> x;
            a[i].push_behind(x);
            break;
        case 2:
            cout << "Введите элемент: ";
            cin >> x;
            a[i].remove(x);
            break;
        case 3:
            cout << "Введите размер списка: ";
            cin >> x;
            a[i] = create(x);
            break;
        case 4:
            for (int j = 0; j < n; j++) {
                a[j] = list();
                a[j].push_back(1);
                a[j].push_back(2);
                a[j].push_back(3);
                a[j].push_back(4);
                a[j].push_back(5);
            }
            break;
        case 5:
            for (int j = 0; j < n; j++) {
                a[j].print();
            }
            break;
        case 6:
            cout << "Введите элемент: ";
            cin >> x;
            push_key(a, x, n);
            break;
        case 7:
            cout << "Введите элемент: ";
            cin >> x;
            cout << a[i].find(x) << endl;
            break;
        case 8:
            cout << "Выберите номер списка: ";
            cin >> i;
            i--;
            break;
        }
        cout << "Продолжить? (0 - нет, 1 - да): ";
        cin >> k;
        cout << endl;
    }
}