#include <ctime>
#include "HashTable.h"

int main()
{
    setlocale(LC_ALL, "rus");
    system("chcp 1251");

    HashTable ht;

    ht.insert({ 123456, "Товар 1", 100.0 });
    ht.insert({ 789012, "Товар 2", 200.5 });
    ht.insert({ 345678, "Товар 3", 150.0 });
    ht.insert({ 601234, "Товар 4", 250.0 });
    ht.insert({ 467890, "Товар 5", 175.5 });

    int choice;
    long long code;
    Product product;
    string name;
    double price;
    Product* foundProduct;

    do {
        cout << "\nМеню:\n";
        cout << "1. Вставить элемент\n";
        cout << "2. Удалить элемент\n";
        cout << "3. Найти элемент\n";
        cout << "4. Вывести таблицу\n";
        cout << "5. Выход\n";
        cout << "Введите ваш выбор: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Введите код товара: ";
            cin >> code;
            cout << "Введите название товара: ";
            getline(cin, name);
            getline(cin, name);
            cout << "Введите цену товара: ";
            cin >> price;
            product = { code, name, price };
            ht.insert(product);
            cout << "Элемент добавлен в таблицу.\n";
            break;
        case 2:
            cout << "Введите код товара для удаления: ";
            cin >> code;
            ht.remove(code);
            cout << "Элемент удален из таблицы.\n";
            break;
        case 3:
            cout << "Введите код товара для поиска: ";
            cin >> code;
            foundProduct = ht.find(code);
            if (foundProduct != nullptr) {
                cout << "Найденный элемент: (" << foundProduct->code << ", " << foundProduct->name << ", " << foundProduct->price << ")\n";
            }
            else {
                cout << "Элемент не найден в таблице.\n";
            }
            break;
        case 4:
            ht.display();
            break;
        case 5:
            cout << "Выход из программы.\n";
            break;
        default:
            cout << "Неверный выбор. Пожалуйста, введите число от 1 до 5.\n";
        }
    } while (choice != 5);

    return 0;
}