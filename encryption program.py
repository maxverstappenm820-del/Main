#encryption program 

import string
import random

chars = " " + string.ascii_letters + string.digits + string.punctuation

print("Welcome to the Encryption Program!")
#print(chars)

cahrs_list = list(chars)
key= chars_list = list(chars)

random.shuffle(key)

#encryption

plain_text = input("Enter the text you want to encrypt: ")
cipher_text = ""
for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]

print(F"Original Text: {plain_text}")
print(F"Encrypted Text: {cipher_text}")

#decryption
decrypt_text = ""
cipher_text = input("Enter the text you want to decrypt: ")
for char in cipher_text:
    index = key.index(char)
    decrypt_text += chars[index]
print(F"Decrypted Text: {decrypt_text}")



