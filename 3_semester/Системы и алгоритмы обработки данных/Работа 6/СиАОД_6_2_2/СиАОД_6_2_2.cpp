#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> make_stoptable(string text, string pattern) {
    vector<int> stoptable(256, pattern.size());
    for (int i = 0; i < pattern.size() - 1; i++) {
        stoptable[pattern[i]] = pattern.size() - 1 - i;
    }
    return stoptable;
}

vector<int> boyer_moore_horspool(string text, string pattern) {
    vector<int> matches;
    vector<int> stoptable = make_stoptable(text, pattern);
    int pos = pattern.size() - 1;
    while (pos <= (text.size() - 1)) {
        bool f = true;
        int dif = 0;
        for (int i = 0; i < pattern.size(); i++) {
            if (pattern[pattern.size() - 1 - i] != text[pos -  i]) {
                f = false;
                dif = i;
                break;
            }
        }
        if (f) {
            matches.push_back(pos - pattern.size() + 1);
            pos++;
        }
        else if (dif == 0) {
            pos += stoptable[text[pos]];
        }
        else {
            pos += stoptable[pattern[pattern.size() - 1 - dif]];
        }
    }
    return matches;
}

int main() {
    setlocale(LC_ALL, "rus");
    system("chcp 1251");
    string text, pattern;
    cout << "Введите строку: ";
    getline(cin, text);
    cout << "Введите подстроку: ";
    getline(cin, pattern);
    vector<int> matches = boyer_moore_horspool(text, pattern);
    if (!matches.empty()) {
        cout << "Вхождения подстроки в строку:\n";
        for (int match : matches) {
            cout << match << " ";
        }
    }
    else {
        cout << "Подстрока не найдена в строке.\n";
    }
    return 0;
}
