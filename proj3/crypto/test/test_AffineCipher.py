import unittest

from crypto.AffineCipher import AffineCipher
from crypto.CaesarCipher import CaesarCipher
from crypto.MultiplicationCipher import MultiplicationCipher
from crypto.test.CipherTest import CipherTest

class AffineCipherTest(CipherTest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.run = unittest.TestCase.run.__get__(self, self.__class__)

    def _init_cipher(self):
        cipher = AffineCipher()
        caesar_key = CaesarCipher.Key(offset=3)
        multiplication_key = MultiplicationCipher.Key(factor=6)
        key = AffineCipher.Key(caesar_key, multiplication_key)
        cipher.set_key(key)
        return cipher
