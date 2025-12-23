#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

struct Node {
    char symbol;
    int frequency;
    Node* left;
    Node* right;

    Node(char s, int f) : symbol(s), frequency(f), left(nullptr), right(nullptr) {}
};

bool compareNodesByFrequency(Node* a, Node* b) {
    return a->frequency > b->frequency;
}

int calculateTotalFrequency(const vector<Node*>& nodes) {
    int totalFrequency = 0;
    for (Node* node : nodes) {
        totalFrequency += node->frequency;
    }
    return totalFrequency;
}

map<char, int> convertNodesToMap(const vector<Node*>& nodes) {
    map<char, int> frequencies;
    for (Node* node : nodes) {
        frequencies[node->symbol] = node->frequency;
    }
    return frequencies;
}

Node* createShannonFanoTree(const map<char, int>& frequencies) {
    vector<Node*> nodes;
    for (const auto& pair : frequencies) {
        nodes.push_back(new Node(pair.first, pair.second));
    }
    sort(nodes.begin(), nodes.end(), compareNodesByFrequency);

    while (nodes.size() > 1) {
        vector<Node*> leftSubtree, rightSubtree;
        int summLeft = 0, summRight = 0;
        for (int i = 0; i < nodes.size(); i++) {
            if (summLeft <= summRight) {
                leftSubtree.push_back(nodes[i]);
                summLeft += nodes[i]->frequency;
            }
            else {
                rightSubtree.push_back(nodes[i]);
                summRight += nodes[i]->frequency;
            }
        }

        Node* parent = new Node('\0', calculateTotalFrequency(leftSubtree) + calculateTotalFrequency(rightSubtree));
        parent->left = createShannonFanoTree(convertNodesToMap(leftSubtree));
        parent->right = createShannonFanoTree(convertNodesToMap(rightSubtree));

        nodes.clear();
        nodes.push_back(parent);
        sort(nodes.begin(), nodes.end(), compareNodesByFrequency);
    }

    return nodes.front();
}

void traverse(Node* node, string code, map<char, string>& codes) {
    if (node->left == nullptr && node->right == nullptr) {
        codes[node->symbol] = code;
        return;
    }
    traverse(node->left, code + "0", codes);
    traverse(node->right, code + "1", codes);
};

map<char, string> getCodes(Node* root) {
    map<char, string> codes;
    if (root == nullptr) {
        return codes;
    }
    traverse(root, "", codes);
    return codes;
}

string compress(const string& text, const map<char, string>& codes) {
    string compressedText;
    for (char c : text) {
        compressedText += codes.at(c);
    }
    return compressedText;
}

string decompress(const string& compressedText, const map<char, string>& codes) {
    string decompressedText = "";
    int i = 0;
    string currentCode = "";
    while (i < compressedText.length()) {
        currentCode += compressedText[i];
        for (const auto& pair : codes) {
            if (pair.second == currentCode) {
                decompressedText += pair.first;
                currentCode = "";
                break;
            }
        }
        i++;
    }
    return decompressedText;
}

void shannonFano() {
    cout << "Реализация сжатия методом Шеннона-Фано:\n\n";
    
    string text = "Кони-кони, коникони,\nМы сидели на балконе,\nЧай пили, воду пили,\nПо - турецки говорили.";
    cout << "Сжимаемые данные:" << text << endl;

    map<char, int> frequency;
    for (char c : text) {
        frequency[c]++;
    }

    Node* root = createShannonFanoTree(frequency);

    map<char, string> codes = getCodes(root);

    /*cout << "Таблица кодировки символов:" << endl;
    for (auto code : codes) {
        cout << code.first << " " << code.second << endl;
    }*/

    string compressedText = compress(text, codes);
    cout << "Сжатый текст: " << compressedText << endl;

    string decompressedText = decompress(compressedText, codes);
    cout << "Восстановленный текст: " << decompressedText << endl << endl << endl;
}


Node* createHuffmanTree(const map<char, int>& frequencies) {
    vector<Node*> nodes;
    for (const auto& pair : frequencies) {
        nodes.push_back(new Node(pair.first, pair.second));
    }
    sort(nodes.begin(), nodes.end(), compareNodesByFrequency);

    while (nodes.size() > 1) {
        Node* left = nodes.back();
        nodes.pop_back();
        Node* right = nodes.back();
        nodes.pop_back();
        Node* parent = new Node('\0', left->frequency + right->frequency);
        parent->left = left;
        parent->right = right;
        nodes.push_back(parent);
        sort(nodes.begin(), nodes.end(), compareNodesByFrequency);
    }

    return nodes.front();
}

void huffman() {
    cout << "Реализация сжатия методом Хаффмана:\n\n";

    string text = "Павлов Никита Сергеевич";
    cout << "Сжимаемые данные:" << text << endl;

    map<char, int> frequency;
    for (char c : text) {
        frequency[c]++;
    }

    Node* root = createHuffmanTree(frequency);

    map<char, string> codes = getCodes(root);

    /*cout << "Таблица кодировки символов:" << endl;
    for (auto code : codes) {
        cout << code.first << " " << code.second << endl;
    }*/

    string compressedText = compress(text, codes);
    cout << "Сжатый текст: " << compressedText << endl;

    string decompressedText = decompress(compressedText, codes);
    cout << "Восстановленный текст: " << decompressedText << endl << endl << endl;
}


struct LZ77Entry {
    int offset;
    int length;
    char nextChar;
};

vector<LZ77Entry> compressLZ77(const string& data) {
    vector<LZ77Entry> compressedData;
    int windowSize = 1024;
    int searchBufferSize = 4096;
    int i = 0;

    while (i < data.length()) {
        int maxMatchLength = 0;
        int maxMatchOffset = 0;
        for (int j = max(0, i - windowSize); j < i; j++) {
            int k = 0;
            while (j + k < i && data[j + k] == data[i + k] && k < searchBufferSize) {
                k++;
            }
            if (k >= maxMatchLength) {
                maxMatchLength = k;
                maxMatchOffset = i - j;
            }
        }
        if (maxMatchLength > 0) {
            compressedData.push_back({ maxMatchOffset, maxMatchLength, data[i + maxMatchLength] });
            i += maxMatchLength + 1;
        }
        else {
            compressedData.push_back({ 0, 0, data[i] });
            i++;
        }
    }

    return compressedData;
}

string decompressLZ77(const vector<LZ77Entry>& compressedData) {
    string decompressedData;

    for (const auto& entry : compressedData) {
        if (entry.length > 0) {
            int start = decompressedData.size() - entry.offset;
            for (int i = 0; i < entry.length; i++) {
                decompressedData += decompressedData[start + i];
            }
        }
        decompressedData += entry.nextChar;
    }

    return decompressedData;
}

void lz77() {
    cout << "Реализация сжатия методом LZ77:\n\n";
    
    string data = "0100001000000100001";
    cout << "Сжимаемые данные: " << data << endl;

    vector<LZ77Entry> compressedData = compressLZ77(data);

    cout << "Сжатые данные:" << endl;
    for (const auto& entry : compressedData) {
        cout << "(" << entry.offset << ", " << entry.length << ", " << entry.nextChar << ")" << endl;
    }

    string decompressedData = decompressLZ77(compressedData);
    cout << "Восстановленные данные: " << decompressedData << endl << endl << endl;
}


struct LZ78Entry {
    int index;
    char nextChar;
};

vector<LZ78Entry> compressLZ78(const string& data) {
    vector<LZ78Entry> compressedData;
    unordered_map<string, int> dictionary;
    dictionary[""] = 0;
    int index = 1;
    string currentWord = "";

    for (int i = 0; i < data.length(); i++) {
        string newWord = currentWord + data[i];
        if (dictionary.find(newWord) == dictionary.end()) {
            dictionary[newWord] = index;
            index++;
            compressedData.push_back({ dictionary[currentWord], data[i] });
            currentWord = "";
        }
        else {
            currentWord = newWord;
        }
    }
    if (!currentWord.empty()) {
        compressedData.push_back({ dictionary[currentWord], '\0' });
    }

    return compressedData;
}

string decompressLZ78(const vector<LZ78Entry>& compressedData) {
    string decompressedData, currentWord;
    unordered_map<int, string> dictionary;
    dictionary[0] = "";

    for (const auto& entry : compressedData) {
        currentWord = dictionary[entry.index] + entry.nextChar;
        decompressedData += currentWord;
        dictionary[dictionary.size()] = currentWord;
    }

    return decompressedData;
}

void lz78() {
    cout << "Реализация сжатия методом LZ78:\n\n";

    string data = "пропронепронепрнепрона с";
    cout << "Сжимаемые данные: " << data << endl;

    vector<LZ78Entry> compressedData = compressLZ78(data);
    cout << "Сжатые данные:" << endl;
    for (const auto& entry : compressedData) {
        cout << "(" << entry.index << ", " << entry.nextChar << ")" << endl;
    }

    string decompressedData = decompressLZ78(compressedData);
    cout << "Восстановленные данные: " << decompressedData << endl << endl << endl;
}

int main()
{
    setlocale(LC_ALL, "rus");
    system("chcp 1251");

    shannonFano();
    huffman();
    lz77();
    lz78();
}