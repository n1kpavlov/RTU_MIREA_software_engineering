import RSA


def main():
    rsa = RSA.RSA(p=17, q=19, e=11, d=131)

    while True:
        print("\nШифровщик RSA:")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Выйти")

        choice = input("\nВаш выбор (1-3): ").strip()

        if choice == '1':
            text = input("Введите текст для шифрования: ")
            try:
                encrypted = rsa.encrypt_from_string(text)
                print(f"\nЗашифрованный текст: {encrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            cipher = input("Введите числа через пробел: ").strip()
            try:
                decrypted = rsa.decrypt_from_string(cipher)
                print(f"\nРасшифрованный текст: {decrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '3':
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 3.")


if __name__ == "__main__":
    main()