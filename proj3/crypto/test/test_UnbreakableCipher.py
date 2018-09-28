import unittest

from crypto.UnbreakableCipher import UnbreakableCipher
from crypto.test.CipherTest import CipherTest

class UnbreakableCipherTest(CipherTest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.run = unittest.TestCase.run.__get__(self, self.__class__)

    def _init_cipher(self):
        cipher = UnbreakableCipher()
        key = UnbreakableCipher.Key(code_word="Pizza")
        cipher.set_key(key)
        return cipher
