from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Key oluşturma
password = b'cEcXW4cEq5CKTexE' # Bu değeri 16 byte olacak şekilde istediğiniz gibi değiştirebilirsiniz
salt = get_random_bytes(16)

# Key üretme
key = PBKDF2(password, salt, dkLen=32)  # 256-bit key üret

# Rastgele IV oluşturma
iv = get_random_bytes(16)

# AES cipher objesi oluşturma (CBC)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Şifrelenecek metin
plaintext = b'print("Hello World")'

# Şifreleme
padded_plaintext = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_plaintext)

# DecryptAES.py dosyasında kullanacağımız değerler
print("IV:", iv)
print("Key:",key)
print("Şifreli Metin:", ciphertext)