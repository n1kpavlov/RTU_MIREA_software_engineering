class CustomHash:
    def __init__(self, z0=0):
        self.z0 = z0 & 0xFFFF
        self.block_size = 16


    def string_to_bits(self, text):
        if isinstance(text, str):
            text = text.encode('utf-8')

        bits = ''
        for byte in text:
            bits += format(byte, '08b')

        return bits


    def bits_to_integer(self, bits):
        if len(bits) > 16:
            bits = bits[:16]
        elif len(bits) < 16:
            bits = bits.ljust(16, '0')

        return int(bits, 2)


    def split_into_blocks(self, bits):
        blocks = []

        for i in range(0, len(bits), 16):
            block_bits = bits[i:i + 16]
            if len(block_bits) < 16:
                block_bits = block_bits + '1' + '0' * (15 - len(block_bits))

            blocks.append(self.bits_to_integer(block_bits))

        return blocks


    def add_length_block(self, blocks, original_text):
        if isinstance(original_text, str):
            length = len(original_text.encode('utf-8'))
        else:
            length = len(original_text)

        length_block = length & 0xFFFF
        blocks.append(length_block)

        return blocks


    def hash(self, text):
        bits = self.string_to_bits(text)
        blocks = self.split_into_blocks(bits)
        blocks = self.add_length_block(blocks, text)

        z = self.z0
        for i, block in enumerate(blocks):
            z_next = (z ^ block) & 0xFFFF
            z = z_next

        return f"{z:04X}"


if __name__ == "__main__":
    hasher = CustomHash(z0=0x1234)
    text = "qwerty"
    result = hasher.hash(text)
    print(result)
