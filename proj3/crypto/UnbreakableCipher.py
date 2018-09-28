from crypto.Cipher import Cipher, alphabet, alphabet_length

class UnbreakableCipher(Cipher):
    class Key(Cipher.Key):
        def __init__(self, code_word: str):
            self._code = list(map(lambda c: alphabet.index(c), code_word))
            self._reverse_code = list(map(lambda c: (alphabet_length - alphabet.index(c)) % alphabet_length, code_word))
            self._code_length = len(self._code)

        def get_code_value(self, position: int) -> int:
            return self._code[position % self._code_length]

        def get_reverse_code_value(self, position: int) -> int:
            return self._reverse_code[position % self._code_length]

        def __str__(self):
            return "Unbreakable key: code word: '%s'" % ''.join(map(lambda c: alphabet[c], self._code))

    def __init__(self):
        super().__init__()

    def encrypt(self, text: str) -> str:
        res = ""
        for i in range(len(text)):
            res += alphabet[(alphabet.index(text[i]) + self._key.get_code_value(i)) % alphabet_length]
        return res


    def decrypt(self, text: str) -> str:
        res = ""
        for i in range(len(text)):
            res += alphabet[(alphabet.index(text[i]) + self._key.get_reverse_code_value(i)) % alphabet_length]
        return res
