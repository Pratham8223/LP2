from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_message(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext.hex()

def decrypt_message(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_plaintext = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), AES.block_size)
    return decrypted_plaintext.decode()

# Example usage
plaintext = "Hello, World!"
key = b"secretaeskey1234"

encrypted_message = encrypt_message(plaintext, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)
