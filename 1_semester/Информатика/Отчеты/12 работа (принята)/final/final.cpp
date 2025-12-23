#include <iostream>
#include <math.h>
#include <ctime>
#include <string>
#include <stdio.h>

using namespace std;

//функция проверки правильности ввода (выбора способа заполнения)
double test_1_or_2()
{
    double x;
    cin >> x;
    while (cin.fail() or cin.eof() or (round(x)!=x) or ((x != 1) and (x != 2))) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Ошибка. Введите 1 или 2: ";
        cin >> x;
    }
    return x;
}

//функция проверки правильности ввода (значение ячеек матрицы)
double test()
{
    double x;
    cin >> x;
    while (cin.fail() or cin.eof() or (x < 0) or (x > 100)) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Ошибка. Введите число из диапазона от 0 до 100: ";
        cin >> x;
    }
    return x;
}

//функция вывода матрицы размера n*m
void output(double** matrix, int n, int m)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%10g", matrix[i][j]);
        }
        cout << endl;
    }
    cout << endl;
}

int main()
{
	setlocale(LC_ALL, "rus");
	const int n = 6;
    //выделение памяти для двумерного масива типа double
    double** matrix = new double* [n];
    for (int j = 0; j < n; j++) {
        matrix[j] = new double[n];
    }
    //выбор способа заполнения матрицы
    cout << "Выберите заполнение матрицы (1 - случайное; 2 - с клавиатуры): ";
    int k;
    k = test_1_or_2();
    switch (k)
    {
    //заполнение матрицы сгенерированными чисами
    case 1:
    {
        srand(time(0));
        int end = 100, start = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = (rand() % (end - start + 1)) + start;
            }
        }
    }
        break;
    //заполнение матрицы с клавиатуры
    case 2:
        cout << "Заполните матрицу числами из диапазона от 0 до 100" << endl;
        for (int i = 0; i < n; i++) {
            cout << "Введите значения " << (i + 1) << " строки:" << endl;
            for (int j = 0; j < n; j++) {
                cout << (j + 1) << " элемент: ";
                matrix[i][j] = test();
            }
        }
        break;
    }
    //вывод на экран введеной (или сгенерированной) матрицы
    cout << "Исходная матрица: " << endl << endl;
    output(matrix, n, n);
    //деление четных строк на нечетные и перезапись матрицы
    for (int i = 0; i < n; i += 2) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                cout << "Ошибка. Обнаружено деление на 0" << endl;
                exit(0);
            }
            else {
                matrix[i / 2][j] = matrix[i + 1][j] / matrix[i][j];
            }
        }
    }
    //вывод матрицы 3х6
    cout << "Полученная матрица 3х6:" << endl << endl;
    output(matrix, n / 2, n);
    //деление четных столбцов на нечетные и перезапись матрицы
    for (int i = 0; i < n / 2; i++) {
        for (int j = 0; j < n; j += 2) {
            if (matrix[i][j] == 0) {
                cout << "Ошибка. Обнаружено деление на 0" << endl;
                exit(0);
            }
            else {
                matrix[i][j / 2] = matrix[i][j + 1] / matrix[i][j];
            }
        }
    }
    //вывод матрицы 3х3
    cout << "Полученная матрица 3х3:" << endl << endl;
    output(matrix, n / 2, n / 2);
    //сортировка столбцов матрицы
    for (int j = 0; j < n / 2; j++) {
        for (int k = 0; k < n / 2 - 1; k++) {
            for (int i = 0; i < n / 2 - k - 1; i++) {
                if (matrix[i][j] > matrix[i + 1][j]) {
                    double x = matrix[i][j];
                    matrix[i][j] = matrix[i + 1][j];
                    matrix[i + 1][j] = x;
                }
            }
        }
    }
    //вывод отсортированной матрицы 3х3
    cout << "Отсортированная матрица 3х3:" << endl << endl;
    output(matrix, n / 2, n / 2);
    //очистка памяти
    for (int j = 0; j < n; j++) {
        delete[] matrix[j];
    }
    delete[] matrix;
}