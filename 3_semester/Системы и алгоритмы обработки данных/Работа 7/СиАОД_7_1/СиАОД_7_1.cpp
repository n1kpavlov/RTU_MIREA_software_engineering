#include "BinarySearchTree.h"

int main()
{
    setlocale(LC_ALL, "rus");
    system("chcp 1251");

    BinarySearchTree tree;
    int choice, length;
    string data, target;

    string test[] = { "50", "30", "70", "20", "40", "60", "80", "10", "25", "45" };
    for (int i = 0; i < 10; i++) {
        tree.insert(test[i]);
    }

    while (true) {
        cout << "\nМеню:\n";
        cout << "1. Вставить узел\n";
        cout << "2. Прямой обход\n";
        cout << "3. Симметричный обход\n";
        cout << "4. Найти среднее арифметическое всех узлов\n";
        cout << "5. Найти длину пути от корня до заданного значения\n";
        cout << "6. Выход\n";
        cout << "Введите ваш выбор: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Введите значение для вставки: ";
            cin >> data;
            tree.insert(data);
            break;
        case 2:
            cout << "Прямой обход: ";// Ожидаемый результат: 50 30 20 10 25 40 45 70 60 80
            tree.preorder();
            break;
        case 3:
            cout << "Симметричный обход: ";// Ожидаемый результат: 10 20 25 30 40 45 50 60 70 80
            tree.inorder();
            break;
        case 4:
            cout << "Среднее арифметическое всех узлов: " << tree.average() << endl;
            break;
        case 5:
            cout << "Введите значение для поиска длины пути: ";
            cin >> target;
            length = tree.pathLength(target);
            if (length == -1) {
                cout << "Узел не найден\n";
            }
            else {
                cout << "Длина пути от корня до " << target << ": " << length << endl;
            }
            break;
        case 6:
            exit(0);
        default:
            cout << "Неверный выбор. Попробуйте снова.\n";
        }
    }
}