import unittest

from crypto.Cipher import Cipher

class CipherTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = None
        self.run = lambda self, *args, **kwargs: None

    def _init_cipher(self) -> Cipher:
        raise NotImplementedError

    def test_encryption_and_decryption(self):
        cipher = self._init_cipher()
        text = "Lorem ipsum dolor sit amet"
        encrypted = cipher.encrypt(text)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(text, decrypted)
