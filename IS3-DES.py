from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
def encrypt_message(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return ciphertext.hex()
def decrypt_message(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_plaintext = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), DES.block_size)
    return decrypted_plaintext.decode()
plaintext = "Hello, World!"
key = b"secretkey"

encrypted_message = encrypt_message(plaintext, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)
