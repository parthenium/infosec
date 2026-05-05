def create_key_order(keyword):
    """
    Assigns numbers to each letter in the keyword based on alphabetical order.
    Example: ZEBRA -> [5,3,1,4,2]
    """
    return [sorted(keyword).index(c) + 1 for c in keyword]

def encrypt(plaintext, keyword):
    key_order = create_key_order(keyword)
    n = len(keyword)

    while len(plaintext) % n != 0:
        plaintext += "X"

    rows = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]

    ciphertext = ""
    for num in sorted(set(key_order)):
        col_index = key_order.index(num)
        for row in rows:
            ciphertext += row[col_index]

    return ciphertext

def decrypt(ciphertext, keyword):
    key_order = create_key_order(keyword)
    n = len(keyword)
    rows = len(ciphertext) // n

    matrix = [[""] * n for _ in range(rows)]

    idx = 0
    for num in sorted(set(key_order)):
        col_index = key_order.index(num)
        for r in range(rows):
            matrix[r][col_index] = ciphertext[idx]
            idx += 1

    plaintext = "".join("".join(row) for row in matrix)
    return plaintext

plaintext = input("Enter plaintext: ").replace(" ", "").upper()
keyword = input("Enter keyword: ").upper()

cipher = encrypt(plaintext, keyword)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, keyword)
print("Decrypted:", decrypted)
