#include <iostream>
#include <vector>
#include <ctime>
#pragma comment(linker, "/STACK:67108864")

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

void shell(int* x, long n, long long& sravn, long long& del)
{
	int d = 1;
	while (d < n / 3) {
		d = d * 3 + 1;
	}
	while (d > 0) {
		sravn++;
		for (int i = d; i < n; i++) {
			sravn++;
			int temp = x[i];
			del++;
			int j = i;
			while (j >= d && x[j - d] > temp) {
				sravn += 2;
				x[j] = x[j - d];
				del++;
				j -= d;
			}
			sravn += 2;
			x[j] = temp;
			del++;
		}
		sravn++;
		d = (d - 1) / 3;
	}
	sravn++;
}

int partition(int* arr, long low, long high, long pivot, long long& sravn, long long& del) {
	long i = low;
	long j = low;
	while (i <= high) {
		sravn++;
		if (arr[i] > pivot) {
			i++;
		}
		else {
			long z = arr[i];
			arr[i] = arr[j];
			arr[j] = z;
			del += 3;
			i++;
			j++;
		}
		sravn++;
	}
	sravn++;
	return j - 1;
}

void quickSort(int* arr, long low, long high, long long& sravn, long long& del) {
	if (low < high) {
		sravn++;
		long pivot = arr[high];
		long pos = partition(arr, low, high, pivot, sravn, del);
		quickSort(arr, low, pos - 1, sravn, del);
		quickSort(arr, pos + 1, high, sravn, del);
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
	//shell(x, n, sravn, del);
	quickSort(x, 0, n - 1, sravn, del);
	int end = clock();

	cout << "Отсортированный массив: ";
	output(x, n);
	cout << "Количество сравнений: " << sravn << endl;
	cout << "Количество смещений: " << del << endl;
	cout << "Время работы: " << end - start << " ms" << endl;
	delete[] x;
}