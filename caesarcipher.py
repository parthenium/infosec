def encrypt(text, offset):
  result = ""


  for i in range(len(text)):
    char = text[i]


    if char.isupper():
      result += chr((ord(char) + offset - 65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + offset - 97) % 26 + 97)
    else:
      result += char
  return result




def decrypt(text, offset):
  return encrypt(text, -offset)
text = input("Enter the text to encrypt: ")
offset = int(input("Enter the offset for encryption: "))


encrypted = encrypt(text, offset)
print("Encrypted text is:-", encrypted)


decrypted = decrypt(encrypted, offset)
print("Decrypted text is:-", decrypted)
