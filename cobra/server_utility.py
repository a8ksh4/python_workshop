from hashlib import sha256
from tinydb import TinyDB, Query
from random import randint
from uuid import uuid4
from time import time
from utility import encode_message

def make_salt():
    return str(randint(0, 99999999)).zfill(8)

def hash_creds(password, salt):
    return sha256(password.encode('ascii') + salt.encode('ascii')).hexdigest()

def get_user(username):
    userdb = TinyDB('userdb.json')
    users = userdb.table('users')
    query = Query()
    getinfo = users.get(query.name == username)
    if getinfo:
        return getinfo
    else:
        return False

def create_new_session(username):
    userdb = TinyDB('userdb.json')
    users = userdb.table('users')
    query = Query()
    userinfo = get_user(username)
    sessionid = uuid4().hex
    salt = userinfo['ip']
    sessionhash = hash_creds(sessionid, salt)
    users.update({'sessionid':sessionhash, 'timestamp': time()}, query.name==username)
    return encode_message(sessionid)

def check_session_id(username, id, ip):
    userinfo = get_user(username)
    # timeout session if not active for over an hour
    if userinfo['timestamp'] + 3600 < time():
        return False
    if userinfo['sessionid'] == hash_creds(id, ip):
        return True
    else:
        return False
    
def add_user(username, password, ip):
    # check if name already exists
    if get_user(username):
        return None
    userdb = TinyDB('userdb.json')
    users = userdb.table('users')
    salt = make_salt()
    pwhash = hash_creds(password, salt)
    users.insert({'name': username, 'hash': pwhash, 'salt': salt, 'sessionid': None, 'ip': ip, 'timestamp': None, 'completed':[]})
    return create_new_session(username)

def login_user(username, password, ip):
    userdb = TinyDB('userdb.json')
    users = userdb.table('users')
    query = Query()
    userinfo = get_user(username)
    if userinfo:
        pass
    else:
        return None
    if userinfo['hash'] == hash_creds(password, userinfo['salt']):
        users.update({'ip':ip}, query.name==username)
        return create_new_session(username)
    else:
        return None
    
def add_user_solution(username, solution):
    pass
    
    
