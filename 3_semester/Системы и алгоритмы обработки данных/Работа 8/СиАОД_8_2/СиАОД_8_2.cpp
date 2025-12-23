#include <iostream>
#include <vector>

using namespace std;

int backpack(const vector<int>& weights, const vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            }
            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    return dp[n][capacity];
}

int main() {
    setlocale(LC_ALL, "rus");

    int capacity, n;
    cout << "Введите вместимость рюкзака: ";
    cin >> capacity;
    cout << "Введите количество вещей: ";
    cin >> n;
    vector<int> weights(n), values(n);
    cout << "Введите веса вещей: ";
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    cout << "Введите ценности вещей: ";
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    int max_value = backpack(weights, values, capacity);
    cout << "Максимальная ценность: " << max_value << endl;

    return 0;
}
