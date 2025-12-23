def main(y, x, z):
    if len(y) != len(x) or len(y) != len(z):
        raise ValueError("Все векторы должны иметь одинаковую длину")

    n = len(y)
    total = 0

    for i in range(n):
        term = z[i] ** 2 + x[n - 1 - i] ** 3 + 7 * y[n - 1 - i]
        total += 97 * (term ** 7)

    return 92 * total


# Пример использования
y = [-0.46, -0.41, -0.87, -0.38, -0.31, 0.9]
x = [0.74, -0.96, 0.85, -0.26, -0.82, -0.04]
z = [0.78, -0.9, 0.68, -0.02, 0.16, -0.6]

result = f(y, x, z)
print(result)  # Ожидаемый результат ≈ 5.29e+09