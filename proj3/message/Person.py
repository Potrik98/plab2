from crypto.Cipher import Cipher

class Person:
    def __init__(self, cipher: Cipher):
        self._cipher = cipher

    def set_key(self, key: Cipher.Key) -> None:
        self._cipher.set_key(key)

    def operate_cipher(self, text: str) -> str:
        raise NotImplementedError
