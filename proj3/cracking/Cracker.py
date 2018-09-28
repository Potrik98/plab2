from crypto.Cipher import Cipher
from cracking.KeyGenerator import KeyGenerator
import time

class Cracker:
    def __init__(self,
                 cipher: Cipher,
                 key_gen: KeyGenerator,
                 words: set):
        self._cipher = cipher
        self._key_gen = key_gen
        self._dict = words
    
    def brute_force(self, text: str) -> None:
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
                    return
        t1 = time.time()
        print("Tried all combinations")
        print("Time used: %.6fs" % (t1 - t0))
