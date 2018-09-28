from crypto.Cipher import Cipher
from crypto.AffineCipher import AffineCipher
from crypto.CaesarCipher import CaesarCipher
from crypto.MultiplicationCipher import MultiplicationCipher
from crypto.UnbreakableCipher import UnbreakableCipher
from cracking.KeyGenerator import KeyGenerator
from cracking.AffineCipherKeyGenerator import AffineCipherKeyGenerator
from cracking.CaesarCipherKeyGenerator import CaesarCipherKeyGenerator
from cracking.MultiplicationCipherKeyGenerator import MultiplicationCipherKeyGenerator
from cracking.UnbreakableCipherKeyGenerator import UnbreakableCipherKeyGenerator
from cracking.dict_utils import get_words_longer_than
import time

def get_key_generator(cipher: Cipher) -> KeyGenerator:
    if cipher.__class__ == AffineCipher:
        return AffineCipherKeyGenerator()
    if cipher.__class__ == CaesarCipher:
        return CaesarCipherKeyGenerator()
    if cipher.__class__ == MultiplicationCipher:
        return MultiplicationCipherKeyGenerator()
    if cipher.__class__ == UnbreakableCipher:
        return UnbreakableCipherKeyGenerator()

class Cracker:
    def __init__(self,
                 cipher: Cipher,
                 words=get_words_longer_than("word_list.txt", 3)):
        self._cipher = cipher
        self._key_gen = get_key_generator(cipher)
        self._dict = words
    
    def brute_force(self, text: str) -> str:
        t0 = time.time()
        for key in self._key_gen:
            self._cipher.set_key(key)
            decrypted = self._cipher.decrypt(text)
            score = 0
            for word in decrypted.split():
                if word in self._dict:
                    score += 1
            if score > 0:
                print("Score: %d, key: %s => %s" % (score, str(key), decrypted))
                if score > 5:
                    t1 = time.time()
                    print("Time used: %.6fs" % (t1 - t0))
                    return decrypted
        return ""
        t1 = time.time()
        print("Tried all combinations")
        print("Time used: %.6fs" % (t1 - t0))
