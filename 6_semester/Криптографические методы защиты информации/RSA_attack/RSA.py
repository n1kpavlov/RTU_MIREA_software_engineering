import random
import math


class RSA:
    def __init__(self, p=None, q=None, e=None, d=None):
        if p and q:
            self.p = p
            self.q = q
        else:
            self.p, self.q = self.generate_primes()

        self.N = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        if e:
            self.e = e
        else:
            self.e = self.generate_e()

        if d:
            self.d = d
        else:
            self.d = self.mod_inverse(self.e, self.phi)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def generate_primes(bits=8):

        def get_prime():
            while True:
                p = random.randint(2 ** (bits - 1), 2 ** bits - 1)
                if RSA.is_prime(p):
                    return p

        p = get_prime()
        q = get_prime()
        while q == p:
            q = get_prime()
        return p, q

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def mod_inverse(a, m):

        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        gcd, x, _ = extended_gcd(a % m, m)
        if gcd != 1:
            raise ValueError("Модулярный обратный не существует")
        return (x % m + m) % m

    def generate_e(self):
        while True:
            e = random.randint(3, self.phi - 1)
            if self.gcd(e, self.phi) == 1:
                return e

    def encrypt_text(self, plaintext):
        if not plaintext:
            raise ValueError("Текст не может быть пустым")

        encrypted_numbers = []
        for char in plaintext:
            m = ord(char)
            if m >= self.N:
                raise ValueError(f"Код символа '{char}' ({m}) >= N ({self.N})")
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
                raise ValueError(f"Число {m} не соответствует символу Unicode")
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

    def get_public_key(self):
        return (self.N, self.e)

    def get_private_key(self):
        return (self.N, self.d)