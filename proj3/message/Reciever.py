from message.Person import Person
from crypto.Cipher import Cipher

class Reciever(Person):
    def __init__(self, cipher: Cipher):
        super().__init__(cipher)

    def operate_cipher(self, text: str) -> str:
        return self._cipher.decrypt(str)
