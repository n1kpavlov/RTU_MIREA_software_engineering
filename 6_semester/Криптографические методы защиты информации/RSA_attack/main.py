from RSA import RSA


def generate_random_rsa():
    rsa = RSA()
    print(f"p = {rsa.p}")
    print(f"q = {rsa.q}")
    print(f"N = {rsa.N}")
    print(f"e = {rsa.e}")
    print(f"d = {rsa.d}")
    return rsa


def cyclic_attack(rsa, ciphertext_numbers):
    N, e = rsa.get_public_key()
    recovered_plaintext = []

    for y in ciphertext_numbers:
        t = 1
        y_current = pow(y, e, N)

        while True:
            if y_current == y:
                plaintext_num = pow(y, pow(e, t - 1), N)
                try:
                    char = chr(plaintext_num)
                    recovered_plaintext.append(char)
                except ValueError:
                    recovered_plaintext.append('?')
                break

            y_current = pow(y_current, e, N)
            t += 1

    result = ''.join(recovered_plaintext)
    print(f"\nРасшифрованный текст: {result}")


def meet_in_the_middle_attack(rsa, ciphertext_numbers, l):
    N, e = rsa.get_public_key()
    message_space_size = pow(2, l) - 1
    recovered_plaintext = []

    encryption_table = {}
    for x1 in range(1, message_space_size):
        c = pow(x1, e, N)
        encryption_table[c] = x1

    for c in ciphertext_numbers:
        found = False
        for x2 in range(1, message_space_size):
            c1 = pow(x2, e, N)
            if c1 != 0 and c % c1 == 0:
                c2 = (c * pow(c1, -1, N)) % N
                if c2 and c2 in encryption_table:
                    m = (encryption_table[x2] * encryption_table[c2]) % N
                    try:
                        char = chr(m)
                        recovered_plaintext.append(char)
                        found = True
                        break
                    except ValueError:
                        pass
        if not found:
            recovered_plaintext.append('?')

    result = ''.join(recovered_plaintext)
    print(f"\nРасшифрованный текст: {result}")


def main():
    rsa = None

    while True:
        print("\nРабота с RSA:")
        print("1. Сгенерировать ключи RSA")
        print("2. Зашифровать текст")
        print("3. Расшифровать текст (с ключом d)")
        print("4. Циклическая атака на RSA")
        print("5. Атака 'встреча посередине'")
        print("6. Выйти")

        choice = input("\nВаш выбор (1-6): ").strip()

        if choice == '1':
            rsa = generate_random_rsa()

        elif choice == '2':
            if not rsa:
                print("Сначала сгенерируйте ключи (пункт 1)")
                continue
            text = input("Введите текст для шифрования: ")
            try:
                encrypted = rsa.encrypt_from_string(text)
                print(f"\nЗашифрованный текст: {encrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '3':
            if not rsa:
                print("Сначала сгенерируйте ключи (пункт 1)")
                continue
            cipher = input("Введите числа через пробел: ").strip()
            try:
                decrypted = rsa.decrypt_from_string(cipher)
                print(f"\nРасшифрованный текст: {decrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '4':
            if not rsa:
                print("Сначала сгенерируйте ключи (пункт 1)")
                continue
            cipher = input("Введите числа через пробел: ").strip()
            try:
                numbers = [int(x) for x in cipher.split()]
                cyclic_attack(rsa, numbers)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '5':
            if not rsa:
                print("Сначала сгенерируйте ключи (пункт 1)")
                continue
            cipher = input("Введите числа через пробел: ").strip()
            try:
                numbers = [int(x) for x in cipher.split()]
                l = 20
                meet_in_the_middle_attack(rsa, numbers, l)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '6':
            print("\nВыход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")


if __name__ == "__main__":
    main()