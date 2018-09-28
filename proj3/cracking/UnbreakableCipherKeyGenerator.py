from cracking.KeyGenerator import KeyGenerator
from crypto.Cipher import Cipher, alphabet_length
from crypto.UnbreakableCipher import UnbreakableCipher
from cracking.dict_utils import get_complete_word_list

class UnbreakableCipherKeyGenerator(KeyGenerator):
    def __init__(self, words=get_complete_word_list("word_list.txt")):
        super().__init__()
        self._word_iterator = iter(words)

    def __iter__(self):
        return self

    def __next__(self) -> Cipher.Key:
        word = self._word_iterator.__next__()
        return UnbreakableCipher.Key(code_word=word)
