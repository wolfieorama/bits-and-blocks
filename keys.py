from bitcoin import *
import ecdsa
from ecdsa import SigningKey, SECP256k1 # cryptography lib for bitcoin addresses
import hashlib
import base58
import os

def keys_address():
    private_key = os.urandom(32)
    print("private key: ", binascii.hexlify(private_key).decode())
    signing_key = ecdsa.SigningKey.from_string(private_key, curve = ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()

    public_key = bytes.fromhex("04") + verifying_key.to_string()
    print("public key: ", binascii.hexlify(public_key).decode())
    sha256_1 = hashlib.sha256(public_key)
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_1.digest())
    hashed_public_key = bytes.fromhex("00") + ripemd160.digest()
    print("hashed public key: ", binascii.hexlify(hashed_public_key).decode())
    check_sum_full = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()
    check_sum = check_sum_full[:4]
    bin_addr = hashed_public_key + check_sum
    final_bit_coin_address = base58.b58encode(bin_addr) #remove 0 and o for human readability
    print("Bit coin address is : ", final_bit_coin_address)

keys_address()
