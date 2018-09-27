class Cipher:
    class Key:
        def __init__(self):
            raise NotImplementedError
    
    def __init__(self):
        self._alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        self._characters = len(self._alphabet)

    def set_key(self, key: Key) -> None:
        self._key = key

    def encrypt(self, text: str) -> str:
        return ''.join(map(self._encrypt_character, text))

    def decrypt(self, text: str) -> str:
        return ''.join(map(self._decrypt_character, text))

    def _encrypt_character(self, char):
        raise NotImplementedError

    def _decrypt_character(self, char):
        raise NotImplementedError
