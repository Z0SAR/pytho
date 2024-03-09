def vigenere_encrypt(plain_text, key):
    # Convert both plain text and key to uppercase
    plain_text = plain_text.upper()
    key = key.upper()

    encrypted_text = ""
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            # Shift char using the corresponding letter from the key
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    # Convert both encrypted text and key to uppercase
    encrypted_text = encrypted_text.upper()
    key = key.upper()

    decrypted_text = ""
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            # Shift char using the corresponding letter from the key
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char

    return decrypted_text

# Example usage:
plain_text = "HELLO"
key = "KEY"
encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
