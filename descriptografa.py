import os
import pyaes

# Chave para descriptografia
key = b"ransomwareprofjv"
aes = pyaes.AESModeOfOperationCTR(key)

# Abrir, ler e descriptografar o arquivo
with open("demo.txt.ransompjv", "rb") as file:
    decrypt_data = aes.decrypt(file.read())

# Remover o arquivo criptografado
os.remove("demo.txt.ransompjv")

# Criar o arquivo descriptografado
with open("demo.txt", "wb") as new_file:
    new_file.write(decrypt_data)
