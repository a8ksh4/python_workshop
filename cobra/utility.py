import os
from base64 import b64encode
from hashlib import sha1

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def encode_solution(soultion):
    return b64encode(soultion.encode('ascii')).decode('utf-8')
    
def hash_results(token, results):
    hash = sha1(token.encode('ascii'))
    for result in results:
        hash.update(str(result).encode('ascii'))
    return hash.hexdigest()
