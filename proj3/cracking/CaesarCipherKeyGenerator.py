from cracking.KeyGenerator import KeyGenerator
from crypto.Cipher import Cipher, alphabet_length
from crypto.CaesarCipher import CaesarCipher

class CaesarCipherKeyGenerator(KeyGenerator):
    def __init__(self):
        super().__init__()
        self._offset = 0

    def __iter__(self):
        return self

    def __next__(self) -> Cipher.Key:
        key = CaesarCipher.Key(offset=self._offset)
        self._offset += 1
        if self._offset > alphabet_length:
            raise StopIteration
        else:
            return key
