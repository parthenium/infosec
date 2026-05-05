def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()


    for c in key:
        if c.isalpha() and c not in used:
            matrix.append(c)
            used.add(c)


    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J removed
        if c not in used:
            matrix.append(c)
            used.add(c)


    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_pos(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0


    while i < len(text):
        a = text[i]
        b = ""


        if i + 1 < len(text):
            b = text[i+1]


        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a
            if b:
                result += b
                i += 2
            else:
                result += "X"
                i += 1


    return result


def encrypt(text, matrix):
    text = prepare_text(text)
    cipher = ""


    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]


        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)


        if r1 == r2:
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]


        elif c1 == c2:
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]


        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]


    return cipher


def decrypt(text, matrix):
    plain = ""


    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]


        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)


        if r1 == r2:
            plain += matrix[r1][(c1-1) % 5]
            plain += matrix[r2][(c2-1) % 5]


        elif c1 == c2:
            plain += matrix[(r1-1) % 5][c1]
            plain += matrix[(r2-1) % 5][c2]


        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]


    return plain


# ===== Example =====


key = "MONARCHY"
text = "HELLO"


matrix = create_matrix(key)


print("Key Matrix:")
for row in matrix:
    print(row)


cipher = encrypt(text, matrix)
print("Encrypted:", cipher)


plain = decrypt(cipher, matrix)
print("Decrypted:", plain)
