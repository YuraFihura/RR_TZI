class Twofish:
    BLOCK_SIZE = 16  # Розмір блоку 16 байт

    def __init__(self, key):
        self.key = key.ljust(self.BLOCK_SIZE, b'\x00')[:self.BLOCK_SIZE]  # Підгонка ключа до 16 байт

    def encrypt_block(self, block):
        return bytes([b ^ k for b, k in zip(block, self.key)])

    def decrypt_block(self, block):
        return bytes([b ^ k for b, k in zip(block, self.key)])

    def encrypt(self, plaintext):
        padded_data = self.pad(plaintext)
        return b''.join(self.encrypt_block(padded_data[i:i + self.BLOCK_SIZE])
                        for i in range(0, len(padded_data), self.BLOCK_SIZE))

    def decrypt(self, ciphertext):
        decrypted_data = b''.join(self.decrypt_block(ciphertext[i:i + self.BLOCK_SIZE])
                                  for i in range(0, len(ciphertext), self.BLOCK_SIZE))
        return self.unpad(decrypted_data)

    def pad(self, data):
        padding_len = self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE
        return data + bytes([padding_len] * padding_len)

    def unpad(self, data):
        padding_len = data[-1]
        return data[:-padding_len]

# Приклад використання
if __name__ == "__main__":
    key = b'secretkey1234567'  # 16-байтний ключ
    tf = Twofish(key)

    plaintext = input("Введіть текст для шифрування: ").encode()
    encrypted = tf.encrypt(plaintext)
    print(f"Зашифрований текст: {encrypted.hex()}")

    decrypted = tf.decrypt(encrypted)
    print(f"Розшифрований текст: {decrypted.decode()}")
