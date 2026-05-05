import numpy as np


# Convert letter to number (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    text = text.upper().replace(" ", "")
    return [ord(c) - ord('A') for c in text]


# Convert numbers back to letters
def numbers_to_text(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)


# Encrypt function
def hill_encrypt(plain_text, key_matrix):
    nums = text_to_numbers(plain_text)


    # Make length even (for 2x2)
    if len(nums) % 2 != 0:
        nums.append(23)  # X padding


    cipher = []


    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        result = np.dot(key_matrix, pair) % 26
        cipher.extend(result.flatten())


    return numbers_to_text(cipher)


# Find modular inverse of determinant
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# Decrypt function
def hill_decrypt(cipher_text, key_matrix):
    nums = text_to_numbers(cipher_text)


    det = int(np.linalg.det(key_matrix))
    det = det % 26


    det_inv = mod_inverse(det, 26)


    if det_inv is None:
        print("Key not invertible")
        return ""


    # Inverse of 2x2 matrix
    inv_matrix = np.array([
        [key_matrix[1][1], -key_matrix[0][1]],
        [-key_matrix[1][0], key_matrix[0][0]]
    ])


    inv_matrix = (det_inv * inv_matrix) % 26


    plain = []


    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        result = np.dot(inv_matrix, pair) % 26
        plain.extend(result.flatten())


    return numbers_to_text(plain)


# Example key (must be invertible mod 26)
key = np.array([[3, 3],
                [2, 5]])


text = "balright"


cipher = hill_encrypt(text, key)
print("Encrypted:", cipher)


decrypted = hill_decrypt(cipher, key)
print("Decrypted:", decrypted)
