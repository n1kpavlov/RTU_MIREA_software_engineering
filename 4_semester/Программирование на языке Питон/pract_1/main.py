from math import exp


def main(m, x, a, b):
    result = 0
    for k in range(1, m + 1):
        result += x ** 4 + 48 * exp(k)
        for c in range(1, b + 1):
            summ = 1
            for j in range(1, a + 1):
                summ *= 1 - (47 * c - x ** 3) ** 2 - (60 * k + 33 + j ** 3)
            result += summ
    return(result)

if __name__ == "__main__":
    print(main(8, 0.9, 3, 6)) # ≈ -5.78e+15
    print(main(8, 0.29, 4, 4)) # ≈ 1.43e+19
    print(main(8, 0.67, 6, 5)) # ≈ 2.50e+29
    print(main(7, -0.3, 6, 6)) # ≈ 2.04e+30
    print(main(5, -0.58, 2, 2)) # ≈ 4.43e+08