from bitcoin import *
import ecdsa
from ecdsa import SigningKey, SECP256k1 # cryptography lib for bitcoin addresses
import os

def keys_address():
    private_key = os.urandom(32)
    print("private key: ", binascii.hexlify(private_key).decode())
    signing_key = ecdsa.SigningKey.from_string(private_key, curve = ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()

    public_key = bytes.fromhex("04") + verifying_key.to_string()
    print("public key: ", binascii.hexlify(public_key).decode())

keys_address()
