from crypto.Cipher import Cipher, alphabet, alphabet_length
from crypto.crypto_utils import modular_inverse

class MultiplicationCipher(Cipher):
    class Key(Cipher.Key):
        def __init__(self, factor: int):
            self._factor = factor
            self._inverse = modular_inverse(factor, alphabet_length)

    def __init__(self):
        super().__init__()

    def _encrypt_character(self, char):
        return alphabet[(alphabet.index(char) * self._key._factor) % alphabet_length]

    def _decrypt_character(self, char):
        return alphabet[(alphabet.index(char) * self._key._inverse) % alphabet_length]
