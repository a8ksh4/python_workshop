import os
from base64 import b64encode, b64decode
from hashlib import sha1, sha256
from Crypto.Cipher import AES
from Crypto import Random
from random import randint
import yaml

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def encode_solution(soultion):
    return b64encode(soultion.encode('ascii')).decode('utf-8')
    
def encode_message(message, key=b'Sixteen byte key'):
    key = key.zfill(16)[:16]
    message = message.encode('ascii')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return b64encode(iv + cipher.encrypt(message)).decode('utf-8')
    
def decode_message(b64coded_message, key=b'Sixteen byte key'):
    key = key.zfill(16)[:16]
    coded_message = b64decode(b64coded_message.encode('ascii'))
    iv = coded_message[:16]
    message = coded_message[16:]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(message).decode('utf-8')
       
def hash_results(results, token='0'):
    hash = sha1(token.encode('ascii'))
    for result in results:
        hash.update(str(result).encode('ascii'))
    return hash.hexdigest()

def save_yml(filepath, data):
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def load_yml(filepath):
    with open(filepath, 'r') as f:
        data = yaml.load(f.read())
    return data