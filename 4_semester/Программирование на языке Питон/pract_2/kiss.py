from math import sin


def f(n):
    arr = [0.70]
    for i in range(1, n + 1):
        arr.append(sin(13 * arr[i - 1]**3 + arr[i - 1]**2)**2)
    return arr[n]


def main(n):
    return f(n)

if __name__ == "__main__":
    print(f(2))
    print(f(1))
    print(f(8))
    print(f(5))
    print(f(7))