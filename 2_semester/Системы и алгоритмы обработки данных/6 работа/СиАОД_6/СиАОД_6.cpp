#include "List.h"
#include <iostream>

using namespace std;

int main() {
    setlocale(LC_ALL, "rus");
    int k = 1, f = 0, x;
    string s;
    List spisok;
    while (k)
    {
        cout << "Операции:" << endl << "1. Создание списка" << endl << "2. Вставка узла" << endl
            << "3. Удаление узла" << endl << "4. Прямой вывод списка" << endl << "5. Обратный вывод списка" << endl 
            << "6. Вставка нового узла в список, упорядоченный по номеру вагона" << endl
            << "7. Удаление сведений о билетах, пассажиры которых добрались уже до места" << endl 
            << "8. Создание списка по указанной дате отправления" << endl;
        cin >> f;
        switch (f)
        {
        case 1:
            cout << endl << "Введите список:" << endl << endl;
            for (int i = 0; i < 10; i++) {
                spisok.push_back();
            }
            cout << endl << "Полученный список:" << endl << endl;
            spisok.print();
            break;
        case 2:
            cout << endl << "Введите позицию узла: ";
            cin >> x;
            cout << "Введите узел списка:" << endl;
            spisok.add(x);
            cout << endl << "Полученный список:" << endl << endl;
            spisok.print();
            break;
        case 3:
            cout << endl << "Введите позицию узла: ";
            cin >> x;
            spisok.del(x);
            cout << endl << "Полученный список:" << endl << endl;
            spisok.print();
            break;
        case 4:
            cout << endl << "Ваш список:" << endl << endl;
            spisok.print();
            break;
        case 5:
            cout << endl << "Ваш обратный список:" << endl << endl;
            spisok.printback();
            break;
        case 6:
            cout << endl << "Введите узел списка:" << endl;
            spisok.cartsorted();
            cout << endl << "Полученный список:" << endl << endl;
            spisok.print();
            break;
        case 7:
            cout << endl << "Введите дату:" << endl;
            cin >> s;
            spisok.del_reach(s);
            cout << endl << "Полученный список:" << endl << endl;
            spisok.print();
            break;
        case 8:
            cout << endl << "Введите дату:" << endl;
            cin >> s;
            List list;
            list = spisok.list_date(s);
            cout << endl << "Полученный список:" << endl << endl;
            list.print();
            break;
        }
        cout << "Продолжить? (0 - нет, 1 - да): ";
        cin >> k;
        cout << endl;
    }
}
