import RabinCrypto


def main():
    rabin = RabinCrypto.RabinCrypto(p=139, q=191)

    message = "A"

    try:
        ciphertext, original_bits_len = rabin.encrypt_message(message)
        print(f"\nШифротекст c = {ciphertext}")

        decrypted = rabin.decrypt_message(ciphertext, original_bits_len)

        if decrypted:
            print(f"Сообщение успешно расшифровано: '{decrypted}'")
        else:
            print("\nНе удалось расшифровать сообщение")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()