#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int distance(const string& word1, const string& word2) {
    int dist = 0;
    for (int i = 0; i < min(word1.size(), word2.size()); i++) {
        if (word1[i] != word2[i]) {
            dist++;
        }
    }
    dist += abs(static_cast<int>(word1.size()) - static_cast<int>(word2.size()));
    return dist;
}

void find_closest_pairs(const string& sentence) {
    vector<string> words;
    string current_word;
    for (char c : sentence) {
        if (c == ' ' || c == ',') {
            if (!current_word.empty()) {
                words.push_back(current_word);
                current_word.clear();
            }
        }
        else {
            current_word += c;
        }
    }
    if (!current_word.empty()) {
        words.push_back(current_word);
    }

    if (words.size() < 2) {
        cout << "В предложении недостаточно слов.\n";
        return;
    }

    int min_dist = INT_MAX;
    vector<pair<string, string>> closest_pairs;
    for (int i = 0; i < words.size() - 1; i++) {
        for (int j = i + 1; j < words.size(); j++) {
            int dist = distance(words[i], words[j]);
            if (dist < min_dist) {
                min_dist = dist;
                closest_pairs.clear();
                closest_pairs.push_back({ words[i], words[j] });
            }
            else if (dist == min_dist) {
                closest_pairs.push_back({ words[i], words[j] });
            }
        }
    }

    if (!closest_pairs.empty()) {
        cout << "Пары слов с минимальным расстоянием:\n";
        for (auto& pair : closest_pairs) {
            cout << pair.first << " " << pair.second << " (Расстояние: " << min_dist << ")\n";
        }
    }
    else {
        cout << "В предложении нет пар слов с минимальным расстоянием.\n";
    }
}

int main() {
    setlocale(LC_ALL, "rus");
    system("chcp 1251");
    string sentence;
    cout << "Введите предложение: ";
    getline(cin, sentence);
    find_closest_pairs(sentence);
    return 0;
}
