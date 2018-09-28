from cracking.KeyGenerator import KeyGenerator
from crypto.Cipher import Cipher, alphabet_length
from crypto.MultiplicationCipher import MultiplicationCipher

class MultiplicationCipherKeyGenerator(KeyGenerator):
    def __init__(self):
        super().__init__()
        self._factor = 0

    def __iter__(self):
        return self

    def __next__(self) -> Cipher.Key:
        try:
            key = MultiplicationCipher.Key(factor=self._factor)
        except ValueError:
            self._factor += 1
            return self.__next__()
        self._factor += 1
        if self._factor > alphabet_length:
            raise StopIteration
        else:
            return key
