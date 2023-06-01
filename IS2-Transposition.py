def encrypt_message(plaintext, key):   
    plaintext = plaintext.replace(" ", "").upper()  
    num_rows = -(-len(plaintext) // key)   
    padded_plaintext = plaintext.ljust(num_rows * key, 'X')
    ciphertext = ''
    for column in range(key):
        for row in range(num_rows):
            index = column + row * key
            ciphertext += padded_plaintext[index]

    return ciphertext


def decrypt_message(ciphertext, key):
    num_rows = -(-len(ciphertext) // key)  
    grid = [[''] * key for _ in range(num_rows)]
    index = 0
    for column in range(key):
        for row in range(num_rows):
            grid[row][column] = ciphertext[index]
            index += 1

    plaintext = ''
    for row in range(num_rows):
        for column in range(key):
            plaintext += grid[row][column]

    return plaintext

plaintext = "HELLO"
key = 4
ciphertext = encrypt_message(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt_message(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
