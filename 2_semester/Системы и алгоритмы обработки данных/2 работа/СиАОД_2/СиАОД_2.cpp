#include <iostream>
#include <ctime>

using namespace std;

void mass_input(int* x, long n)
{
	srand(time(0));
	for (int i = 0; i < n; i++) {
		x[i] = rand() % 10;
	}
	/*for (int i = 0; i < n; i++) {
		x[i] = i;
	}*/
	/*for (int i = 0; i < n; i++) {
		x[i] = n - i;
	}*/
}

void output(int* x, long n)
{
	for (int i = 0; i < n; i++) {
		cout << x[i] << " ";
	}
	cout << endl;
}

void bubble(int* x, long n, long long& sravn, long long& del)
{
	for (long i = 0; i < n - 1; i++) {
		sravn++;
		for (long j = i + 1; j < n; j++) {
			sravn++;
			if (x[i] > x[j]) {
				int k = x[i];
				x[i] = x[j];
				x[j] = k;
				del += 3;
			}
			sravn++;
		}
		sravn++;
	}
	sravn++;
}

void insertion(int* x, long n, long long& sravn, long long& del)
{
	for (long i = 1; i < n; i++) {
		sravn++;
		int k = x[i];
		long j = i - 1;
		while (j >= 0 && x[j] > k) {
			sravn++;
			x[j + 1] = x[j];
			del++;
			j--;
		}
		sravn++;
		x[j + 1] = k;
		del++;
	}
	sravn++;
}

int main()
{
    setlocale(LC_ALL, "rus");
    long n;
	long long sravn = 0, del = 0;
    cout << "Введите размер массива: ";
    cin >> n;
    int* x = new int[n];
    mass_input(x, n);
	cout << "Исходный массив: ";
	output(x, n);
	int start = clock();
	//bubble(x, n, sravn, del);
	insertion(x, n, sravn, del);
	int end = clock();
	cout << "Отсортированный массив: ";
	output(x, n);
	cout << "Количество сравнений: " << sravn << endl;
	cout << "Количество смещений: " << del << endl;
	cout << "Время работы: " << end - start << " ms" << endl;
}