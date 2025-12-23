import string
import os


class SubstitutionCipherDecoder:
    def __init__(self, encrypted_text):
        self.encrypted_text = encrypted_text.upper()
        self.original_text = encrypted_text.upper()

        # Создаем алфавит (русский + английский)
        self.russian_alphabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ'
        self.all_alphabet = self.russian_alphabet

        # Словарь для подстановки (изначально все символы остаются как есть)
        self.substitution_map = {char: char for char in self.all_alphabet}

        # История изменений для отмены
        self.history = []

    def save_state(self):
        """Сохраняет текущее состояние подстановки"""
        self.history.append(self.substitution_map.copy())

    def set_substitution(self, encrypted_char, decrypted_char):
        """Устанавливает подстановку для символа"""
        encrypted_char = encrypted_char.upper()
        decrypted_char = decrypted_char.upper()

        if encrypted_char not in self.all_alphabet:
            print(f"Ошибка: символ '{encrypted_char}' не найден в алфавите")
            return False

        # Сохраняем состояние перед изменением
        self.save_state()

        # Устанавливаем подстановку
        self.substitution_map[encrypted_char] = decrypted_char
        return True

    def remove_substitution(self, encrypted_char):
        """Удаляет подстановку для символа"""
        encrypted_char = encrypted_char.upper()

        if encrypted_char in self.substitution_map:
            self.save_state()
            self.substitution_map[encrypted_char] = encrypted_char
            return True
        return False

    def undo(self):
        """Отменяет последнее изменение"""
        if self.history:
            self.substitution_map = self.history.pop()
            return True
        return False

    def decrypt(self):
        """Дешифрует текст с текущими подстановками"""
        result = []
        for char in self.original_text:
            if char.upper() in self.substitution_map:
                # Сохраняем регистр
                if char.isupper():
                    result.append(self.substitution_map[char.upper()])
                else:
                    result.append(self.substitution_map[char.upper()].lower())
            else:
                result.append(char)
        return ''.join(result)

    def display_two_line_view(self):
        """Выводит текст в две линии: сверху расшифрованный, снизу оригинальный"""
        decrypted_line = []
        encrypted_line = []

        for char in self.original_text:
            upper_char = char.upper()

            # Верхняя строка: расшифрованный символ или "_" если не изменен
            if upper_char in self.substitution_map:
                decrypted_char = self.substitution_map[upper_char]
                if decrypted_char == upper_char:  # Подстановка не установлена
                    decrypted_line.append('_')
                else:
                    # Сохраняем регистр
                    if char.isupper():
                        decrypted_line.append(decrypted_char)
                    else:
                        decrypted_line.append(decrypted_char.lower())
            else:
                decrypted_line.append(char)

            # Нижняя строка: оригинальный символ
            encrypted_line.append(char)

        # Форматируем вывод
        max_line_length = 80  # Максимальная длина строки для удобства просмотра

        print("╔" + "═" * max_line_length + "╗")
        print("║ РАСШИФРОВАННЫЙ ТЕКСТ:" + " " * (max_line_length - 22) + "║")
        print("║ " + "".join(decrypted_line).ljust(max_line_length) + " ║")
        print("║ " + " " * max_line_length + " ║")
        print("║ ИСХОДНЫЙ ТЕКСТ:" + " " * (max_line_length - 16) + "║")

        # Выводим нижнюю строку с выравниванием под верхней
        encrypted_display = "".join(encrypted_line)
        decrypted_display = "".join(decrypted_line)

        # Разбиваем на строки для длинных текстов
        for i in range(0, len(decrypted_display), max_line_length):
            decrypted_part = decrypted_display[i:i + max_line_length]
            encrypted_part = encrypted_display[i:i + max_line_length]

            # Выравниваем нижнюю строку относительно верхней
            encrypted_aligned = []
            for j, char in enumerate(encrypted_part):
                if j < len(decrypted_part) and decrypted_part[j] == '_':
                    encrypted_aligned.append(char)
                else:
                    encrypted_aligned.append(' ')

            print("║ " + decrypted_part.ljust(max_line_length) + " ║")
            print("║ " + "".join(encrypted_aligned).ljust(max_line_length) + " ║")
            if i + max_line_length < len(decrypted_display):
                print("║ " + " " * max_line_length + " ║")

        print("╚" + "═" * max_line_length + "╝")

    def show_statistics(self):
        """Показывает статистику по подстановкам"""
        substituted = {k: v for k, v in self.substitution_map.items() if k != v}
        print(f"\n--- Статистика ---")
        print(f"Всего символов в алфавите: {len(self.all_alphabet)}")
        print(f"Расшифровано символов: {len(substituted)}")
        print(f"Осталось расшифровать: {len(self.all_alphabet) - len(substituted)}")

        if substituted:
            print("\nТекущие подстановки:")
            for enc, dec in sorted(substituted.items()):
                print(f"  {enc} -> {dec}")

    def show_frequency(self):
        """Показывает частоту символов в зашифрованном тексте"""
        freq = {}
        total_letters = 0

        for char in self.encrypted_text:
            if char.upper() in self.all_alphabet:
                upper_char = char.upper()
                freq[upper_char] = freq.get(upper_char, 0) + 1
                total_letters += 1

        if total_letters > 0:
            print(f"\n--- Частота символов (всего букв: {total_letters}) ---")
            sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

            for char, count in sorted_freq[:15]:  # Показываем топ-15
                percentage = (count / total_letters) * 100
                substitution = self.substitution_map[char]
                status = "✓" if char != substitution else " "
                print(f"{status} {char}: {count:3d} раз ({percentage:5.2f}%) -> {substitution}")

    def save_progress(self, filename):
        """Сохраняет прогресс в файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Сохраняем зашифрованный текст
                f.write(f"ENCRYPTED_TEXT:{self.original_text}\n")

                # Сохраняем подстановки
                for enc, dec in self.substitution_map.items():
                    if enc != dec:
                        f.write(f"SUBSTITUTION:{enc}:{dec}\n")

            print(f"Прогресс сохранен в файл: {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

    def load_progress(self, filename):
        """Загружает прогресс из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()

                for line in lines:
                    line = line.strip()
                    if line.startswith('ENCRYPTED_TEXT:'):
                        self.original_text = line.split(':', 1)[1]
                    elif line.startswith('SUBSTITUTION:'):
                        parts = line.split(':')
                        if len(parts) == 3:
                            enc, dec = parts[1], parts[2]
                            self.substitution_map[enc] = dec

            print(f"Прогресс загружен из файла: {filename}")
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")


def clear_screen():
    """Очищает экран консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("=== Дешифратор методом простой подстановки ===\n")

    # Получаем зашифрованный текст
    encrypted_text = input("Введите зашифрованный текст: ")

    if not encrypted_text:
        print("Используем пример текста для демонстрации...")
        encrypted_text = "Съешь же ещё этих мягких французских булок, да выпей чаю."

    decoder = SubstitutionCipherDecoder(encrypted_text)

    while True:
        clear_screen()

        # Показываем двухстрочное представление
        decoder.display_two_line_view()

        # Показываем статистику
        decoder.show_frequency()
        decoder.show_statistics()

        # Меню
        print("\n=== КОМАНДЫ ===")
        print("1. Установить подстановку (например: А Б)")
        print("2. Удалить подстановку (например: А)")
        print("3. Отменить последнее действие")
        print("4. Сохранить прогресс")
        print("5. Загрузить прогресс")
        print("6. Сбросить все подстановки")
        print("0. Выход")

        choice = input("\nВыберите команду: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            substitution = input("Введите подстановку (зашифрованный_символ дешифрованный_символ): ").split()
            if len(substitution) == 2:
                if decoder.set_substitution(substitution[0], substitution[1]):
                    print("Подстановка установлена!")
                else:
                    print("Ошибка установки подстановки!")
            else:
                print("Неверный формат! Используйте: А Б")
            input("\nНажмите Enter для продолжения...")

        elif choice == '2':
            char_to_remove = input("Введите символ для удаления подстановки: ").strip()
            if decoder.remove_substitution(char_to_remove):
                print("Подстановка удалена!")
            else:
                print("Символ не найден или подстановка не установлена!")
            input("\nНажмите Enter для продолжения...")

        elif choice == '3':
            if decoder.undo():
                print("Действие отменено!")
            else:
                print("Нечего отменять!")
            input("\nНажмите Enter для продолжения...")

        elif choice == '4':
            filename = input("Введите имя файла для сохранения: ").strip()
            if filename:
                decoder.save_progress(filename)
            input("\nНажмите Enter для продолжения...")

        elif choice == '5':
            filename = input("Введите имя файла для загрузки: ").strip()
            if filename:
                decoder.load_progress(filename)
            input("\nНажмите Enter для продолжения...")

        elif choice == '6':
            if input("Вы уверены? (y/n): ").lower() == 'y':
                decoder.save_state()
                decoder.substitution_map = {char: char for char in decoder.all_alphabet}
                print("Все подстановки сброшены!")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()