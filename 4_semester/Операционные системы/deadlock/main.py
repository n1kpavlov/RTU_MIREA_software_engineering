import numpy as np
import argparse

def detect_deadlock(T, C, R):
    m = len(T)
    n = len(C)

    if C.shape != (n, m) or R.shape != (n, m):
        raise ValueError("Несоответствие размеров матриц C и R вектору T")

    if np.any(T < 0) or np.any(C < 0) or np.any(R < 0):
        raise ValueError("Все значения в T, C и R должны быть неотрицательными")

    A = np.array(T) - np.sum(C, axis=0)
    completed = np.zeros(n, dtype=bool)

    while True:
        found = False
        for i in range(n):
            if not completed[i] and np.all(R[i] <= A):
                A += C[i]
                completed[i] = True
                found = True

        if not found:
            break

    if np.any(~completed):
        print("Обнаружена взаимоблокировка")
    else:
        print("Взаимоблокировка не обнаружена")

def read_vector(filename):
    with open(filename, 'r') as file:
        return np.array(list(map(int, file.readline().strip().split())))

def read_matrix(filename):
    with open(filename, 'r') as file:
        return np.array([list(map(int, line.strip().split())) for line in file])

def main():
    parser = argparse.ArgumentParser(description="Обнаружение взаимоблокировки")
    parser.add_argument('T_file', type=str, help="Файл с вектором T")
    parser.add_argument('C_file', type=str, help="Файл с матрицей C")
    parser.add_argument('R_file', type=str, help="Файл с матрицей R")
    args = parser.parse_args()

    try:
        T = read_vector(args.T_file)
        C = read_matrix(args.C_file)
        R = read_matrix(args.R_file)

        detect_deadlock(T, C, R)
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
