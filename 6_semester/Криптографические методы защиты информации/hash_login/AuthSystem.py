import os
import random
import CustomHash


class AuthSystem:
    def __init__(self, filename="users.txt"):
        self.hasher = CustomHash.CustomHash()
        self.filename = filename
        if not os.path.exists(filename):
            open(filename, 'w').close()


    def hash_password(self, password):
        return self.hasher.hash(password)


    def generate_salt(self):
        return f"{random.randint(1, 65535):04X}"


    def xor_with_salt(self, hash_value, salt):
        hash_int = int(hash_value, 16)
        sault_int = int(salt, 16)
        result = hash_int ^ sault_int
        return hex(result)[2:]


    def check_login_exists(self, login):
        with open(self.filename, 'r') as f:
            for line in f:
                if line.strip():
                    stored_login, _, _ = line.strip().split(':')
                    if stored_login == login:
                        return True
        return False


    def register(self):
        print("\nРегистрация:")

        while True:
            login = input("Введите логин: ").strip()
            if not login:
                print("Логин не может быть пустым!")
                continue

            if self.check_login_exists(login):
                print("Этот логин уже занят! Попробуйте другой.")
            else:
                break

        while True:
            password = input("Введите пароль (минимум 10 символов): ")
            if len(password) < 10:
                print("Пароль должен содержать минимум 10 символов!")
            else:
                break

        password_hash = self.hash_password(password)
        salt = self.generate_salt()
        xor_result = self.xor_with_salt(password_hash, salt)

        with open(self.filename, 'a') as f:
            f.write(f"{login}:{xor_result}:{salt}\n")

        print("Регистрация прошла успешно!")


    def login(self):
        print("\nАвторизация:")

        login = input("Введите логин: ").strip()
        if not self.check_login_exists(login):
            print("Пользователь с таким логином не найден!")
            return False

        password = input("Введите пароль: ")

        with open(self.filename, 'r') as f:
            for line in f:
                if line.strip():
                    stored_login, stored_xor, stored_salt = line.strip().split(':')

                    if stored_login == login:
                        password_hash = self.hash_password(password)
                        computed_xor = self.xor_with_salt(password_hash, stored_salt)

                        if computed_xor == stored_xor:
                            print("Авторизация успешна! Добро пожаловать!")
                            return True
                        else:
                            print("Неверный пароль!")
                            return False
        return False


def main():
    auth = AuthSystem()

    while True:
        print("\nСИСТЕМА АВТОРИЗАЦИИ")
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            auth.register()
        elif choice == '2':
            auth.login()
        elif choice == '3':
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите 1-3.")


if __name__ == "__main__":
    main()