from crypto.Cipher import Cipher

class KeyGenerator:
    def __iter__(self):
        return self

    def __next__(self) -> Cipher.Key:
        raise NotImplementedError
