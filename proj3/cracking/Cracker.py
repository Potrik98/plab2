from crypto.Cipher import Cipher
from cracking.KeyGenerator import KeyGenerator

class Cracker:
    def __init__(self,
                 cipher: Cipher,
                 key_gen: KeyGenerator,
                 words: set):
        self._cipher = cipher
        self._key_gen = key_gen
        self._dict = words
    
    def brute_force(self, text: str) -> None:
        for key in self._key_gen:
            self._cipher.set_key(key)
            decrypted = self._cipher.decrypt(text)
            score = 0
            for word in decrypted:
                if word in self._dict:
                    score += 1
            if score > 0:
                print("Score: %d, key: %s => %s" % (score, str(key), decrypted))
