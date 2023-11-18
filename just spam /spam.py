from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = plaintext + " " * (8 - len(plaintext) % 8)  # Pad to multiple of 8 bytes
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def decrypt_des(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b" ").decode()

key = get_random_bytes(8)  
message = "Meet me very urgently"
encrypted_message = encrypt_des(key, message)
print("Encrypted:", encrypted_message.hex())

decrypted_message = decrypt_des(key, encrypted_message)
print("Decrypted:", decrypted_message)

