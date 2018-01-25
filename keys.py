from bitcoin import *
import os

def keys_address():
    private_key = os.urandom(32)
    print("private key: ", binascii.hexlify(private_key).decode())

keys_address()
