class RSA:
    def __init__(self, p=61, q=67, e=13, d=2437):
        self.p = p
        self.q = q
        self.N = p * q
        self.e = e
        self.d = d


    def encrypt_text(self, plaintext):
        if not plaintext:
            raise ValueError("Текст не может быть пустым")

        encrypted_numbers = []
        for char in plaintext:
            m = ord(char)
            if m >= self.N:
                raise ValueError(f"Код символа '{char}' ({m}) >= N ({self.N}). "
                                 f"Невозможно зашифровать, так как нарушается условие RSA.")
            c = pow(m, self.e, self.N)
            encrypted_numbers.append(c)

        return encrypted_numbers


    def decrypt_numbers(self, numbers):
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")

        decrypted_chars = []
        for c in numbers:
            m = pow(c, self.d, self.N)
            try:
                char = chr(m)
            except ValueError:
                raise ValueError(f"Число {m} не соответствует ни одному символу Unicode")
            decrypted_chars.append(char)

        return ''.join(decrypted_chars)


    def encrypt_from_string(self, plaintext_string):
        numbers = self.encrypt_text(plaintext_string)
        return ' '.join(map(str, numbers))


    def decrypt_from_string(self, ciphertext_string):
        numbers = []
        for num_str in ciphertext_string.strip().split():
            try:
                numbers.append(int(num_str))
            except ValueError:
                raise ValueError(f"'{num_str}' не является целым числом")
        text = self.decrypt_numbers(numbers)
        return text