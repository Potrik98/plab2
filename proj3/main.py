from crypto import *
from cracking import *

# initial text is today's featured article on wikipedia
initial_text = "Myst IV: Revelation is an adventure video game, the fourth installment in the Myst series, developed and published by Ubisoft. Revelation was the first game in the series released on a DVD-ROM format; a multiple CD-ROM version was not produced as it would have taken twelve compact discs to fit the data.[1] Like Myst III: Exile, Revelation combines pre-rendered graphics with digital video, but also features real-time 3D effects for added realism."

def crack_caesar():
    cipher = CaesarCipher.CaesarCipher()
    key = CaesarCipher.CaesarCipher.Key(offset=34)
    cipher.set_key(key)

    encrypted_text = cipher.encrypt(initial_text)
    print("Encrypted text:")
    print(encrypted_text)

    print("Starting brute force\n")

    filename = "word_list.txt"
    length = 3
    words = dict_utils.get_words_longer_than(filename, length)
    key_gen = CaesarCipherKeyGenerator.CaesarCipherKeyGenerator()
    cracker = Cracker.Cracker(cipher, key_gen, words)

    cracker.brute_force(encrypted_text)

def crack_multiplication():
    cipher = MultiplicationCipher.MultiplicationCipher()
    key = MultiplicationCipher.MultiplicationCipher.Key(factor=33)
    cipher.set_key(key)

    encrypted_text = cipher.encrypt(initial_text)
    print("Encrypted text:")
    print(encrypted_text)

    print("Starting brute force\n")

    filename = "word_list.txt"
    length = 3
    words = dict_utils.get_words_longer_than(filename, length)
    key_gen = MultiplicationCipherKeyGenerator.MultiplicationCipherKeyGenerator()
    cracker = Cracker.Cracker(cipher, key_gen, words)

    cracker.brute_force(encrypted_text)

crack_multiplication()
