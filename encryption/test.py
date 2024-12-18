from cipher import encipher as encrypt
from decipher import decipher as decrypt
import unittest

plain_text = "I Love Coding"
known_word = "Love"
key = 4
cipher_text = "M$Pszi$Gshmrk"

class TestEncryption(unittest.TestCase):
    def test_encryption(self):
        encrypted_text = encrypt(plain_text, key)
        self.assertEqual(encrypted_text, cipher_text)

    def test_decryption(self):
        decrypted_text = decrypt(cipher_text, known_word)
        self.assertEqual(plain_text, decrypted_text)


if __name__ == "__main__":
    unittest.main()