from crypto.Cipher import Cipher
from cracking.Cracker import Cracker, get_key_generator

class Hacker:
    def brute_force(self, text: str, cipher: Cipher) -> str:
        cracker = Cracker(cipher)
        cracker.brute_force(text)
