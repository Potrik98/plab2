from crypto.Cipher import Cipher

class CaesarCipher(Cipher):
    class Key(Cipher.Key):
        def __init__(self, offset: int):
            self._offset = offset

    def __init__(self):
        super().__init__()

    def _encrypt_character(self, char):
        return self._alphabet[(self._alphabet.index(char) + self._key._offset) % self._characters]

    def _decrypt_character(self, char):
        return self._alphabet[(self._alphabet.index(char) - self._key._offset) % self._characters]
