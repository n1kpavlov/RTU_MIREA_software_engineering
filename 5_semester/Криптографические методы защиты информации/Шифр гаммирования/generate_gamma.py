import random
import math

def generate_prime():
    while True:
        num = random.getrandbits(50)
        if num < 2 ** 49:
            continue
        if num % 4 == 3:
            return num


def bbs_generator(length, mode, param_file="parametrs.txt"):
    if mode == "encrypt":
        p = generate_prime()
        q = generate_prime()
        while p == q:
            q = generate_prime()
        N = p * q
        X = 2 ** 40
        while math.gcd(X, N) != 1:
            X = random.randint(2, N - 1)

        with open(param_file, 'w') as f:
            f.write(f"p = {p}\nq = {q}\nX = {X}")
        print(f"Параметры гаммы записаны в файл: '{param_file}'")

    elif mode == "decrypt":
        with open(param_file, 'r') as f:
            p = int(f.readline()[4:])
            q = int(f.readline()[4:])
            N = p * q
            X = int(f.readline()[4:])

    gamma = []
    Xi = (X ** 2) % N
    for _ in range(length):
        Xi = (Xi ** 2) % N
        gamma.append(str(Xi % 2))
    return "".join(gamma)


def check_n_grams(sequence, n):
    n_grams = [sequence[i:i + n] for i in range(0, len(sequence) - n + 1)]
    n_gram_counts = {}
    for gram in n_grams:
        n_gram_counts[gram] = n_gram_counts.get(gram, 0) + 1
    total = len(n_grams)
    print(f"\n{n}-граммы (всего {len(n_gram_counts)} различных):")
    for gram, count in sorted(n_gram_counts.items()):
        percentage = count / total * 100
        print(f"  {gram}: {count} ({percentage:.2f}%)")


def check_golomb_postulates(sequence):
    total = len(sequence)
    zeros = sequence.count('0')
    ones = sequence.count('1')
    print(f"Количество нулей: {zeros} ({zeros / total * 100:.2f}%)")
    print(f"Количество единиц: {ones} ({ones / total * 100:.2f}%)")
    for n in range(2, 11):
        check_n_grams(sequence, n)


if __name__ == '__main__':
    gamma = bbs_generator(10000, "encrypt")
    print(gamma)

    check_golomb_postulates(gamma)