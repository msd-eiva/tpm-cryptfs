#!/usr/bin/env python3
#coding: UTF-8

'''
The simple encryption/decryption for secret info
'''

import logging
import argparse
import struct

SECRET_XOR_BYTE_CODE = 0x48

class Secret():
    def encrypt(self, input):
        _ = SECRET_XOR_BYTE_CODE

        input = bytes(input)
        out = str()
        for b in input:
            b = struct.unpack('<1B', b)[0]
            _ = b ^ _
            out = out + struct.pack('<1B', _)

        return out
             
    def decrypt(self, input):
        _ = SECRET_XOR_BYTE_CODE

        input = bytes(input)
        out = str()
        for b in input:
            b = struct.unpack('<1B', b)[0]
            out = out + struct.pack('<1B', b ^ _)
            _ = b

        return out

logging.basicConfig(level=logging.DEBUG, \
                    format="[%(asctime)s] %(levelname)s: %(message)s")

parser = argparse.ArgumentParser(description='Simple encryption/decryption for secret info')
parser.add_argument('-i', '--input', dest='secret',
                    help='Input secret info', required=True)

args = parser.parse_args()
try:
    print(Secret().encrypt(args.secret), end='')
except:
    logging.error("Unable to encrypt the secret")
