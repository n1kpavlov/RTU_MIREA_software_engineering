#include <iostream>
#include <iomanip>

using namespace std;

void input(int** matrix, int n)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = rand() % 10;
        }
    }
}

void output(int** matrix, int n)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << setw(3) << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void multiply(int** matrix_A, int** matrix_B, int** matrix_C, int n, int& count)
{
    for (int i = 0; i < n; i++) {
        count++;
        for (int j = 0; j < n; j++) {
            count++;
            for (int k = 0; k < n; k++) {
                count++;
                matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j];
                count++;
            }
            count++;
        }
        count++;
    }
    count++;
}

int main() {
	setlocale(LC_ALL, "rus");
	int n, count = 0;
	cout << "Введите размерность квадратной матрицы: ";
	cin >> n;
    int** matrix_A = new int* [n];
    int** matrix_B = new int* [n];
    int** matrix_C = new int* [n];
    for (int i = 0; i < n; i++) {
        matrix_A[i] = new int[n];
        matrix_B[i] = new int[n];
        matrix_C[i] = new int[n] {0};
    }
    srand(time(0));
    input(matrix_A, n);
    input(matrix_B, n);
    cout << "Исходная матрица A:" << endl;
    output(matrix_A, n);
    cout << "Исходная матрица B:" << endl;
    output(matrix_B, n);
    multiply(matrix_A, matrix_B, matrix_C, n, count);
    cout << "Произведение матриц:" << endl;
    output(matrix_C, n);
    cout << "Сложность алгоритма: " << count << endl;
    for (int i = 0; i < n; i++) {
        delete[] matrix_A[i];
        delete[] matrix_B[i];
        delete[] matrix_C[i];
    }
    delete[] matrix_A;
    delete[] matrix_B;
    delete[] matrix_C;
}