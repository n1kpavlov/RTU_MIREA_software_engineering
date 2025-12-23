#include <iostream>
#include <cstdlib>
#include <Windows.h>
#include <bitset>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");


    //Задание 1
    cout << "Задание 1\n\n";

    unsigned int x = 200, maska_1 = 1;
    cout << "Исходное число: " << x << endl;
    x &= (~(maska_1 << 4));//пятый разряд в 0
    cout << "После преобразования: " << x << endl;
    x = 11;
    maska_1 = 1;
    cout << "Исходное число: " << x << endl;
    x |= (maska_1 << 6);//седьмой разряд в 1
    cout << "После преобразования: " << x << endl << endl;


    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    x = 25;
    const int n = sizeof(int) * 8;
    unsigned maska = (1 << n - 1);
    cout << "Начальный вид маски: " << bitset<n>(maska) << endl;
    cout << "Результат: ";
    for (int i = 1; i <= n; i++) {
        cout << ((x & maska) >> (n - i));
        maska = maska >> 1;
    }
    cout << endl;


    //Задание 2
    cout << "\n\nЗадание 2\n\n";

    unsigned char bitmas = 0;
    cout << "Введите до 8 чисел (значения от 0 до 7, 8 - завершение ввода): ";
    cin >> x;
    while (x != 8) {
        bitmas |= (1 << (7 - x));
        cin >> x;
    }
    cout << "Отсортированны массив:";
    bitset<8> sort = bitmas;
    for (int i = 7; i >= 0; i--) {
        if (sort[i] == 1) {
            cout << " " << 7 - i;
        }
    }

    unsigned long long mas = 0;
    cout << "\nВведите до 64 чисел (значения от 0 до 63, 64 - завершение ввода): ";
    cin >> x;
    while (x != 64) {
        mas |= (static_cast<unsigned long long>(1) << (63 - x));
        cin >> x;
    }
    cout << "Отсортированны массив:";
    bitset<64> srt = mas;
    for (int i = 63; i >= 0; i--) {
        if (srt[i] == 1) {
            cout << " " << 63 - i;
        }
    }

    unsigned char mass[8]{ 0 };
    cout << "\nВведите до 64 чисел (значения от 0 до 63, 64 - завершение ввода): ";
    cin >> x;
    while (x != 64) {
        mass[x / 8] |= (1 << (7 - x % 8));
        cin >> x;
    }
    cout << "Отсортированны массив:";
    for (int i = 0; i < 8; i++) {
        bitset<8> sorting = mass[i];
        for (int j = 7; j >= 0; j--) {
            if (sorting[j] == 1) {
                cout << " " << i * 8 + 7 - j;
            }
        }
    }


    //Задание 3
    cout << "\n\nЗадание 3\n\n";

    long int max = 8 * 1024 * 1024;
    fstream fout("input.txt");
    for (long int i = 1; i < max; i++) {
        fout << max - i << " ";
    }
    fout << max;
    fout.close();

    unsigned int start = clock();
    const long int bitset_size = 8 * 1024 * 1024;
    bitset<bitset_size>* numbers = new bitset<bitset_size>;
    fstream fin("input.txt");
    while (fin >> x) {
        numbers->set(x, 1);
    }
    fin.close();
    fout.open("output.txt");
    for (long int i = 0; i < bitset_size; i++) {
        if (numbers->test(i)) {
            fout << i << " ";
        }
    }
    fout.close();
    unsigned int end = clock();

    cout << "Время работы алгоритма: " << end - start <<  " ms" << endl;
    cout << "Размер массива: " << sizeof(*numbers) << " bytes" << endl;
}