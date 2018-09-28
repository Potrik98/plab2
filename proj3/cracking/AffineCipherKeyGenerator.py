from cracking.KeyGenerator import KeyGenerator
from cracking.CaesarCipherKeyGenerator import CaesarCipherKeyGenerator
from cracking.MultiplicationCipherKeyGenerator import MultiplicationCipherKeyGenerator
from crypto.Cipher import Cipher, alphabet_length
from crypto.AffineCipher import AffineCipher

class AffineCipherKeyGenerator(KeyGenerator):
    def __init__(self):
        super().__init__()
        self._caesar_key_gen = CaesarCipherKeyGenerator()
        self._multi_key_gen = MultiplicationCipherKeyGenerator()
        self._caesar_key = self._caesar_key_gen.__next__()

    def __iter__(self):
        return self

    def __next__(self) -> Cipher.Key:
        try:
            multi_key = self._multi_key_gen.__next__()
            return AffineCipher.Key(self._caesar_key, multi_key)
        except StopIteration:
            self._caesar_key = self._caesar_key_gen.__next__()
            self._multi_key_gen = MultiplicationCipherKeyGenerator()
            return self.__next__()
