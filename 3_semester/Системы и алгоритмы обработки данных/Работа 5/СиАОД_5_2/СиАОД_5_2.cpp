#include <iostream>
#include <bitset>
#include <fstream>
#include <string>
#include <ctime>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

struct book {
    
    long long isbn;
    string author;
    string name;

    string out() {
        return to_string(isbn) + ", " + author + ", " + name + "\n";
    }
};

bool comp(const pair<book, int>& left, const pair<book, int>& right) {
    return left.first.isbn < right.first.isbn;
}

int search_key(vector<pair<book, int>> tabl, vector<int> table, long long key) {
    int i = table[0] - 1;
    bool f = false;
    if (key >= tabl[0].first.isbn && key <= tabl[tabl.size() - 1].first.isbn) {
        for (int j = 1; j < table.size(); j++) {
            if (tabl[i].first.isbn == key) {
                f = true;
                break;
            }
            else if (tabl[i].first.isbn < key) {
                i += table[j];
            }
            else {
                i -= table[j];
            }
        }
        if (f) {
            return tabl[i].second;
        }
        else {
            return -1;
        }
    }
    else {
        return -1;
    }
    return 0;
}

string search_url(string s, int url) {
    unsigned int start = clock();
    ifstream fin(s, ios::binary | ios::in);
    fin.seekg(sizeof(book) * (url - 1), ios_base::beg);
    book test;
    fin.read((char*)&test, sizeof(book));
    fin.close();
    unsigned int end = clock();
    cout << "Время работы программы: " << end - start << " ms" << endl;
    return test.out();
}

int main()
{
    setlocale(LC_ALL, "rus");
    srand(time(0));
    vector<pair<book, int>> tabl;

    int x, size = rand() % 100;
    book test;

    ofstream fout("books.bin", ios::binary | ios::out);
    for (int i = 0; i < size; i++) {
        test.isbn = 0;
        for (int j = 0; j < 12; j++) {
            x = rand() % 10;
            if (x == 0 && j == 11) {
                test.isbn += (x + 1) * pow(10, j);
            }
            else {
                test.isbn += x * pow(10, j);
            }
        }
        test.author = "Vasya_" + to_string(size - i);
        test.name = "book_" + to_string(i);
        fout.write((char*)&test, sizeof(book));
    }
    fout.close();


    //Линейный поиск
    
    unsigned int start = clock();
    ifstream fin("books.bin", ios::binary | ios::in);
    long long key;
    int number = 0;
    bool f = false;
    cout << "Введите ключ для поиска: ";
    cin >> key;
    while (fin.read((char*)&test, sizeof(book))) {
        number++;
        if (test.isbn == key) {
            f = true;
            break;
        }
    }
    if (f) {
        cout << "Искомый ключ в " << number << " строке" << endl;
    }
    else {
        cout << "Ключ не найден" << endl;
    }
    fin.close();
    unsigned int end = clock();
    cout << "Время работы программы: " << end - start << " ms"  << endl;


    //однородный бинарный поиск с таблицей смещений

    fin.open("books.bin", ios::binary | ios::in);
    for (int i = 0; i < size; i++) {
        fin.read((char*)&test, sizeof(book));
        tabl.push_back(make_pair(test, i + 1));
    }
    fin.close();

    sort(tabl.begin(), tabl.end(), comp);

    for (auto element : tabl) {
        cout << element.second << " " << element.first.out();
    }

    vector <int> table;
    for (int j = 1; j <= log2(tabl.size()) + 2; j++) {
        table.push_back((tabl.size() + pow(2, j - 1)) / pow(2, j));
    }

    cout << "Введите ключ для поиска: ";
    cin >> key;
    start = clock();
    int out = search_key(tabl, table, key);
    end = clock();
    cout << "Время работы программы: " << end - start << " ms" << endl;
    if (out >= 0) {
        cout << "Искомый ключ в " << out << " строке" << endl;
    }
    else {
        cout << "Ключ не найден" << endl;
    }


    //прямой доступ к записи файла

    int url;
    cout << "Введите номер записи: ";
    cin >> url;
    string s = "books.bin";
    cout << "Найдена запись: " << search_url(s, url);
}