import Crypto.Util.number as number

def generate_key_pair(key_size):
    p = number.getPrime(key_size)
    q = number.getPrime(key_size)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537  # commonly used public exponent
    d = number.inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt_message(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt_message(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Example usage
plaintext = "Hello, World!"
key_size = 1024

public_key, private_key = generate_key_pair(key_size)

encrypted_message = encrypt_message(plaintext, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
