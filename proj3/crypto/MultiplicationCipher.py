from crypto.Cipher import Cipher, alphabet, alphabet_length
from crypto.SimpleCipher import SimpleCipher
from crypto.crypto_utils import modular_inverse

class MultiplicationCipher(SimpleCipher):
    class Key(Cipher.Key):
        def __init__(self, factor: int):
            self._factor = factor
            self._inverse = modular_inverse(factor, alphabet_length)
        
        def __str__(self):
            return "Multiplication key: factor %d, inverse %d" % (self._factor, self._inverse)

    def __init__(self):
        super().__init__()

    def _encrypt_character(self, char):
        return alphabet[(alphabet.index(char) * self._key._factor) % alphabet_length]

    def _decrypt_character(self, char):
        return alphabet[(alphabet.index(char) * self._key._inverse) % alphabet_length]
