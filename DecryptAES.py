from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
import sys

# Sabit değerler (anahtar ve IV)
iv = b''  # IV
key = b'' # Key

# Şifreli metin (EncryptAES.py'den alınacak)
ciphertext = b''

# AES şifreli objesi oluşturma (CBC)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Şifre çözme
decrypted_text = cipher.decrypt(ciphertext)
try:
    unpadded_text = unpad(decrypted_text, AES.block_size)
    print("Çözülen Metin:", unpadded_text.decode('utf-8'))
    exec(unpadded_text.decode('utf-8')) # Çözülen metni çalıştır
except ValueError as e:
    sys.exit
