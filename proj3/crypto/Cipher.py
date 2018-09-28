alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
alphabet_length = len(alphabet)

class Cipher:
    class Key:
        def __init__(self):
            raise NotImplementedError

    def set_key(self, key: Key) -> None:
        self._key = key

    def encrypt(self, text: str) -> str:
        raise NotImplementedError

    def decrypt(self, text: str) -> str:
        raise NotImplementedError
