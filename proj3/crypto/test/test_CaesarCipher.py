import unittest

from crypto.CaesarCipher import CaesarCipher
from crypto.test.CipherTest import CipherTest

class CaesarCipherTest(CipherTest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.run = unittest.TestCase.run.__get__(self, self.__class__)

    def _init_cipher(self):
        cipher = CaesarCipher()
        key = CaesarCipher.Key(offset=5)
        cipher.set_key(key)
        return cipher
