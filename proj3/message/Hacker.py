from message.Person import Person
from crypto.Cipher import Cipher
from cracking.Cracker import Cracker, get_key_generator

class Hacker(Person):
    def __init__(self):
        super().__init__(None)

    def operate_cipher(self, text: str, cipher: Cipher) -> str:
        cracker = Cracker(cipher)
        cracker.brute_force(text)
