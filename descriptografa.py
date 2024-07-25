import os
import pyaes

## Abre o arquivo criptografado
file_name = "demo.txt.ransompjv"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave para descriptografia
key = b"ransomwareprofjv"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remove o arquivo criptografado
os.remove(file_name)

## Cria o arquivo descriptografado
new_file = "demo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
