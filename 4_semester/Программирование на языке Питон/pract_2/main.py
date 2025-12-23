from math import sqrt, fabs
import matplotlib.pyplot as plt
import timeit
import Levenshtein

def task_1(n , m ,a):
    sum1 = 1
    for c in range(1, a + 1):
        sum2 = 1
        for j in range(1, m + 1):
            sum3 = 0
            for i in range(1, n + 1):
                sum3 += ((28 * c**2)**6 / 5 + 16 * (j**3 / 44 + i**2)**5)
            sum2 *= sum3
        sum1 *= sum2
    print(sum1)

def task_2(y, z):
    sum = 0
    n = len(y)
    for i in range(0, n):
        sum += (y[i] - z[i])**2
    return(sqrt(sum))

def task_3(y, z):
    sum = 0
    n = len(y)
    for i in range(0, n):
        sum += fabs(y[i] - z[i])
    return(sum)

def task_4(y, z):
    max = 0
    n = len(y)
    for i in range(0, n):
        if fabs(y[i] - z[i]) > max:
            max = fabs(y[i] - z[i])
    return(max)

def task_5(y, z):
    sum = 0
    n = len(y)
    for i in range(0, n):
        sum += (y[i] - z[i])**2
    return(sum)

def task_6(y, z, h):
    sum = 0
    n = len(y)
    for i in range(0, n):
        sum += (fabs(y[i] - z[i]))**h
    return(sum**(1 / h))


def task_7(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        print(distance_before_move)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()
    # Построение гистограммы с подписями.
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    # для тех, кто работает в средах, отличных от jupyter-подобных - раскомментировать строку ниже
    plt.show()

def task_8(words):
    n = len(words)
    str = words[n - 1]
    for i in range(1, n):
        str += " " + words[n - i - 1]
    print(str)

def f(s, c):
    count = 0
    for i in range(0, len(s)):
        if s[i] == c:
            count += 1
    return(count)

def task_9(s):
    dict = {}
    for i in range(0, len(s)):
        if s[i] == " ":
            continue
        dict[s[i]] = f(s, s[i])
    print(dict)

def levenshtein_distance(a, b, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    if a[i - 1] == b[j - 1]:
        return levenshtein_distance(a, b, i - 1, j - 1)

    return 1 + min(
        levenshtein_distance(a, b, i, j - 1),
        levenshtein_distance(a, b, i - 1, j),
        levenshtein_distance(a, b, i - 1, j - 1)
    )

def task_10(s1, s2):
    execution_time = timeit.timeit(lambda: levenshtein_distance(s1, s2, len(s1), len(s2)), number=1000)
    distance = levenshtein_distance(s1, s2, len(s1), len(s2))
    print(f"'{s1}' и '{s2}': {distance} : {execution_time} cек")

def levenshtein_distance_whil(a, b):
    if len(a) < len(b):
        return levenshtein_distance_whil(b, a)

    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def task_11(s1, s2):
    execution_time = timeit.timeit(lambda: levenshtein_distance_whil(s1, s2), number=1000)
    distance = levenshtein_distance_whil(s1, s2)
    print(f"'{s1}' и '{s2}': {distance} : {execution_time} cек")
    execution_time = timeit.timeit(lambda: Levenshtein.distance(s1, s2), number=1000)
    distance = Levenshtein.distance(s1, s2)
    print(f"'{s1}' и '{s2}': {distance} : {execution_time} cек")

if __name__ == "__main__":
    task_1(4, 2, 8)
    print(task_2([1, 0.5, 1], [0.5, 2, 1]))
    print(task_3([1, 0.5, 1], [0.5, 2, 1]))
    print(task_4([1, 0.5, 1], [0.5, 2, 1]))
    print(task_5([1, 0.5, 1], [0.5, 2, 1]))
    print(task_6([1, 0.5, 1], [0.5, 2, 1], 5))
    #task_7((task_2, task_3, task_4, task_5), [1, 0.5, 1], [0.5, 2, 1])
    task_8(["language!", "programming", "Python", "the", "love", "I"])
    task_9("I love the Python programming language!")
    task_10("Hello, world!", "Goodbye, world!")
    task_10("Hello, world!", "Bye, world!")
    task_10("I love Python", "I like Python")
    task_10("100101", "100011")
    task_11("Hello, world!", "Goodbye, world!")
    task_11("Hello, world!", "Bye, world!")
    task_11("I love Python", "I like Python")
    task_11("100101", "100011")