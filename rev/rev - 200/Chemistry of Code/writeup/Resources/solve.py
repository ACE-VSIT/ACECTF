from base64 import b64decode
from binascii import unhexlify, hexlify
from Crypto.Util.number import bytes_to_long, long_to_bytes

FERROUS_OXIDE_USERNAME = "AdminFeroxide"
ANIONIC_PASSWORD = "NjQzMzcyNzUzNTM3MzE2Njc5MzE2ZTM2"
ALKALINE_SECRET = "4143454354467B34707072336E373163335F3634322C28010D3461302C392E"

# Decode the password
anionic_password_hex = b64decode(ANIONIC_PASSWORD).decode()
password = unhexlify(anionic_password_hex).decode()

# Convert inputs to hex
cation_hex = hexlify(FERROUS_OXIDE_USERNAME.encode()).decode()
anion_hex = anionic_password_hex

# XOR operations
cation_value = bytes_to_long(unhexlify(cation_hex))
anion_value = bytes_to_long(unhexlify(anion_hex))
alkaline_secret_value = bytes_to_long(unhexlify(ALKALINE_SECRET))

covalent_link = cation_value ^ anion_value
metallic_alloy = covalent_link ^ alkaline_secret_value

# Convert to ASCII
precipitate = hex(metallic_alloy)[2:]
alloy_compound = ''.join(
    chr(int(precipitate[i:i+2], 16)) for i in range(0, len(precipitate), 2)
)

print("Flag:", alloy_compound)
