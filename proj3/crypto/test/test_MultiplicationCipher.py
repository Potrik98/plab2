import unittest

from crypto.MultiplicationCipher import MultiplicationCipher
from crypto.test.CipherTest import CipherTest

class MultiplicationCipherTest(CipherTest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.run = unittest.TestCase.run.__get__(self, self.__class__)

    def _init_cipher(self):
        cipher = MultiplicationCipher()
        key = MultiplicationCipher.Key(factor=11)
        cipher.set_key(key)
        return cipher
