from hashlib import sha256
from tinydb import TinyDB

def hash_creds(password, salt=None):
    if not salt:
        salt = str(randint(0, 99999999)).zfill(8)
    return sha256(password.encode('ascii') + salt.encode('ascii')).hexdigest(), salt


def add_user(username, password):
    userdb = TinyDB('userdb.json')
    users = userdb.table('users')
    pwhash, salt = hash_cread(password)
    userdb.insert({'name': username, 'hash': pwhash, 'salt': salt})
