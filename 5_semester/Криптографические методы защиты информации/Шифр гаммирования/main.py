from generate_gamma import bbs_generator


def text_to_bits(text, encoding='utf-8'):
    bytes_data = text.encode(encoding)
    bits_string = ''.join(format(byte, '08b') for byte in bytes_data)
    return bits_string


def bits_to_text(bits_string, encoding='utf-8'):
    bytes_list = []
    for i in range(0, len(bits_string), 8):
        byte_bits = bits_string[i:i + 8]
        byte_val = int(byte_bits, 2)
        bytes_list.append(byte_val)

    bytes_data = bytes(bytes_list)
    return bytes_data.decode(encoding)


def encrypt_decrypt_bits(text_bits, gamma_bits):
    result_bits = ''
    for i in range(len(text_bits)):
        result_bits += str((int(text_bits[i]) + int(gamma_bits[i])) % 2)
    return result_bits


def encrypt(input_file, output_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as f:
        plaintext = f.read()

    plaintext_bits = text_to_bits(plaintext, encoding)

    gamma_bits = bbs_generator(len(plaintext_bits), "encrypt")

    cipher_bits = encrypt_decrypt_bits(plaintext_bits, gamma_bits)
    ciphertext = bits_to_text(cipher_bits, encoding)

    with open(output_file, 'w', encoding=encoding) as f:
        f.write(ciphertext)
    print(f"Шифротекст записан в файл: '{output_file}'")


def decrypt(input_file, output_file, param_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as f:
        ciphertext = f.read()

    ciphertext_bits = text_to_bits(ciphertext, encoding)

    gamma_bits = bbs_generator(len(ciphertext_bits), "decrypt", param_file)

    decrypted_bits = encrypt_decrypt_bits(ciphertext_bits, gamma_bits)
    decrypted_text = bits_to_text(decrypted_bits, encoding)

    with open(output_file, 'w', encoding=encoding) as f:
        f.write(decrypted_text)
    print(f"Расшифрованный текст записан в файл: '{output_file}'")


if __name__ == "__main__":

    while True:
        print("1 - Зашифровать файл\n"
              "2 - Расшифровать файл\n"
              "0 - Завершить работу")

        mode = input()

        match mode:
            case "1":
                print("Исходный файл:")
                input_file = input()

                encrypt(input_file, "encrypted.txt", encoding='koi8-r')

            case "2":
                print("Зашифрованный файл:")
                encrypted_file = input()
                print("Файл с параметрами гаммы:")
                param_file = input()

                decrypt(encrypted_file, "decrypted.txt", param_file, encoding='koi8-r')

            case "0": break
            case _: print("Некорректный выбор")