from hashlib import sha256
from random import randint
from uuid import uuid4
from time import time
from util.utility import encode_message, load_yml, save_yml
from os.path import isfile
from os import listdir
        
class User():
    def __init__(self, name):
        self.name = name
        self.filepath = 'users/{file}.yml'.format(file=self.name)
        self.exists = False
        if self.user_exists():
            self.userinfo = load_yml(self.filepath)
            self.exists = True
        else:
            self.userinfo = {'name': self.name, 'hash': None, 'salt': None, 'sessionid': None, 'ip': None, 'timestamp': None, 'completed': [], 'seed': 0}
        
    def user_exists(self): 
        return isfile(self.filepath)

    def create_user(self, password, ip):
        if self.user_exists():
            return False
        salt = make_salt()
        pwhash = hash_creds(password, salt)
        self.update_user({'hash': pwhash, 'salt': salt, 'ip': ip, 'seed': self.new_seed()})
        self.exists = True
        return True        
        
    def update_user(self, data):
        self.userinfo.update(data)
        save_yml(self.filepath, self.userinfo)
        
    def get_completed(self):
        return self.userinfo['completed']
        
    def update_completed(self, item):
        if item in self.userinfo['completed']:
            pass
        else:
            self.update_user({'completed': self.get_completed() + [item]})
    
    def check_completed(self, item):
        if item in self.userinfo['completed']:
            return True
        else:
            return False
    
    def create_new_session(self):
        sessionid = uuid4().hex
        salt = self.userinfo['ip']
        sessionhash = hash_creds(sessionid, salt)
        self.update_user({'sessionid':sessionhash, 'timestamp': time()})
        return encode_message(sessionid)

    def check_session_id(self, id, ip):
        # timeout session if not active for over an hour
        if self.userinfo['timestamp'] + 3600 < time():
            return False
        # check to see if id is valid for ip
        elif self.userinfo['sessionid'] == hash_creds(id, ip):
            return True
        else:
            return False

    def login_user(self, password, ip):
        if self.userinfo['hash'] == hash_creds(password, self.userinfo['salt']):
            self.update_user({'ip': ip})
            return self.create_new_session()
        else:
            return False
            
    def new_seed(self):
        #self.update_user({'seed': int(make_salt())})
        self.update_user({'seed': int(111)}) # static seed until I can figure out a bug
        return self.get_seed()
        
    def get_seed(self):
        return self.userinfo['seed']
        

class Questions():
    def __init__(self):
        self.questions = {filename.rstrip('.yml'): load_yml('enabled/{}'.format(filename)) for filename in listdir('enabled')}

    def get_lessons(self):
        return list(self.questions.keys())
        
    def get_questions(self, lesson):
        return list(self.questions[lesson].keys())
        
    def get_question(self, lesson, question_label):
        return dict(self.questions[lesson][question_label])
        

def get_users():
    return {filename.rsplit('.yml', maxsplit=1)[0]: User(filename.rsplit('.yml', maxsplit=1)[0])
            for filename in listdir('users')}

def make_salt():
    return str(randint(0, 99999999)).zfill(8)
   
def hash_creds(password, salt):
    return sha256(password.encode('ascii') + salt.encode('ascii')).hexdigest()
    
def update_history(item, user, solution, stats):
    print(item)
    yml_file = 'history/{0}__{1}.yml'.format(*item)
    if isfile(yml_file):
        history_data = load_yml(yml_file)
    else:
        history_data = {}
    print(history_data)
    history_data[user] = {'solution': solution, 'stats': stats}
    save_yml(yml_file, history_data)
    
def get_history(item):
    yml_file = 'history/{0}__{1}.yml'.format(*item)
    if isfile(yml_file):
        history_data = load_yml(yml_file)
        return history_data
    else:
        return False