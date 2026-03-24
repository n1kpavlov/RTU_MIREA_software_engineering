class RabinCrypto:
    def __init__(self, p=139, q=191):
        self.p = p
        self.q = q
        self.n = p * q

        if not (p % 4 == 3 and q % 4 == 3):
            raise ValueError("p и q должны быть сравнимы с 3 по модулю 4")

    def text_to_bits(self, text):
        bits = bin(ord(text))[2:]
        return bits

    def bits_to_text(self, bits):
        bytes_list = [bits[i:i + 8] for i in range(0, len(bits), 8)]
        text = ''.join(chr(int(byte, 2)) for byte in bytes_list)
        return text

    def duplicate_bits(self, bits):
        return bits + bits

    def bits_to_number(self, bits):
        return int(bits, 2)

    def number_to_bits(self, num, length=None):
        bits = bin(num)[2:]
        if length and len(bits) < length:
            bits = '0' * (length - len(bits)) + bits
        return bits

    def encrypt(self, m):
        c = pow(m, 2, self.n)
        return c

    def decrypt(self, c):
        p1 = pow(self.p, -1, self.q)
        q1 = pow(self.q, -1, self.p)

        c1 = pow(c, (self.p + 1) // 4, self.p)
        c2 = pow(c, (self.q + 1) // 4, self.q)

        r1 = (c1 * self.q * q1 + c2 * self.p * p1) % self.n
        r2 = (c1 * self.q * q1 - c2 * self.p * p1) % self.n
        r3 = (-c1 * self.q * q1 + c2 * self.p * p1) % self.n
        r4 = (-c1 * self.q * q1 - c2 * self.p * p1) % self.n

        roots = set([r1, r2, r3, r4])
        print(f"Возможные корни (расшифрованные сообщения): {roots}")

        return roots

    def find_correct_message(self, roots, original_bits_length):
        original_length = original_bits_length
        expected_length = original_length * 2

        for root in roots:
            bits = self.number_to_bits(root, expected_length)

            if len(bits) == expected_length:
                first_half = bits[:original_length]
                second_half = bits[original_length:]

                if first_half == second_half:
                    return first_half

        return None

    def encrypt_message(self, message):
        original_bits = self.text_to_bits(message)
        print(f"Исходное сообщение: {message}")
        print(f"ASCII биты: {original_bits}")

        duplicated_bits = self.duplicate_bits(original_bits)

        m = self.bits_to_number(duplicated_bits)
        print(f"\nЧисловое представление m: {m}")

        c = self.encrypt(m)

        return c, len(original_bits)

    def decrypt_message(self, c, original_bits_length):
        roots = self.decrypt(c)

        original_bits = self.find_correct_message(roots, original_bits_length)

        if original_bits is None:
            print("Не удалось найти корректное сообщение среди корней!")
            return None

        message = self.bits_to_text(original_bits)
        print(f"\nВосстановленное сообщение: {message}")

        return message