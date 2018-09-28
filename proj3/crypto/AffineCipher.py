from crypto.Cipher import Cipher, alphabet, alphabet_length
from crypto.MultiplicationCipher import MultiplicationCipher
from crypto.CaesarCipher import CaesarCipher

class AffineCipher(Cipher):
    class Key(Cipher.Key):
        def __init__(self,
                     caesar_key: CaesarCipher.Key,
                     multiplication_key: MultiplicationCipher.Key):
            self._caesar_key = caesar_key
            self._multiplication_key = multiplication_key

    def __init__(self):
        super().__init__()
        self._caesar_cipher = CaesarCipher()
        self._multiplication_cipher = MultiplicationCipher()

    def set_key(self, key: Key):
        self._caesar_cipher.set_key(key._caesar_key)
        self._multiplication_cipher.set_key(key._multiplication_key)

    def _encrypt_character(self, char):
        return self._caesar_cipher._encrypt_character(
            self._multiplication_cipher._encrypt_character(char))

    def _decrypt_character(self, char):
        return self._multiplication_cipher._decrypt_character(
            self._caesar_cipher._decrypt_character(char))
