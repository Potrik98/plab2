from crypto.SimpleCipher import SimpleCipher
from crypto.Cipher import Cipher, alphabet, alphabet_length

class CaesarCipher(SimpleCipher):
    class Key(Cipher.Key):
        def __init__(self, offset: int):
            self._offset = offset

        def __str__(self):
            return "Caesar key: offset %d" % self._offset

    def __init__(self):
        super().__init__()

    def _encrypt_character(self, char):
        return alphabet[(alphabet.index(char) + self._key._offset) % alphabet_length]

    def _decrypt_character(self, char):
        return alphabet[(alphabet.index(char) - self._key._offset) % alphabet_length]
