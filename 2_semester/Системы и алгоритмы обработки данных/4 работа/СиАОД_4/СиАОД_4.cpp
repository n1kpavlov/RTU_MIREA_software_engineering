#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <vector>
#include <queue>

using namespace std;

struct Person
{
	string name;
	string surname;
	string birthday;
	int weight;
	int height;
	char gender;
};

void insertion_sort(int* x, int n)
{
	for (int i = 1; i < n; i++) {
		int k = x[i];
		int j = i - 1;
		while (j >= 0 && x[j] > k) {
			x[j + 1] = x[j];
			j--;
		}
		x[j + 1] = k;
	}
}

void insertion_sort_2(Person* person, int n)
{
	for (int i = 1; i < n; i++) {
		int k = person[i].height;
		Person test = person[i];
		int j = i - 1;
		while (j >= 0 && person[j].height > k) {
			person[j + 1] = person[j];
			j--;
		}
		person[j + 1] = test;
	}
}

void first_sort_example(string& A1, string B, string C, string A, int n)
{
	int n1 = 1;
	while (n1 < n) {
		ifstream finA1;
		ofstream foutB, foutC;
		finA1.open(A1);
		foutB.open(B);
		foutC.open(C);
		if (!finA1.is_open() || !foutB.is_open() || !foutC.is_open()) {
			cout << "Ошибка открытия файла" << endl;
			exit(0);
		}
		else {
			int k = 1;
			while (!finA1.eof()) {
				string x;
				for (int i = 0; i < n1; i++) {
					if (finA1 >> x) {
						if (k > 0) {
							foutB << " " << x;
						}
						else {
							foutC << " " << x;
						}
					}
				}
				k *= -1;
			}
		}
		finA1.close();
		foutB.close();
		foutC.close();

		ifstream finB, finC;
		ofstream foutA;
		foutA.open(A);
		finB.open(B);
		finC.open(C);
		if (!foutA.is_open() || !finB.is_open() || !finC.is_open()) {
			cout << "Ошибка открытия файла" << endl;
			exit(0);
		}
		else {
			string b, c;
			int k = 0, count = 0;
			int* arr = new int[n1 * 2];
			while (!finB.eof()) {
				finB >> b;
				arr[k] = stoi(b);
				k++;
				if (finC >> c) {
					arr[k] = stoi(c);
					k++;
				}
				count += 2;
				if (count % (n1 * 2) == 0) {
					insertion_sort(arr, k);
					for (int i = 0; i < k; i++) {
						foutA << arr[i] << " ";
					}
					k = 0;
				}
			}
			delete[] arr;
		}
		foutA.close();
		finB.close();
		finC.close();
		n1 *= 2;
		A1=A;
	}
}

void first_sort_variate(string& A1, string B, string C, string A, int n)
{
	int start = clock();
	int n1 = 1;
	while (n1 < n) {
		ifstream finA1;
		ofstream foutB, foutC;
		finA1.open(A1);
		foutB.open(B);
		foutC.open(C);
		if (!finA1.is_open() || !foutB.is_open() || !foutC.is_open()) {
			cout << "Ошибка открытия файла" << endl;
		}
		else {
			int k = 1, l = 0;
			while (!finA1.eof()) {
				string x;
				for (int i = 0; i < n1; i++) {
					getline(finA1, x);
					l++;
					if (k > 0) {
						if (l == 1) {
							foutB << x;
						}
						else {
							foutB << endl << x;
						}
					}
					else {
						if (l == n) {
							foutC << x;
						}
						else {
							foutC << x << endl;
						}
					}
				}
				k *= -1;
			}
		}
		finA1.close();
		foutB.close();
		foutC.close();

		ifstream finB, finC;
		ofstream foutA;
		foutA.open(A);
		finB.open(B);
		finC.open(C);
		if (!foutA.is_open() || !finB.is_open() || !finC.is_open()) {
			cout << "Ошибка открытия файла" << endl;
		}
		else {
			string b, c;
			int k = 0, count = 0;
			Person* person = new Person[n1 * 2];
			while (!finB.eof() && count != n) {		
				finB >> person[k].name >> person[k].surname >> person[k].birthday
					>> person[k].weight >> person[k].height >> person[k].gender;
				k++;
				finC >> person[k].name >> person[k].surname >> person[k].birthday
					>> person[k].weight >> person[k].height >> person[k].gender;
				k++;
				count += 2;
				if (count % (n1 * 2) == 0) {
					insertion_sort_2(person, k);
					bool f = true;
					for (int i = 0; i < k; i++) {
						foutA << person[i].name << " " << person[i].surname << " " << person[i].birthday << " "
							<< person[i].weight << " " << person[i].height << " " << person[i].gender << endl;
					}
					k = 0;
				}
			}
			delete[] person;
		}
		foutA.close();
		finB.close();
		finC.close();
		n1 *= 2;
		A1 = A;
	}
	int end = clock();
	cout << "Время работы: " << end - start << " ms" << endl;
}

void second_sort_example(string& A1, string B, string C, string A, int n)
{
	first_sort_example(A1, B, C, A, n);
}

void second_sort_variate(string& A1, string B, string C, string A, int n)
{
	first_sort_variate(A1, B, C, A, n);
}

int main()
{
    setlocale(LC_ALL, "rus");
	int number, test;
	cout << "Выберите № задания: ";
	cin >> number;
	cout << "Выберите исходный файл (1 - из примера, 2 - по варианту): ";
	cin >> test;
	string A1;
	string A = "A.txt";
	string B = "B.txt";
	string C = "C.txt";
	switch (number)
	{
	case 1:
		switch (test)
		{
		case 1:
			A1 = "A11.txt";
			first_sort_example(A1, B, C, A, 15);
			break;
		case 2:
			A1 = "A2.txt";
			int n;
			cout << "Введите размер сортируемого файла: ";
			cin >> n;
			first_sort_variate(A1, B, C, A, n);
			break;
		}
		break;
	case 2:
		switch (test)
		{
		case 1:
			A1 = "A12.txt";
			second_sort_example(A1, B, C, A, 15);
			break;
		case 2:
			A1 = "A2.txt";
			int n;
			cout << "Введите размер сортируемого файла: ";
			cin >> n;
			second_sort_variate(A1, B, C, A, n);
			break;
		}
		break;
	}
}