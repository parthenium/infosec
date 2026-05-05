#Encryption
def rail_fence_encrypt(text, rails):
    if rails <= 1:
        return text

    # Create empty rails
    fence = ['' for _ in range(rails)]
    
    rail = 0
    direction = 1  # 1 = down, -1 = up

    for char in text:
        fence[rail] += char
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(fence)

# Example
plaintext = "glass roads"
cipher = rail_fence_encrypt(plaintext, 3)
print(cipher)

#Decryption
def rail_fence_decrypt(cipher, rails):
    if rails <= 1:
        return cipher

    # Step 1: Create pattern
    pattern = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        pattern[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Step 2: Fill the pattern with cipher text
    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if pattern[r][c] == '*' and index < len(cipher):
                pattern[r][c] = cipher[index]
                index += 1

    # Step 3: Read zig-zag to reconstruct original text
    result = []
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        result.append(pattern[rail][i])
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(result)

# Example
decoded = rail_fence_decrypt(cipher, 3)
print(decoded)
