def product_cipher_transposition(text: str, key: str, encrypt: bool = True) -> str:
    shift = len(key) % 26

    def caesar(t, s):
        result = []
        for ch in t:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base + s) % 26 + base))
            else:
                result.append(ch)
        return ''.join(result)

    def get_col_order(k):
        return sorted(range(len(k)), key=lambda x: k[x])

    def columnar_encrypt(t, k):
        num_cols = len(k)
        num_rows = (len(t) + num_cols - 1) // num_cols
        padded = t + 'X' * (num_rows * num_cols - len(t))
        grid = [list(padded[i * num_cols:(i + 1) * num_cols]) for i in range(num_rows)]
        return ''.join(grid[row][col] for col in get_col_order(k) for row in range(num_rows))

    def columnar_decrypt(t, k):
        num_cols = len(k)
        num_rows = len(t) // num_cols
        col_order = get_col_order(k)
        grid = [''] * num_cols
        idx = 0
        for col in col_order:
            grid[col] = t[idx:idx + num_rows]
            idx += num_rows
        return ''.join(grid[col][row] for row in range(num_rows) for col in range(num_cols)).rstrip('X')

    if encrypt:
        return columnar_encrypt(caesar(text, shift), key)
    else:
        return caesar(columnar_decrypt(text, key), -shift)

ciphertext = product_cipher_transposition("HELLO WORLD", "SECRET", encrypt=True)
print("Encrypted:", ciphertext)

plaintext = product_cipher_transposition(ciphertext, "SECRET", encrypt=False)
print("Decrypted:", plaintext)
