#include <iostream>

using namespace std;

void delFirstMetod(int* x, int& n, int key, int& sravn, int& del)
{
	int i = 0;
	while (i < n) {
		sravn++;
		if (x[i] == key) {
			for (int j = i; j < n - 1; j++) {
				sravn++;
				x[j] = x[j + 1];
				del++;
			}
			sravn++;
			n--;
		}
		else {
			i++;
		}
		sravn++;
	}
	sravn++;
}

void delOtherMetod(int* x, int& n, int key, int& sravn, int& del)
{
	int j = 0;
	for (int i = 0; i < n; i++) {
		sravn++;
		x[j] = x[i];
		del++;
		if (x[i] != key) {
			j++;
		}
		sravn++;
	}
	sravn++;
	n = j;
}

void mass_input(int* x, int n) //заполнение случайными числами
{
	srand(time(0));
	for (int i = 0; i < n; i++) {
		x[i] = rand() % 5;
	}
}

void output(int* x, int n) //вывод массива на экран
{
	for (int i = 0; i < n; i++) {
		cout << x[i] << " ";
	}
	cout << endl;
}

int main() {
	setlocale(LC_ALL, "rus");
	int n, key, sravn = 0, del = 0;
	cout << "Введите n: ";
	cin >> n;
	cout << "Введите key: ";
	cin >> key;
	int* x = new int[n];
	mass_input(x, n);
	cout << "Исходный массив: ";
	output(x, n);
	//delFirstMetod(x, n, key, sravn, del);
	delOtherMetod(x, n, key, sravn, del);
	cout << "Результат удаления: ";
	output(x, n);
	cout << "Колличество сравнений: " << sravn << endl;
	cout << "Колличество перемещений: " << del << endl;
	delete[] x;
	cout << "int: \t\t" << sizeof(int) << "bytes" << endl;
	cout << "char: \t\t" << sizeof(char) << "bytes" << endl;
	cout << "bool: \t\t" << sizeof(bool) << "bytes" << endl;
	cout << "float: \t\t" << sizeof(float) << "bytes" << endl;
	cout << "double: \t" << sizeof(double) << "bytes" << endl;
	cout << "int*: \t\t" << sizeof(int*) << "bytes" << endl;
	cout << "long long: \t" << sizeof(long long) << "bytes" << endl;
	cout << "long double: \t" << sizeof(long double) << "bytes" << endl;
}