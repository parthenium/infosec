#Monoalphabetic Cipher
import string


# Create substitution mapping
def create_substitution_cipher(key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    cipher_map = dict(zip(alphabet, key))
    return cipher_map


# Encrypt function
def mono_encrypt(plaintext, cipher_map):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char in cipher_map:
            ciphertext += cipher_map[char]
        else:
            ciphertext += char
    return ciphertext


# Decrypt function
def mono_decrypt(ciphertext, cipher_map):
    reverse_map = {v: k for k, v in cipher_map.items()}
    plaintext = ""
    for char in ciphertext:
        if char in reverse_map:
            plaintext += reverse_map[char]
        else:
            plaintext += char
    return plaintext


# Example Key (26 unique letters)
key = "QWERTYUIOPASDFGHJKLZXCVBNM"


cipher_map = create_substitution_cipher(key)


text = "HELLO WORLD"
encrypted = mono_encrypt(text, cipher_map)
decrypted = mono_decrypt(encrypted, cipher_map)


print("Plaintext:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)


#Polyalphabetic Cipher
import string


def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0


    for char in plaintext:
        if char in string.ascii_uppercase:
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char


    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_index = 0


    for char in ciphertext:
        if char in string.ascii_uppercase:
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char


    return plaintext


# Example
text = "HELLO WORLD"
key = "KEY"


encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)


print("Plaintext:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
