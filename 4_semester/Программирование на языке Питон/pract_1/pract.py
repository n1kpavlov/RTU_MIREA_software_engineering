import math

def task_3_1(x):
    x += x
    x += x
    x += x + x
    print(x)

def task_3_2(x):
    x += x
    x += x
    x += x
    x += x
    print(x)

def task_3_3(x):
    a = x + x
    a += a
    a += a
    x -= a
    a -= x
    print(a)

def task_3_4(a, b, n):
    sum_part = 0
    for j in range(1, n + 1):
        for c in range(1, b + 1):
            sum_part += (34 * j + 41) ** 4 - 93 * (c + 79 + c ** 3) ** 5

    prod_part = 1
    for k in range(1, a + 1):
        inner_sum = 0
        for c in range(1, b + 1):
            inner_sum += 22 * (c - 8) ** 5 - k ** 4
        prod_part *= inner_sum

    print(sum_part - prod_part)

def task_3_5(x):
    if x < 13:
        print(x ** 5)
    elif 13 <= x < 87:
        print(x ** 7 - 1 - (math.ceil(x) ** 3) / 54)
    else:
        print(math.ceil(x) ** 3)

def task_3_6(n):
    if n == 0:
        print(3)
    else:
        prev = 3
        for i in range(1, n + 1):
            current = math.sin(prev) - (1 / 16) * prev ** 3
            prev = current
        print(prev)

def task_3_7(x, y):
    sum = 0
    while y > 0:
        if y % 2 != 0:
            sum += x
        x *= 2
        y //= 2
    print(sum)

def task_3_8(a, n):
    x = a
    for i in range(1, n):
        y = a
        sum = 0
        while y > 0:
            if y % 2 != 0:
                sum += x
            x *= 2
            y //= 2
        x = sum
    print(x)

def task_3_9(y):
    if y == 12:
        print("def f(x):")
        print(" x += x")
        print(" x += x")
        print(" x += x + x")
        print(" return x")

    elif y == 16:
        print("def f(x):")
        print(" x += x")
        print(" x += x")
        print(" x += x")
        print(" x += x")
        print(" return x")

    elif y == 15:
        print("def f(x):")
        print(" a = x + x")
        print(" a += a")
        print(" a += a")
        print(" x -= a")
        print(" a -= x")
        print(" return a")

    else:
        print("Функция для умножения на", y, "не реализована.")

if __name__=="__main__":
    task_3_1(2)
    task_3_2(3)
    task_3_3(4)
    task_3_4(6, 2, 2)
    task_3_5(14)
    task_3_6(8)
    task_3_7(9, 5)
    task_3_8(2, 10)
    task_3_9(15)
