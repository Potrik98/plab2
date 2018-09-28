from crypto.Cipher import Cipher

class SimpleCipher(Cipher):
    def encrypt(self, text: str) -> str:
        return ''.join(map(self._encrypt_character, text))

    def decrypt(self, text: str) -> str:
        return ''.join(map(self._decrypt_character, text))

    def _encrypt_character(self, char):
        raise NotImplementedError

    def _decrypt_character(self, char):
        raise NotImplementedError
